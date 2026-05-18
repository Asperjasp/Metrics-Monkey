"""
Automatic evaluation metrics for motorcycle repair Q&A.

Scoring philosophy:
  - No single metric is perfect; we use a weighted composite.
  - Where ground truth exists, we use ROUGE-L for lexical overlap.
  - Keyword coverage rewards domain-correct terminology.
  - Length heuristics penalize non-answers and padding.
  - LLM-as-judge (optional) gives holistic quality signals.
"""
import re
import json
import math
import requests
from typing import Optional
from config import OPENROUTER_API_KEY, JUDGE_PROMPT_TEMPLATE

# Weights for the composite score
WEIGHTS = {
    "keyword_coverage": 0.30,
    "rouge_l": 0.25,
    "length_score": 0.10,
    "safety_compliance": 0.10,
    "llm_judge": 0.25,   # only applied when API key available
}


# --- individual metrics ---

def keyword_coverage(response: str, keywords: list[str]) -> float:
    """Fraction of expected domain keywords present in the response (0–1)."""
    if not keywords:
        return 1.0
    resp_lower = response.lower()
    hits = sum(1 for kw in keywords if kw.lower() in resp_lower)
    return hits / len(keywords)


def rouge_l(response: str, reference: str) -> float:
    """
    ROUGE-L F1 score between response and reference.
    Uses token-level LCS without importing rouge_score (keeps deps optional).
    Falls back to rouge_score library if available.
    """
    try:
        from rouge_score import rouge_scorer
        scorer = rouge_scorer.RougeScorer(["rougeL"], use_stemmer=False)
        scores = scorer.score(reference, response)
        return scores["rougeL"].fmeasure
    except ImportError:
        return _rouge_l_manual(response, reference)


def _rouge_l_manual(hyp: str, ref: str) -> float:
    """Pure-python LCS-based ROUGE-L."""
    hyp_tokens = hyp.lower().split()
    ref_tokens = ref.lower().split()
    if not hyp_tokens or not ref_tokens:
        return 0.0
    lcs = _lcs_length(hyp_tokens, ref_tokens)
    precision = lcs / len(hyp_tokens)
    recall = lcs / len(ref_tokens)
    if precision + recall == 0:
        return 0.0
    return 2 * precision * recall / (precision + recall)


def _lcs_length(a: list, b: list) -> int:
    m, n = len(a), len(b)
    # Space-optimised LCS
    prev = [0] * (n + 1)
    for i in range(1, m + 1):
        curr = [0] * (n + 1)
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                curr[j] = prev[j - 1] + 1
            else:
                curr[j] = max(prev[j], curr[j - 1])
        prev = curr
    return prev[n]


def length_score(response: str, min_words: int = 30, max_words: int = 500) -> float:
    """
    Penalises very short (likely incomplete) or very long (padded) answers.
    Returns 1.0 for responses in the sweet spot.
    """
    words = len(response.split())
    if words < min_words:
        return words / min_words
    if words > max_words:
        # Soft ceiling — long but not terrible
        return max(0.5, 1.0 - (words - max_words) / max_words * 0.5)
    return 1.0


SAFETY_KEYWORDS = [
    "safety", "caution", "warning", "danger", "precaution",
    "seguridad", "advertencia", "peligro", "precaución", "cuidado",
    "ventilated", "ventilado", "exhaust", "escape",
    "immediately", "inmediatamente",
    "protective", "protección",
]

def safety_compliance(response: str, case: dict) -> float:
    """
    For safety-category questions, checks whether the response includes
    safety language. For non-safety questions returns 1.0 (not penalised).
    """
    if case.get("category") != "safety":
        return 1.0
    resp_lower = response.lower()
    hits = sum(1 for kw in SAFETY_KEYWORDS if kw in resp_lower)
    return min(1.0, hits / 2)  # at least 2 safety terms = full score


def llm_judge_score(
    question: str,
    context: str,
    response: str,
    judge_model: str = "openai/gpt-4o-mini",
) -> Optional[dict]:
    """
    Uses a strong LLM (via OpenRouter) to score the response on 5 dimensions.
    Returns a dict with keys: accuracy, completeness, safety, usefulness, no_hallucination, overall.
    Returns None if no API key is configured or call fails.
    """
    if not OPENROUTER_API_KEY:
        return None
    prompt = JUDGE_PROMPT_TEMPLATE.format(
        question=question, context=context[:2000], response=response
    )
    try:
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": judge_model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.0,
        }
        resp = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=30,
        )
        resp.raise_for_status()
        raw = resp.json()["choices"][0]["message"]["content"]
        # Extract JSON from the response
        match = re.search(r"\{.*?\}", raw, re.DOTALL)
        if match:
            return json.loads(match.group())
    except Exception as e:
        print(f"[judge] error: {e}")
    return None


# --- composite scorer ---

def score_response(
    response: str,
    case: dict,
    context: str = "",
    run_llm_judge: bool = True,
) -> dict:
    """
    Computes all metrics for a single (case, response) pair.
    Returns a dict with individual scores and a weighted composite.
    """
    keywords = case.get("context_keywords", [])
    ground_truth = case.get("ground_truth", "")

    kc = keyword_coverage(response, keywords)
    rl = rouge_l(response, ground_truth) if ground_truth else 0.5
    ls = length_score(response)
    sc = safety_compliance(response, case)

    judge = None
    if run_llm_judge:
        judge = llm_judge_score(case["question"], context, response)

    judge_score_norm = (judge["overall"] / 10.0) if judge else None

    # Composite — redistribute LLM judge weight if unavailable
    if judge_score_norm is not None:
        composite = (
            WEIGHTS["keyword_coverage"] * kc
            + WEIGHTS["rouge_l"] * rl
            + WEIGHTS["length_score"] * ls
            + WEIGHTS["safety_compliance"] * sc
            + WEIGHTS["llm_judge"] * judge_score_norm
        )
    else:
        # Redistribute judge weight proportionally
        total_non_judge = 1 - WEIGHTS["llm_judge"]
        composite = (
            (WEIGHTS["keyword_coverage"] / total_non_judge) * kc
            + (WEIGHTS["rouge_l"] / total_non_judge) * rl
            + (WEIGHTS["length_score"] / total_non_judge) * ls
            + (WEIGHTS["safety_compliance"] / total_non_judge) * sc
        )

    return {
        "keyword_coverage": round(kc, 3),
        "rouge_l": round(rl, 3),
        "length_score": round(ls, 3),
        "safety_compliance": round(sc, 3),
        "llm_judge": judge,
        "composite": round(composite, 3),
    }
