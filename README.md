# Metrics Monkey 🏍️

**Motorcycle Repair AI Benchmark** — Hackathon Gemma G4

Evaluates how well small/local LLMs (especially Gemma 2B, 4B, and fine-tuned variants) answer real motorcycle repair questions from workshop manuals, compared to SOTA cloud models.

---

## Why this exists

The project trains a fine-tuned Gemma model on motorcycle workshop manuals so mechanics can access repair guides **offline** on low-resource hardware. This benchmark measures whether the fine-tuned model actually improves over the base Gemma, and how it stacks up against ChatGPT, Mistral, and Qwen.

---

## Benchmark design

25 test cases across 5 categories and 3 difficulty levels, sourced from real workshop manuals (AKT, Suzuki, Yamaha, BMW, Honda, KTM). Each case includes:
- A natural-language repair question (Spanish & English)
- Ground-truth excerpt from the manual
- Expected domain keywords
- A scoring rubric

### Scoring metrics (weighted composite)

| Metric | What it measures | Weight |
|---|---|---|
| Keyword Coverage | Domain-specific terms present in response | 30% |
| ROUGE-L | Lexical overlap with ground-truth excerpt | 25% |
| LLM Judge | GPT-4o-mini rates accuracy, completeness, safety (0–10) | 25% |
| Safety Compliance | Safety language for safety-category questions | 10% |
| Length Score | Penalises non-answers (<30 words) or padding (>500 words) | 10% |

---

## Models tested

| Key | Model | Type |
|---|---|---|
| `gemma_2b` | Gemma 2B (E2B) | Local / Ollama — pull `gemma2:2b` |
| `gemma_4b` | Gemma 4 (E4B proxy) | Local / Ollama — `gemma4:latest` |
| `gemma_2b_finetuned` | Gemma 2B Fine-tuned | Local — set model ID when ready |
| `gpt4o` | GPT-4o | OpenRouter |
| `mistral_large` | Mistral Large | OpenRouter |
| `qwen_72b` | Qwen 2.5 72B | OpenRouter |

Add more models in `config.py → MODELS`.

---

## Quick start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Copy and fill environment variables
cp .env.example .env
# Edit .env with your OpenRouter key

# 3. Make sure Ollama is running with at least one Gemma model
ollama pull gemma4:latest   # or gemma2:2b

# 4. Run benchmark (local models only, quick 5-case smoke test)
python run_benchmark.py --models gemma_9b --quick --report

# 5. Full run with cloud models and LLM judge
python run_benchmark.py --judge --report --markdown

# 6. Generate report from existing results file
python -m results.report results/benchmark_YYYYMMDD_HHMMSS.json --markdown results/report.md
```

---

## Plugging in the fine-tuned model

When the fine-tuned Gemma 2B is ready:

1. Push it to Ollama:
   ```bash
   ollama create gemma2b-moto -f Modelfile
   ```
2. Update `config.py`:
   ```python
   "gemma_2b_finetuned": {
       "type": "ollama",
       "model_id": "gemma2b-moto:latest",
       "display": "Gemma 2B Fine-tuned",
   }
   ```
3. Run:
   ```bash
   python run_benchmark.py --models gemma_2b,gemma_2b_finetuned,gpt4o --report --markdown
   ```

---

## Project structure

```
Metrics-Monkey/
├── config.py               # Model registry + API keys + prompts
├── run_benchmark.py        # CLI entry point
├── requirements.txt
├── data/
│   ├── loader.py           # RAG context retrieval from manuals
│   └── test_cases.json     # 25 curated benchmark questions
├── models/
│   ├── base.py             # Abstract model interface
│   ├── ollama_model.py     # Local models via Ollama
│   └── openrouter_model.py # Cloud models via OpenRouter
├── benchmark/
│   ├── metrics.py          # ROUGE-L, keyword coverage, LLM judge
│   └── evaluator.py        # Orchestrates the run
└── results/
    └── report.py           # Generates Markdown + terminal tables
```

---

## Adding manual data

The benchmark uses:
- `suzuki_dataset_v3.csv` — 16,402 Suzuki manual chunks (context for Suzuki questions)
- `[TM]_akt_manual_de_taller_akt_ak_2020.md` — AKT manual (context for AKT questions)

To add more brands, place `.md` files in the project root and update `data/loader.py → get_context_for_case()` to route new `source_manual` prefixes.

---

## References

- Gemma 4 model family: https://huggingface.co/google/gemma-4-E4B-it
- Open LLM Leaderboard: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard
- ROUGE: Lin, C.-Y. (2004). ACL Workshop on Text Summarization.
- LLM-as-judge: Zheng et al. (2023). MT-Bench. NeurIPS.
- RAGAS (RAG evaluation): Es et al. (2023). EACL.
