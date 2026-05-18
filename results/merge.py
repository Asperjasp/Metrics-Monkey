"""
Merges two benchmark JSON files into one combined result.
Use when you run local models and cloud models in separate runs.

Usage:
  python -m results.merge results/run_A.json results/run_B.json --out results/merged.json
"""
import json
import sys
from pathlib import Path
from datetime import datetime


def load(path: str) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def merge(path_a: str, path_b: str, out_path: str = None) -> dict:
    a = load(path_a)
    b = load(path_b)

    # Build lookup: case_id → case result for each file
    cases_b = {c["case_id"]: c for c in b["results"]}

    merged_cases = []
    for case_a in a["results"]:
        cid = case_a["case_id"]
        case_b = cases_b.get(cid, {})
        merged_models = dict(case_a.get("models", {}))
        merged_models.update(case_b.get("models", {}))  # B overrides A on collision
        merged_cases.append({**case_a, "models": merged_models})

    # Add any cases only in B
    cids_a = {c["case_id"] for c in a["results"]}
    for case_b in b["results"]:
        if case_b["case_id"] not in cids_a:
            merged_cases.append(case_b)

    models_a = a["metadata"].get("models", [])
    models_b = b["metadata"].get("models", [])
    all_models = models_a + [m for m in models_b if m not in models_a]

    merged = {
        "metadata": {
            "timestamp": datetime.now().isoformat(),
            "models": all_models,
            "total_cases": len(merged_cases),
            "source_files": [path_a, path_b],
            "use_context": a["metadata"].get("use_context", True),
            "llm_judge": a["metadata"].get("llm_judge") or b["metadata"].get("llm_judge"),
        },
        "results": sorted(merged_cases, key=lambda c: c["case_id"]),
    }

    if out_path:
        Path(out_path).write_text(json.dumps(merged, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"Merged {len(models_a)} + {len(models_b)} models → {out_path}")
    return merged


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python -m results.merge <file_a.json> <file_b.json> [--out merged.json]")
        sys.exit(1)
    out = None
    if "--out" in sys.argv:
        i = sys.argv.index("--out")
        out = sys.argv[i + 1]
    merge(sys.argv[1], sys.argv[2], out_path=out or "results/merged.json")
