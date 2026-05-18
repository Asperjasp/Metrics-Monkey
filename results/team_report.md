# Metrics Monkey — Team Report
> Generated 2026-05-18 12:29

---

## 1. Executive Summary

| Model | Composite | Keyword Coverage | Rouge L | Spec Recall | Step Completeness | Hallucination Risk |
|---|---|---|---|---|---|---|
| **Gemma 9B (local)** | 🟡 0.718 | 🟡 0.651 | 🔴 0.468 | 🟡 0.700 | 🟢 1.000 | 🟢 1.000 |

> 🟢 ≥ 0.80 · 🟡 0.60–0.79 · 🔴 < 0.60

---

## 2. Finetuning Impact Assessment

The table below shows the **minimum composite score the finetuned model must reach** to
demonstrate meaningful improvement over the base model on each difficulty tier.

| Difficulty | Baseline | Target (baseline + 0.10) | Pass bar |
|---|---|---|---|
| Easy | 0.738 | **0.838** | 🟢 |
| Medium | 0.642 | **0.742** | 🟡 |
| Hard | 0.000 | **0.100** | 🔴 |

---

## 3. Weakest Test Cases (Finetuning Priorities)

These are the questions where the baseline model scored **below 0.60**.
The finetuned model should be evaluated on these first.

| ID | Question | Category | Diff | Score | Model |
|---|---|---|---|---|---|

---

## 4. Full Question-by-Question Results

Every test case with question, ground truth, and per-model responses.

### TC001 · specification · easy · `es`

**Question:** ¿Cuáles son las dos funciones principales de la bujía en un motor de motocicleta?

**Ground truth:** Las dos funciones principales de la bujía son: 1) Encender la mezcla de aire-combustible transmitiendo energía eléctrica de la bobina para producir una chispa de alto voltaje. 2) Remover el calor de la cámara de combustión, trabajando como intercambiador de calor hacia el sistema de enfriamiento.

<details><summary>🤖 <b>Gemma 9B (local)</b> — composite=0.838 · kw=0.71 · rouge=0.64 · spec=1.00 · halluc_risk=1.00</summary>

**Las dos funciones principales de la bujía en un motor de motocicleta son:**

1. Encender la mezcla de aire-combustible.
2. Remover el calor de la cámara de combustión.

</details>

---

### TC002 · specification · easy · `es`

**Question:** ¿Cada cuántos kilómetros se deben cambiar las bujías de cobre de un solo electrodo en una motocicleta?

**Ground truth:** Las bujías de cobre con un electrodo se cambian cada 10,000 km. Las de cobre con varios electrodos pueden durar hasta 20,000 km por electrodo.

<details><summary>🤖 <b>Gemma 9B (local)</b> — composite=0.742 · kw=0.80 · rouge=0.60 · spec=0.50 · halluc_risk=1.00</summary>

Las bujías de cobre de un solo electrodo se cambian cada **10,000 km**.

</details>

---

### TC007 · diagnostic · medium · `es`

**Question:** La horquilla delantera de la moto se hunde demasiado durante los frenajes. ¿Cuáles son las causas y soluciones posibles?

**Ground truth:** Causas y soluciones: 1) Horquilla muy blanda: endurecer la horquilla, agregar 5mm de aceite o conseguir resortes más duros. 2) Sag del amortiguador trasero muy alto con compresión muy dura: aflojarlo para conseguir balance. Si continúa, ajustar de forma más progresiva.

<details><summary>🤖 <b>Gemma 9B (local)</b> — composite=0.642 · kw=0.86 · rouge=0.32 · spec=0.00 · halluc_risk=1.00</summary>

**Causas:**

* Horquilla demasiado blanda.
* Amortificador demasiado suave o con demasiado sag.

**Soluciones:**

* Endurecer la horquilla delantera.
* Utilizar resortes más duros.
* Ablandar la compresión de la horquilla delantera.
* Endurecer el amortiguador trasero.
* Aumentar la altura de la moto atrás (menos sag).

</details>

---

### TC012 · specification · easy · `en`

**Question:** What is the specified torque for the final gearbox cover bolts on a Suzuki Burgman UH125?

**Ground truth:** The final gear box cover bolts must be tightened in ascending order of the numbered sequence to a torque of 22 N·m (2.2 kgf-m).

<details><summary>🤖 <b>Gemma 9B (local)</b> — composite=0.755 · kw=0.60 · rouge=0.49 · spec=1.00 · halluc_risk=1.00</summary>

The specified torque for the final gearbox cover bolts on a Suzuki Burgman UH125 is **22 N·m (2.2 kgf-m)**.

</details>

---

### TC016 · safety · easy · `en`

**Question:** What safety precautions must be followed when running a motorcycle engine indoors during service work?

**Ground truth:** When running the engine indoors, make sure that exhaust gas is forced outdoors. When working with toxic or flammable materials, ensure the work area is well-ventilated and follow all manufacturer's instructions. Never use gasoline as a cleaning solvent.

<details><summary>🤖 <b>Gemma 9B (local)</b> — composite=0.615 · kw=0.29 · rouge=0.29 · spec=1.00 · halluc_risk=1.00</summary>

The provided text states that when running a motorcycle engine indoors during service work, **exhaust gas must be forced outdoors** to ensure proper ventilation and prevent exposure to harmful fumes.

</details>

---

## 5. Recommendations for Finetuning Pipeline

Based on the metric breakdown, here are the highest-leverage improvements:

1. Baseline scores are solid across all metrics — focus on spec recall and hard cases.


---

## 6. How to Run the Benchmark on the Fine-tuned Model

```bash
# 1. Register the fine-tuned model in Ollama
ollama create gemma2b-moto -f Modelfile

# 2. Update config.py  →  gemma_2b_finetuned  →  model_id = 'gemma2b-moto:latest'

# 3. Run comparison (base vs finetuned vs SOTA)
python run_benchmark.py \
  --models gemma_9b,gemma_2b_finetuned,gpt4o \
  --report --markdown

# 4. Generate figures
python -m results.visualize results/benchmark_YYYYMMDD_HHMMSS.json

# 5. Build team report
python -m results.team_report results/benchmark_YYYYMMDD_HHMMSS.json --out team_report.md
```

---

_Report generated by Metrics Monkey — Hackathon Gemma G4_