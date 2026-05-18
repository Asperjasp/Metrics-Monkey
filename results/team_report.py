"""
Generates a structured team report for the finetuning leader (Juan Bernardo).
Shows:
  1. Full results table with every question + model response
  2. Which test cases the finetuned model must beat to justify finetuning
  3. Concrete improvement targets per metric
  4. Suggested action items for the finetuning pipeline

Usage:
  python -m results.team_report results/benchmark_YYYYMMDD.json [--out report.md]
"""
import json
import sys
from pathlib import Path
from collections import defaultdict
from datetime import datetime


def load(path: str) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _avg(lst: list) -> float:
    return round(sum(lst) / len(lst), 3) if lst else 0.0


def _medal(score: float) -> str:
    if score >= 0.80: return "🟢"
    if score >= 0.60: return "🟡"
    return "🔴"


def generate(results: dict, out_path: str = None) -> str:
    meta   = results["metadata"]
    cases  = results["results"]
    models = meta["models"]

    # ── aggregate ────────────────────────────────────────────────────────────
    agg: dict[str, dict[str, list]] = defaultdict(lambda: defaultdict(list))
    for case in cases:
        for model, mdata in case["models"].items():
            if mdata.get("scores"):
                for metric, val in mdata["scores"].items():
                    if isinstance(val, (int, float)):
                        agg[model][metric].append(val)

    model_avg = {m: {k: _avg(v) for k, v in metrics.items()} for m, metrics in agg.items()}

    # ── identify baseline (first non-finetuned model) ─────────────────────
    baseline_model = models[0] if models else None

    lines = [
        "# Metrics Monkey — Team Report",
        f"> Generated {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "---",
        "",
        "## 1. Executive Summary",
        "",
    ]

    # Summary table
    metric_cols = ["composite", "keyword_coverage", "rouge_l", "spec_recall",
                   "step_completeness", "hallucination_risk"]
    lines.append("| Model | " + " | ".join(m.replace("_", " ").title() for m in metric_cols) + " |")
    lines.append("|---|" + "---|" * len(metric_cols))
    for model in models:
        s = model_avg.get(model, {})
        row_vals = []
        for m in metric_cols:
            v = s.get(m, 0)
            row_vals.append(f"{_medal(v)} {v:.3f}")
        lines.append(f"| **{model}** | " + " | ".join(row_vals) + " |")

    lines += [
        "",
        "> 🟢 ≥ 0.80 · 🟡 0.60–0.79 · 🔴 < 0.60",
        "",
        "---",
        "",
        "## 2. Finetuning Impact Assessment",
        "",
        "The table below shows the **minimum composite score the finetuned model must reach** to",
        "demonstrate meaningful improvement over the base model on each difficulty tier.",
        "",
    ]

    # Per-difficulty baseline
    diff_scores: dict[str, dict[str, list]] = defaultdict(lambda: defaultdict(list))
    for case in cases:
        diff = case["difficulty"]
        for model, mdata in case["models"].items():
            if mdata.get("scores"):
                diff_scores[diff][model].append(mdata["scores"]["composite"])

    diffs = ["easy", "medium", "hard"]
    lines.append("| Difficulty | Baseline | Target (baseline + 0.10) | Pass bar |")
    lines.append("|---|---|---|---|")
    for d in diffs:
        base = _avg(diff_scores[d].get(baseline_model, [0])) if baseline_model else 0
        target = min(1.0, base + 0.10)
        lines.append(f"| {d.capitalize()} | {base:.3f} | **{target:.3f}** | {_medal(target)} |")

    lines += [
        "",
        "---",
        "",
        "## 3. Weakest Test Cases (Finetuning Priorities)",
        "",
        "These are the questions where the baseline model scored **below 0.60**.",
        "The finetuned model should be evaluated on these first.",
        "",
    ]

    low_cases = []
    for case in cases:
        for model, mdata in case["models"].items():
            s = mdata.get("scores", {})
            if s and s.get("composite", 1) < 0.60:
                low_cases.append((s["composite"], case, model))

    low_cases.sort(key=lambda x: x[0])
    lines.append("| ID | Question | Category | Diff | Score | Model |")
    lines.append("|---|---|---|---|---|---|")
    for score, case, model in low_cases[:15]:
        q = case["question"][:70].replace("|", "\\|") + ("…" if len(case["question"]) > 70 else "")
        lines.append(f"| {case['case_id']} | {q} | {case['category']} | {case['difficulty']} | {score:.3f} | {model} |")

    lines += [
        "",
        "---",
        "",
        "## 4. Full Question-by-Question Results",
        "",
        "Every test case with question, ground truth, and per-model responses.",
        "",
    ]

    for case in cases:
        lines += [
            f"### {case['case_id']} · {case['category']} · {case['difficulty']} · `{case.get('language','es')}`",
            "",
            f"**Question:** {case['question']}",
            "",
            f"**Ground truth:** {case.get('ground_truth', '—')[:300]}{'…' if len(case.get('ground_truth','')) > 300 else ''}",
            "",
        ]
        for model in models:
            mdata = case["models"].get(model, {})
            resp  = mdata.get("response") or "_error / no response_"
            scores = mdata.get("scores") or {}
            s_str = ""
            if scores:
                s_str = (
                    f"composite={scores.get('composite','?'):.3f} · "
                    f"kw={scores.get('keyword_coverage','?'):.2f} · "
                    f"rouge={scores.get('rouge_l','?'):.2f} · "
                    f"spec={scores.get('spec_recall','?'):.2f} · "
                    f"halluc_risk={scores.get('hallucination_risk','?'):.2f}"
                )
            lines += [
                f"<details><summary>🤖 <b>{model}</b> — {s_str}</summary>",
                "",
                f"{resp[:600]}{'…' if len(resp) > 600 else ''}",
                "",
                "</details>",
                "",
            ]
        lines.append("---")
        lines.append("")

    lines += [
        "## 5. Recommendations for Finetuning Pipeline",
        "",
        "Based on the metric breakdown, here are the highest-leverage improvements:",
        "",
    ]

    # Auto-generate recommendations from weakest metrics
    if baseline_model and model_avg.get(baseline_model):
        bm = model_avg[baseline_model]
        recs = []

        if bm.get("spec_recall", 1) < 0.70:
            recs.append(
                "**Spec Recall is low** — the model rarely states exact torque values or service intervals. "
                "Include training examples where the answer MUST cite the exact numeric spec. "
                "Consider adding a system-prompt instruction: 'Always quote the specific value from the manual.'"
            )
        if bm.get("hallucination_risk", 1) < 0.70:
            recs.append(
                "**Hallucination Risk is high** — the model invents numbers not in the manual. "
                "Fine-tune with negative examples that show incorrect spec fabrication and their corrections. "
                "Add context-grounding instruction to the system prompt."
            )
        if bm.get("step_completeness", 1) < 0.60:
            recs.append(
                "**Step Completeness is low** — procedural answers lack numbered steps. "
                "Training data should include examples formatted as numbered lists. "
                "Prompt: 'If the answer involves a procedure, always number the steps.'"
            )
        if bm.get("safety_compliance", 1) < 0.70:
            recs.append(
                "**Safety Compliance is low** — safety questions miss safety language. "
                "Add safety-specific Q&A pairs to the fine-tuning set, ensuring every answer "
                "about fuels, brakes, or running engines includes a warning."
            )
        if bm.get("rouge_l", 1) < 0.30:
            recs.append(
                "**ROUGE-L is low** — responses use different vocabulary than the manual. "
                "This may reflect paraphrasing (not always bad), but if spec terminology is "
                "substituted for generic language, fine-tuning on domain vocabulary will help."
            )

        if not recs:
            recs.append("Baseline scores are solid across all metrics — focus on spec recall and hard cases.")

        for i, rec in enumerate(recs, 1):
            lines.append(f"{i}. {rec}")
            lines.append("")

    lines += [
        "",
        "---",
        "",
        "## 6. How to Run the Benchmark on the Fine-tuned Model",
        "",
        "```bash",
        "# 1. Register the fine-tuned model in Ollama",
        "ollama create gemma2b-moto -f Modelfile",
        "",
        "# 2. Update config.py  →  gemma_2b_finetuned  →  model_id = 'gemma2b-moto:latest'",
        "",
        "# 3. Run comparison (base vs finetuned vs SOTA)",
        "python run_benchmark.py \\",
        "  --models gemma_9b,gemma_2b_finetuned,gpt4o \\",
        "  --report --markdown",
        "",
        "# 4. Generate figures",
        "python -m results.visualize results/benchmark_YYYYMMDD_HHMMSS.json",
        "",
        "# 5. Build team report",
        "python -m results.team_report results/benchmark_YYYYMMDD_HHMMSS.json --out team_report.md",
        "```",
        "",
        "---",
        "",
        "_Report generated by Metrics Monkey — Hackathon Gemma G4_",
    ]

    report = "\n".join(lines)

    if out_path:
        Path(out_path).write_text(report, encoding="utf-8")
        print(f"Team report saved to {out_path}")

    return report


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python -m results.team_report <results_json> [--out path.md]")
        sys.exit(1)
    res = load(sys.argv[1])
    out = None
    if "--out" in sys.argv:
        idx = sys.argv.index("--out")
        out = sys.argv[idx + 1] if idx + 1 < len(sys.argv) else "team_report.md"
    generate(res, out_path=out or "results/team_report.md")
