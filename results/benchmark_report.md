# Metrics Monkey — Benchmark Results

**Run date:** 2026-05-18  
**Models tested:** Gemma 9B (local)  
**Test cases:** 5  
**Context (RAG):** yes  
**LLM judge:** no  

---

## Overall Scores

| Model | Composite ↑ | KW Coverage ↑ | ROUGE-L ↑ | Length ↑ | Avg Latency |
|---|---|---|---|---|---|
| Gemma 9B (local) | **0.718** | 0.651 | 0.468 | 0.800 | 108.9s |

---

## Scores by Difficulty

| Model | Easy | Medium | Hard |
|---|---|---|---|
| Gemma 9B (local) | 0.738 | 0.642 | — |

---

## Scores by Category

| Model | Diagnostic | Safety | Specificat |
|---|---|---|---|
| Gemma 9B (local) | 0.642 | 0.615 | 0.778 |

---

## Fine-tuned Model Placeholder

> The following row will be filled once the fine-tuned Gemma 2B model is available.

| Model | Composite ↑ | KW Coverage ↑ | ROUGE-L ↑ | Length ↑ | Avg Latency |
|---|---|---|---|---|---|
| Gemma 2B Fine-tuned | _TBD_ | _TBD_ | _TBD_ | _TBD_ | _TBD_ |

---

## Metric Definitions

| Metric | Description | Weight |
|---|---|---|
| **Composite** | Weighted average of all metrics below | — |
| **KW Coverage** | Fraction of expected domain keywords present in response | 30% |
| **ROUGE-L** | F1 score of Longest Common Subsequence vs ground-truth excerpt | 25% |
| **Length Score** | Penalises too-short (<30 words) or too-long (>500 words) responses | 10% |
| **Safety Compliance** | For safety-category questions: presence of safety language | 10% |
| **LLM Judge** | GPT-4o-mini scores accuracy/completeness/hallucination (0–10 → 0–1) | 25% |

> Note: LLM judge weight is redistributed proportionally when no API key is configured.

---

## References

- Gemma 4 model family: https://huggingface.co/google/gemma-4-E4B-it
- Open LLM Leaderboard: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard
- ROUGE metric: Lin, C.-Y. (2004). ROUGE: A Package for Automatic Evaluation of Summaries. ACL Workshop.
- LLM-as-judge: Zheng et al. (2023). Judging LLM-as-a-Judge with MT-Bench. NeurIPS.
- RAG benchmark methodology: Es et al. (2023). RAGAS: Automated Evaluation of RAG Pipelines. EACL.