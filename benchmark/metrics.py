"""
Automatic evaluation metrics for motorcycle repair Q&A.

Metrics:
  keyword_coverage   - fraction of expected domain keywords in response (0-1)
  rouge_l            - lexical overlap with ground-truth excerpt (0-1)
  spec_recall        - critical numbers/specs from ground truth present (0-1)
  step_completeness  - for procedural questions: structured steps detected (0-1)
  hallucination_risk - specs in response NOT found in context (0=many, 1=none)
  length_score       - penalises <30-word and >500-word responses (0-1)
  safety_compliance  - safety language for safety-category questions (0-1)
  llm_judge          - GPT-4o-mini scores 5 dimensions (0-10 → 0-1, optional)
  composite          - weighted combination of the above
"""
import re
import json
import requests
from typing import Optional
from config import OPENROUTER_API_KEY, JUDGE_PROMPT_TEMPLATE

WEIGHTS = {
    "keyword_coverage":   0.25,
    "rouge_l":            0.20,
    "spec_recall":        0.15,
    "step_completeness":  0.10,
    "hallucination_risk": 0.10,
    "length_score":       0.05,
    "safety_compliance":  0.05,
    "llm_judge":          0.10,
}


# ── 1. Keyword Coverage ───────────────────────────────────────────────────────

def keyword_coverage(response: str, keywords: list[str]) -> float:
    """Fraction of expected domain keywords present in the response."""
    if not keywords:
        return 1.0
    resp_lower = response.lower()
    hits = sum(1 for kw in keywords if kw.lower() in resp_lower)
    return hits / len(keywords)


# ── 2. ROUGE-L ────────────────────────────────────────────────────────────────

def rouge_l(response: str, reference: str) -> float:
    """ROUGE-L F1 between response and ground-truth reference."""
    try:
        from rouge_score import rouge_scorer
        scorer = rouge_scorer.RougeScorer(["rougeL"], use_stemmer=False)
        return scorer.score(reference, response)["rougeL"].fmeasure
    except ImportError:
        return _rouge_l_manual(response, reference)


def _rouge_l_manual(hyp: str, ref: str) -> float:
    h, r = hyp.lower().split(), ref.lower().split()
    if not h or not r:
        return 0.0
    lcs = _lcs_length(h, r)
    p, rc = lcs / len(h), lcs / len(r)
    return 2 * p * rc / (p + rc) if (p + rc) else 0.0


def _lcs_length(a: list, b: list) -> int:
    prev = [0] * (len(b) + 1)
    for ai in a:
        curr = [0] * (len(b) + 1)
        for j, bj in enumerate(b, 1):
            curr[j] = prev[j - 1] + 1 if ai == bj else max(prev[j], curr[j - 1])
        prev = curr
    return prev[len(b)]


# ── 3. Spec Recall ────────────────────────────────────────────────────────────
# Extracts numbers + units from the ground truth and checks if they appear in
# the response. Rewards models that actually cite the correct spec values.

_SPEC_PATTERN = re.compile(
    r"\b(\d+[\.,]?\d*)\s*"
    r"(N[·.]?m|kgf[·-]?m|km|rpm|mm|cc|°C|psi|bar|V|A|Ω|%|km/h|N·m)\b",
    re.IGNORECASE,
)

def spec_recall(response: str, ground_truth: str) -> float:
    """
    Finds numeric specs (e.g. '22 N·m', '10,000 km') in the ground truth
    and checks how many appear verbatim in the response.
    Returns 1.0 if no specs in ground truth (not a spec question).
    """
    specs_in_gt = _SPEC_PATTERN.findall(ground_truth)
    if not specs_in_gt:
        return 1.0
    resp_lower = response.lower()
    hits = 0
    for val, unit in specs_in_gt:
        pattern = val.replace(",", "[,.]?").replace(".", "[,.]?")
        if re.search(rf"{pattern}\s*{re.escape(unit)}", resp_lower, re.IGNORECASE):
            hits += 1
    return hits / len(specs_in_gt)


# ── 4. Step Completeness ──────────────────────────────────────────────────────
# For procedural questions, rewards responses that use numbered steps or
# bullet lists — a signal that the model structured its answer for practical use.

def step_completeness(response: str, case: dict) -> float:
    """
    For procedure/maintenance categories:
      - Counts numbered steps (1. / 1) / Step 1:) or bullet lines
      - Compares with expected step count derived from ground truth
    For non-procedural categories returns 1.0.
    """
    cat = case.get("category", "")
    if cat not in ("procedure", "maintenance"):
        return 1.0

    gt = case.get("ground_truth", "")
    expected_steps = max(1, len(re.findall(r"(?:^\d+[.):]|\bstep\s+\d+|\bpaso\s+\d+)", gt, re.I | re.M)))

    step_lines = re.findall(
        r"(?:^\s*\d+[.):]|^\s*[-•*]|\bstep\s+\d+|\bpaso\s+\d+)",
        response, re.I | re.M,
    )
    found = len(step_lines)
    if found == 0:
        return 0.3  # gave prose only — partial credit
    return min(1.0, found / expected_steps)


