#!/usr/bin/env python3
"""
Metrics Monkey — Motorcycle Repair AI Benchmark
Usage:
  python run_benchmark.py [options]

Options:
  --models   Comma-separated model keys from config.MODELS (default: all available)
  --cases    Comma-separated case IDs to run (default: all 25)
  --no-context   Disable RAG context injection
  --judge        Enable LLM-as-judge scoring (requires OPENROUTER_API_KEY)
  --report       Print comparison tables after run
  --markdown     Also export a Markdown report to results/report.md
  --quick        Run only the first 5 cases (smoke test)

Examples:
  # Run all available local models
  python run_benchmark.py --models gemma_2b,gemma_4b --report

  # Full run with cloud models and LLM judge
  python run_benchmark.py --judge --report --markdown

  # Quick smoke test
  python run_benchmark.py --quick --models gemma_4b
"""
import argparse
import sys
from pathlib import Path

from config import MODELS, OPENROUTER_API_KEY
from models.ollama_model import OllamaModel
from models.openrouter_model import OpenRouterModel, OpenAIModel, MistralModel
from benchmark.evaluator import Evaluator
from results.report import print_summary_table, print_per_case_table, export_markdown
from results.visualize import generate_all as generate_figures
from results.team_report import generate as generate_team_report


def build_model(key: str, cfg: dict):
    t = cfg["type"]
    if t == "ollama":
        return OllamaModel(cfg["model_id"], cfg["display"])
    elif t == "openrouter":
        return OpenRouterModel(cfg["model_id"], cfg["display"])
    elif t == "openai":
        return OpenAIModel(cfg["model_id"], cfg["display"])
    elif t == "mistral":
        return MistralModel(cfg["model_id"], cfg["display"])
    raise ValueError(f"Unknown model type: {t}")


def main():
    parser = argparse.ArgumentParser(description="Motorcycle repair AI benchmark")
    parser.add_argument("--models", default="", help="Comma-separated model keys (or 'local'/'foundational'/'all')")
    parser.add_argument("--cases", default="", help="Comma-separated case IDs")
    parser.add_argument("--no-context", action="store_true", help="Disable manual context injection")
    parser.add_argument("--judge", action="store_true", help="Enable LLM-as-judge scoring")
    parser.add_argument("--report", action="store_true", help="Print tables after run")
    parser.add_argument("--markdown", action="store_true", help="Export Markdown report + figures + team report")
    parser.add_argument("--quick", action="store_true", help="Run only first 5 cases")
    args = parser.parse_args()

    # Resolve which models to run
    raw = args.models.strip()
    if raw in ("local", "foundational", "finetuned"):
        requested_keys = [k for k, v in MODELS.items() if v.get("group") == raw]
    elif raw == "all" or not raw:
        requested_keys = list(MODELS.keys())
    else:
        requested_keys = [k.strip() for k in raw.split(",") if k.strip()]

    models = []
    for key in requested_keys:
        if key not in MODELS:
            print(f"[warn] Unknown model key '{key}', skipping")
            continue
        cfg = MODELS[key]
        try:
            m = build_model(key, cfg)
        except Exception as e:
            print(f"[warn] Could not build model {key}: {e}")
            continue

        if not m.is_available():
            if cfg.get("skip_if_missing"):
                print(f"[skip] {cfg['display']} not available (placeholder)")
            else:
                print(f"[warn] {cfg['display']} not reachable — skipping")
            continue
        models.append(m)

    if not models:
        print("[error] No models available. Check Ollama is running and/or API keys are set.")
        sys.exit(1)

    print(f"\nRunning benchmark with {len(models)} model(s):")
    for m in models:
        print(f"  • {m.display_name} ({m.model_id})")

    # Resolve which cases to run
    case_ids = None
    if args.cases:
        case_ids = [c.strip() for c in args.cases.split(",") if c.strip()]
    elif args.quick:
        case_ids = ["TC001", "TC002", "TC007", "TC012", "TC016"]

    evaluator = Evaluator(
        models=models,
        run_llm_judge=args.judge,
        case_ids=case_ids,
        use_context=not args.no_context,
    )

    results = evaluator.run()
    results_path = evaluator.save_results(results)

    if args.report or args.markdown:
        print_summary_table(results)
        print_per_case_table(results)

    if args.markdown:
        md_path = Path("results") / "benchmark_report.md"
        export_markdown(results, str(md_path))

        # Generate figures
        print("\nGenerating figures...")
        generate_figures(str(results_path))

        # Generate team report
        team_path = Path("results") / "team_report.md"
        generate_team_report(results, out_path=str(team_path))
        print(f"Team report → {team_path}")

    return str(results_path)


if __name__ == "__main__":
    main()
