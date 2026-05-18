"""
Generates human-readable comparison tables from benchmark JSON results.
Supports Markdown output (for papers/READMEs) and terminal pretty-print.
"""
import json
import sys
from pathlib import Path
from collections import defaultdict


def load_results(path: str) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def aggregate_scores(results: dict) -> dict:
    """Returns per-model aggregate stats across all test cases."""
    model_scores: dict[str, list[dict]] = defaultdict(list)
    model_latencies: dict[str, list[float]] = defaultdict(list)

    for case in results["results"]:
        for model_name, data in case["models"].items():
            if data.get("scores"):
                model_scores[model_name].append(data["scores"])
            if data.get("latency_s") is not None:
                model_latencies[model_name].append(data["latency_s"])

    agg = {}
    for model, score_list in model_scores.items():
        n = len(score_list)
        agg[model] = {
            "n_cases": n,
            "composite": round(sum(s["composite"] for s in score_list) / n, 3),
            "keyword_coverage": round(sum(s["keyword_coverage"] for s in score_list) / n, 3),
            "rouge_l": round(sum(s["rouge_l"] for s in score_list) / n, 3),
            "length_score": round(sum(s["length_score"] for s in score_list) / n, 3),
            "avg_latency_s": round(sum(model_latencies[model]) / len(model_latencies[model]), 1)
            if model_latencies[model] else None,
        }
    return agg


def aggregate_by_difficulty(results: dict) -> dict:
    """Returns per-model per-difficulty composite score."""
    data: dict[str, dict[str, list[float]]] = defaultdict(lambda: defaultdict(list))
    for case in results["results"]:
        diff = case["difficulty"]
        for model_name, mdata in case["models"].items():
            if mdata.get("scores"):
                data[model_name][diff].append(mdata["scores"]["composite"])
    out = {}
    for model, diffs in data.items():
        out[model] = {d: round(sum(v) / len(v), 3) for d, v in diffs.items()}
    return out


def aggregate_by_category(results: dict) -> dict:
    """Returns per-model per-category composite score."""
    data: dict[str, dict[str, list[float]]] = defaultdict(lambda: defaultdict(list))
    for case in results["results"]:
        cat = case["category"]
        for model_name, mdata in case["models"].items():
            if mdata.get("scores"):
                data[model_name][cat].append(mdata["scores"]["composite"])
    out = {}
    for model, cats in data.items():
        out[model] = {c: round(sum(v) / len(v), 3) for c, v in cats.items()}
    return out


def print_summary_table(results: dict):
    """Prints the main comparison table to stdout."""
    try:
        from tabulate import tabulate
    except ImportError:
        tabulate = None

    agg = aggregate_scores(results)
    models = list(agg.keys())

    headers = ["Model", "Composite ↑", "KW Coverage ↑", "ROUGE-L ↑", "Length ↑", "Avg Latency (s)"]
    rows = []
    for model in sorted(models, key=lambda m: agg[m]["composite"], reverse=True):
        s = agg[model]
        rows.append([
            model,
            f"{s['composite']:.3f}",
            f"{s['keyword_coverage']:.3f}",
            f"{s['rouge_l']:.3f}",
            f"{s['length_score']:.3f}",
            f"{s['avg_latency_s']}s" if s["avg_latency_s"] else "—",
        ])

    if tabulate:
        print("\n=== BENCHMARK SUMMARY ===")
        print(tabulate(rows, headers=headers, tablefmt="github"))
    else:
        print("\n=== BENCHMARK SUMMARY ===")
        print(" | ".join(headers))
        for row in rows:
            print(" | ".join(str(x) for x in row))


def print_per_case_table(results: dict):
    """Prints composite score per case per model."""
    try:
        from tabulate import tabulate
    except ImportError:
        tabulate = None

    cases = results["results"]
    models = list(cases[0]["models"].keys()) if cases else []

    headers = ["ID", "Cat", "Diff", "Lang"] + models
    rows = []
    for case in cases:
        row = [case["case_id"], case["category"][:8], case["difficulty"][:4], case.get("language", "es")]
        for model in models:
            mdata = case["models"].get(model, {})
            if mdata.get("scores"):
                row.append(f"{mdata['scores']['composite']:.3f}")
            elif mdata.get("error"):
                row.append("ERR")
            else:
                row.append("—")
        rows.append(row)

    if tabulate:
        print("\n=== PER-CASE SCORES ===")
        print(tabulate(rows, headers=headers, tablefmt="github"))
    else:
        print("\n=== PER-CASE SCORES ===")
        print(" | ".join(headers))
        for row in rows:
            print(" | ".join(str(x) for x in row))


