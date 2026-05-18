# Metrics Monkey — Benchmark Results

**Run date:** 2026-05-18  
**Models tested:** Gemma E2B (2B local), GPT-4o, Mistral Large, Qwen 2.5 72B, Claude Sonnet  
**Test cases:** 25  
**Context (RAG):** yes  
**LLM judge:** yes  

---

## Overall Scores

| Model | Composite ↑ | KW Coverage ↑ | ROUGE-L ↑ | Length ↑ | Avg Latency |
|---|---|---|---|---|---|
| Claude Sonnet | **0.806** | 0.909 | 0.239 | 1.000 | 8.4s |
| GPT-4o | **0.781** | 0.817 | 0.254 | 0.985 | 5.2s |
| Qwen 2.5 72B | **0.769** | 0.781 | 0.190 | 0.987 | 24.1s |
| Gemma E2B (2B local) | **0.731** | 0.652 | 0.249 | 0.968 | 53.5s |
| Mistral Large | **0.703** | 0.812 | 0.115 | 0.878 | 18.7s |

---

## Scores by Difficulty

| Model | Easy | Medium | Hard |
|---|---|---|---|
| Claude Sonnet | 0.793 | 0.803 | 0.841 |
| GPT-4o | 0.768 | 0.792 | 0.771 |
| Qwen 2.5 72B | 0.753 | 0.804 | 0.709 |
| Gemma E2B (2B local) | 0.74 | 0.746 | 0.663 |
| Mistral Large | 0.693 | 0.7 | 0.73 |

---

## Scores by Category

| Model | Diagnostic | Maintenanc | Procedure | Safety | Specificat |
|---|---|---|---|---|---|
| Claude Sonnet | 0.796 | 0.83 | 0.824 | 0.784 | 0.806 |
| GPT-4o | 0.781 | 0.772 | 0.793 | 0.752 | 0.798 |
| Qwen 2.5 72B | 0.786 | 0.753 | 0.756 | 0.759 | 0.785 |
| Gemma E2B (2B local) | 0.687 | 0.778 | 0.757 | 0.696 | 0.774 |
| Mistral Large | 0.713 | 0.673 | 0.688 | 0.764 | 0.669 |

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