# ── 5. Hallucination Risk ─────────────────────────────────────────────────────
# Checks if the response contains numeric specs NOT found in the provided
# context. A model that invents specs (wrong torque values, wrong intervals)
# is dangerous for real mechanics.

def hallucination_risk(response: str, context: str) -> float:
    """
    Returns 1.0 if all numeric specs in the response also appear in context.
    Returns 0.0 if the response is full of invented specs.
    A response with no specs at all scores 1.0 (no risk).
    """
    specs_in_resp = _SPEC_PATTERN.findall(response)
    if not specs_in_resp:
        return 1.0
    ctx_lower = context.lower()
    verified = 0
    for val, unit in specs_in_resp:
        pattern = val.replace(",", "[,.]?").replace(".", "[,.]?")
        if re.search(rf"{pattern}\s*{re.escape(unit)}", ctx_lower, re.IGNORECASE):
            verified += 1
    verified_ratio = verified / len(specs_in_resp)
    # Score = fraction of specs that ARE in context (1 = no hallucination)
    return verified_ratio


# ── 6. Length Score ───────────────────────────────────────────────────────────

def length_score(response: str, min_words: int = 30, max_words: int = 500) -> float:
    words = len(response.split())
    if words < min_words:
        return words / min_words
    if words > max_words:
        return max(0.5, 1.0 - (words - max_words) / max_words * 0.5)
    return 1.0


# ── 7. Safety Compliance ──────────────────────────────────────────────────────

SAFETY_TERMS = [
    "safety", "caution", "warning", "danger", "precaution",
    "seguridad", "advertencia", "peligro", "precaución", "cuidado",
    "ventilated", "ventilado", "exhaust", "gases de escape",
    "immediately", "inmediatamente", "protective", "protección",
    "never", "nunca", "do not", "no use",
]

def safety_compliance(response: str, case: dict) -> float:
    if case.get("category") != "safety":
        return 1.0
    resp_lower = response.lower()
    hits = sum(1 for kw in SAFETY_TERMS if kw in resp_lower)
    return min(1.0, hits / 2)


# ── 8. LLM-as-Judge (optional) ────────────────────────────────────────────────

def llm_judge_score(
    question: str,
    context: str,
    response: str,
    judge_model: str = "openai/gpt-4o-mini",
) -> Optional[dict]:
    """
    Scores on 5 dimensions via OpenRouter. Returns None if no API key.
    Dimensions: accuracy, completeness, safety, usefulness, no_hallucination (0-10 each).
    """
    if not OPENROUTER_API_KEY:
        return None
    prompt = JUDGE_PROMPT_TEMPLATE.format(
        question=question, context=context[:2000], response=response
    )
    try:
        resp = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json",
            },
            json={"model": judge_model, "messages": [{"role": "user", "content": prompt}], "temperature": 0.0},
            timeout=30,
        )
        resp.raise_for_status()
        raw = resp.json()["choices"][0]["message"]["content"]
        match = re.search(r"\{.*?\}", raw, re.DOTALL)
        if match:
            return json.loads(match.group())
    except Exception as e:
        print(f"  [judge] {e}")
    return None


# ── Composite Scorer ──────────────────────────────────────────────────────────

def score_response(
    response: str,
    case: dict,
    context: str = "",
    run_llm_judge: bool = False,
) -> dict:
    """
    Computes all metrics for a (case, response) pair and returns a score dict.
    LLM-judge weight is redistributed proportionally when no API key is set.
    """
    kw   = keyword_coverage(response, case.get("context_keywords", []))
    rl   = rouge_l(response, case.get("ground_truth", "")) if case.get("ground_truth") else 0.5
    sr   = spec_recall(response, case.get("ground_truth", ""))
    sc_  = step_completeness(response, case)
    hr   = hallucination_risk(response, context)
    ls   = length_score(response)
    saf  = safety_compliance(response, case)

    judge = llm_judge_score(case["question"], context, response) if run_llm_judge else None
    judge_norm = judge["overall"] / 10.0 if judge else None

    active_weights = dict(WEIGHTS)
    if judge_norm is None:
        # Redistribute the LLM judge weight across the other metrics
        extra = active_weights.pop("llm_judge")
        total = sum(active_weights.values())
        active_weights = {k: v + extra * (v / total) for k, v in active_weights.items()}

    scores = {
        "keyword_coverage":   kw,
        "rouge_l":            rl,
        "spec_recall":        sr,
        "step_completeness":  sc_,
        "hallucination_risk": hr,
        "length_score":       ls,
        "safety_compliance":  saf,
    }

    composite = sum(active_weights[k] * v for k, v in scores.items())
    if judge_norm is not None:
        composite += WEIGHTS["llm_judge"] * judge_norm

    result = {k: round(v, 3) for k, v in scores.items()}
    result["llm_judge"] = judge
    result["composite"] = round(composite, 3)
    return result