def export_markdown(results: dict, output_path: str):
    """Exports a full Markdown report (suitable for a paper appendix or README)."""
    agg = aggregate_scores(results)
    by_diff = aggregate_by_difficulty(results)
    by_cat = aggregate_by_category(results)
    meta = results["metadata"]

    lines = [
        "# Metrics Monkey — Benchmark Results",
        "",
        f"**Run date:** {meta['timestamp'][:10]}  ",
        f"**Models tested:** {', '.join(meta['models'])}  ",
        f"**Test cases:** {meta['total_cases']}  ",
        f"**Context (RAG):** {'yes' if meta.get('use_context') else 'no'}  ",
        f"**LLM judge:** {'yes' if meta.get('llm_judge') else 'no'}  ",
        "",
        "---",
        "",
        "## Overall Scores",
        "",
    ]

    # Overall table
    sorted_models = sorted(agg.keys(), key=lambda m: agg[m]["composite"], reverse=True)
    header = "| Model | Composite ↑ | KW Coverage ↑ | ROUGE-L ↑ | Length ↑ | Avg Latency |"
    sep = "|---|---|---|---|---|---|"
    lines += [header, sep]
    for model in sorted_models:
        s = agg[model]
        lat = f"{s['avg_latency_s']}s" if s["avg_latency_s"] else "—"
        lines.append(f"| {model} | **{s['composite']:.3f}** | {s['keyword_coverage']:.3f} | {s['rouge_l']:.3f} | {s['length_score']:.3f} | {lat} |")

    lines += ["", "---", "", "## Scores by Difficulty", ""]
    diffs = ["easy", "medium", "hard"]
    header = "| Model | " + " | ".join(d.capitalize() for d in diffs) + " |"
    sep = "|---|" + "---|" * len(diffs)
    lines += [header, sep]
    for model in sorted_models:
        d_scores = by_diff.get(model, {})
        row = f"| {model} | " + " | ".join(f"{d_scores.get(d, '—')}" for d in diffs) + " |"
        lines.append(row)

    lines += ["", "---", "", "## Scores by Category", ""]
    cats = sorted({c for m in by_cat.values() for c in m})
    header = "| Model | " + " | ".join(c[:10].capitalize() for c in cats) + " |"
    sep = "|---|" + "---|" * len(cats)
    lines += [header, sep]
    for model in sorted_models:
        c_scores = by_cat.get(model, {})
        row = f"| {model} | " + " | ".join(f"{c_scores.get(c, '—')}" for c in cats) + " |"
        lines.append(row)

    # Placeholder rows for models not yet run
    lines += [
        "",
        "---",
        "",
        "## Fine-tuned Model Placeholder",
        "",
        "> The following row will be filled once the fine-tuned Gemma 2B model is available.",
        "",
        "| Model | Composite ↑ | KW Coverage ↑ | ROUGE-L ↑ | Length ↑ | Avg Latency |",
        "|---|---|---|---|---|---|",
        "| Gemma 2B Fine-tuned | _TBD_ | _TBD_ | _TBD_ | _TBD_ | _TBD_ |",
        "",
        "---",
        "",
        "## Metric Definitions",
        "",
        "| Metric | Description | Weight |",
        "|---|---|---|",
        "| **Composite** | Weighted average of all metrics below | — |",
        "| **KW Coverage** | Fraction of expected domain keywords present in response | 30% |",
        "| **ROUGE-L** | F1 score of Longest Common Subsequence vs ground-truth excerpt | 25% |",
        "| **Length Score** | Penalises too-short (<30 words) or too-long (>500 words) responses | 10% |",
        "| **Safety Compliance** | For safety-category questions: presence of safety language | 10% |",
        "| **LLM Judge** | GPT-4o-mini scores accuracy/completeness/hallucination (0–10 → 0–1) | 25% |",
        "",
        "> Note: LLM judge weight is redistributed proportionally when no API key is configured.",
        "",
        "---",
        "",
        "## References",
        "",
        "- Gemma 4 model family: https://huggingface.co/google/gemma-4-E4B-it",
        "- Open LLM Leaderboard: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard",
        "- ROUGE metric: Lin, C.-Y. (2004). ROUGE: A Package for Automatic Evaluation of Summaries. ACL Workshop.",
        "- LLM-as-judge: Zheng et al. (2023). Judging LLM-as-a-Judge with MT-Bench. NeurIPS.",
        "- RAG benchmark methodology: Es et al. (2023). RAGAS: Automated Evaluation of RAG Pipelines. EACL.",
    ]

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Markdown report saved to {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python -m results.report <results_json> [--markdown output.md]")
        sys.exit(1)

    results = load_results(sys.argv[1])
    print_summary_table(results)
    print_per_case_table(results)

    if "--markdown" in sys.argv:
        idx = sys.argv.index("--markdown")
        md_path = sys.argv[idx + 1] if idx + 1 < len(sys.argv) else "benchmark_report.md"
        export_markdown(results, md_path)
