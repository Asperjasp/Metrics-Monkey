"""
Core evaluation runner.
Iterates over test cases, queries each model, scores responses, and collects results.
"""
import json
import time
import traceback
from datetime import datetime
from pathlib import Path
from typing import Optional

from models.base import BaseModel
from benchmark.metrics import score_response
from data.loader import load_test_cases, load_suzuki_corpus, get_context_for_case
from config import SYSTEM_PROMPT_ES, SYSTEM_PROMPT_EN


class Evaluator:
    def __init__(
        self,
        models: list[BaseModel],
        run_llm_judge: bool = False,
        case_ids: Optional[list[str]] = None,
        use_context: bool = True,
    ):
        self.models = models
        self.run_llm_judge = run_llm_judge
        self.use_context = use_context
        self.case_ids = set(case_ids) if case_ids else None

        print("Loading corpora...")
        self.test_cases = load_test_cases()
        self.suzuki_corpus = load_suzuki_corpus()
        print(f"  {len(self.test_cases)} test cases | {sum(len(v) for v in self.suzuki_corpus.values())} Suzuki chunks")

    def run(self) -> dict:
        """
        Runs the full benchmark. Returns a results dict structured as:
        {
            "metadata": {...},
            "results": [
                {
                    "case_id": ...,
                    "models": {
                        "display_name": {"response": ..., "scores": ..., "error": ...}
                    }
                }
            ]
        }
        """
        cases = self.test_cases
        if self.case_ids:
            cases = [c for c in cases if c["id"] in self.case_ids]

        run_meta = {
            "timestamp": datetime.now().isoformat(),
            "models": [m.display_name for m in self.models],
            "total_cases": len(cases),
            "use_context": self.use_context,
            "llm_judge": self.run_llm_judge,
        }

        all_results = []
        for case in cases:
            print(f"\n[{case['id']}] {case['question'][:70]}...")
            context = ""
            if self.use_context:
                context = get_context_for_case(case, self.suzuki_corpus)

            system_prompt = SYSTEM_PROMPT_ES if case.get("language") == "es" else SYSTEM_PROMPT_EN

            case_result = {
                "case_id": case["id"],
                "category": case["category"],
                "difficulty": case["difficulty"],
                "language": case.get("language", "es"),
                "question": case["question"],
                "ground_truth": case.get("ground_truth", ""),
                "models": {},
            }

            for model in self.models:
                print(f"  → {model.display_name}", end=" ", flush=True)
                t0 = time.time()
                try:
                    response = model.query(case["question"], context, system_prompt)
                    elapsed = round(time.time() - t0, 1)
                    scores = score_response(
                        response, case, context, run_llm_judge=self.run_llm_judge
                    )
                    print(f"✓ ({elapsed}s) composite={scores['composite']}")
                    case_result["models"][model.display_name] = {
                        "response": response,
                        "scores": scores,
                        "latency_s": elapsed,
                        "error": None,
                    }
                except Exception as e:
                    elapsed = round(time.time() - t0, 1)
                    print(f"✗ ({elapsed}s) {e}")
                    case_result["models"][model.display_name] = {
                        "response": None,
                        "scores": None,
                        "latency_s": elapsed,
                        "error": str(e),
                    }

            all_results.append(case_result)

        return {"metadata": run_meta, "results": all_results}

    def save_results(self, results: dict, output_dir: str = "results") -> Path:
        """Saves the full JSON results and returns the path."""
        out = Path(output_dir)
        out.mkdir(exist_ok=True)
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = out / f"benchmark_{ts}.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        print(f"\nResults saved to {path}")
        return path
