"""
Phone Test — 5 questions to compare with AI Edge Gallery (Android) outputs.

Run this on desktop to see what each local model answers.
Then take screenshots of the SAME questions in AI Edge Gallery and add them to:
  results/phone/screenshots/  (named Q1_E2B.png, Q1_E4B.png, etc.)

Usage:
  python phone_test.py              # runs all 5 on available local models
  python phone_test.py --save       # also writes results/phone_test.md
"""
import sys
import time
from models.ollama_model import OllamaModel
from data.loader import load_suzuki_corpus, get_context_for_case

PHONE_QUESTIONS = [
    {
        "id": "P1",
        "question": "Mi moto no enciende bien en frío y el motor falla a alta velocidad. ¿Qué reviso primero?",
        "category": "diagnostic",
        "why": "Tests basic cold-start / misfire diagnosis — very common real mechanic question",
        "context_keywords": ["bujía", "electro-erosión", "voltaje", "chispa", "mezcla"],
    },
    {
        "id": "P2",
        "question": "¿Cómo cambio el líquido de frenos de mi moto paso a paso?",
        "category": "procedure",
        "why": "Classic procedure question — tests whether model gives safe numbered steps",
        "context_keywords": ["purgador", "macarrón", "bombear", "maneta", "depósito"],
    },
    {
        "id": "P3",
        "question": "La horquilla delantera de mi moto se hunde mucho cuando freno fuerte. ¿Qué hago?",
        "category": "diagnostic",
        "why": "Multi-cause diagnostic — tests depth of suspension knowledge",
        "context_keywords": ["horquilla", "resortes", "sag", "balance", "compresión"],
    },
    {
        "id": "P4",
        "question": "¿Cada cuánto debo cambiar las bujías y qué tipo necesito para mi moto?",
        "category": "maintenance",
        "why": "Simple spec/maintenance question — tests knowledge of intervals and heat range",
        "context_keywords": ["10,000 km", "cobre", "platino", "rango térmico", "electrodo"],
    },
    {
        "id": "P5",
        "question": "Después de cambiar el aceite, noté que la moto vibra más de lo normal. ¿Puede ser el aceite incorrecto?",
        "category": "diagnostic",
        "why": "Edge case — tests if model can reason about oil viscosity effects on engine behavior",
        "context_keywords": ["aceite", "viscosidad", "SAE", "motor", "vibración"],
    },
]

LOCAL_MODELS = [
    OllamaModel("gemma2:2b",    "Gemma E2B (2B)"),
    OllamaModel("gemma4:latest","Gemma E4B (8B)"),
]


def run_phone_test(save: bool = False) -> list[dict]:
    corpus = load_suzuki_corpus()
    results = []

    print("=" * 70)
    print("PHONE TEST — 5 Key Questions")
    print("Compare these outputs with your AI Edge Gallery screenshots")
    print("=" * 70)

    for q in PHONE_QUESTIONS:
        print(f"\n{'─'*70}")
        print(f"[{q['id']}] {q['question']}")
        print(f"Category: {q['category']} | Why: {q['why']}")
        print()

        # Build a minimal context from AKT manual
        fake_case = {"source_manual": "akt", "context_keywords": q["context_keywords"]}
        context = get_context_for_case(fake_case, corpus, max_chars=1000)

        entry = {"id": q["id"], "question": q["question"], "responses": {}}
        for model in LOCAL_MODELS:
            if not model.is_available():
                print(f"  [{model.display_name}] — not available, skipping")
                continue
            print(f"  ▶ {model.display_name}:", end=" ", flush=True)
            t0 = time.time()
            try:
                resp = model.query(q["question"], context,
                                   "Eres un mecánico experto. Responde de forma práctica y concisa.")
                elapsed = round(time.time() - t0, 1)
                print(f"({elapsed}s)")
                print(f"\n{resp}\n")
                entry["responses"][model.display_name] = {"response": resp, "latency_s": elapsed}
            except Exception as e:
                print(f"ERROR: {e}")
                entry["responses"][model.display_name] = {"response": f"ERROR: {e}", "latency_s": 0}
        results.append(entry)

    if save:
        _save_markdown(results)

    print("\n" + "=" * 70)
    print("📱 Now test the same questions in AI Edge Gallery on your phone")
    print("   Save screenshots as: results/phone/Q1_E2B.png, Q1_E4B.png, etc.")
    print("=" * 70)
    return results


def _save_markdown(results: list[dict]):
    import os
    os.makedirs("results/phone", exist_ok=True)
    lines = [
        "# Phone Test Results — AI Edge Gallery vs Desktop Ollama",
        "",
        "> Run on desktop: `python phone_test.py --save`  ",
        "> Phone screenshots go in `results/phone/screenshots/`",
        "",
    ]
    for entry in results:
        q_obj = next(q for q in PHONE_QUESTIONS if q["id"] == entry["id"])
        lines += [
            f"## {entry['id']} — {q_obj['category'].capitalize()}",
            "",
            f"**Question:** {entry['question']}",
            f"**Why this question:** {q_obj['why']}",
            "",
        ]
        for model_name, data in entry["responses"].items():
            lines += [
                f"### {model_name} ({data.get('latency_s', '?')}s)",
                "",
                data["response"],
                "",
            ]

        # Phone screenshot placeholders
        lines += [
            "### 📱 Phone Screenshots (AI Edge Gallery)",
            "",
            f"| E2B on Phone | E4B on Phone |",
            f"|---|---|",
            f"| ![{entry['id']}_E2B](screenshots/{entry['id']}_E2B.png) | "
            f"![{entry['id']}_E4B](screenshots/{entry['id']}_E4B.png) |",
            "",
            "---",
            "",
        ]

    path = "results/phone/phone_test.md"
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"\nPhone test report saved to {path}")


if __name__ == "__main__":
    save = "--save" in sys.argv
    run_phone_test(save=save)
