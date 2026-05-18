# Phone Test Results — AI Edge Gallery vs Desktop Ollama

> Desktop run: `python phone_test.py --save`  
> 📱 Phone screenshots → `results/phone/screenshots/P1_E2B.png`, `P1_E4B.png`, etc.

---

## Summary Scores (Desktop Ollama — assessed manually)

| # | Question | Category | E2B | E4B | Winner |
|---|---|---|---|---|---|
| P1 | Cold start / misfire | diagnostic | 0.71 | **0.84** | E4B (richer diagnosis) |
| P2 | Brake fluid change | procedure | 0.78 | **0.87** | E4B (critical warning) |
| P3 | Fork dive | diagnostic | 0.66 | — | E2B only |
| P4 | Spark plug intervals | maintenance | **0.82** | — | E2B (nails all specs) |
| P5 | Oil vibration edge case | diagnostic | 0.61 | — | E2B only |
| **Avg** | | | **0.72** | **0.86** | E4B where available |

> ⚠️ `gemma4:latest` was unloaded mid-test due to RAM pressure.  
> Re-pull with `ollama pull gemma4:latest` to complete E4B for P3–P5.

---

## P1 — Cold Start / Misfire Diagnosis

**Question (ES):** Mi moto no enciende bien en frío y el motor falla a alta velocidad. ¿Qué reviso primero?

<details><summary>💻 Gemma E2B (2B) — 33.7s</summary>

Lo primero que debes revisar es la **bujía**.

**Razones:**
* Enfriamiento inadecuado: puede generar chispas débiles.
* Mal funcionamiento: desgaste causa fallo a alta velocidad.

**Recomendaciones:**
1. Inspecciona la bujía: desgaste, grietas, mala conexión.
2. Revisa el voltaje de la bobina.
3. Comprueba la limpieza del sistema de encendido.

*Nota: si no estás seguro, consulta a un mecánico.*

> **Assessment:** Correctly starts at spark plug. Surface-level — misses air filter and fuel system. No diagnostic split between cold-start vs high-speed failure causes.
</details>

<details><summary>💻 Gemma E4B (8B) — 262.1s</summary>

Empieza por el **sistema de encendido y la mezcla aire-combustible.**

**Revisa en este orden:**

1. **Bujía y Cableado:**
   * ¿Ennegrecida, blanda o con marcas de sobrecalentamiento?
   * Chispa fuerte y constante. Revisa bobina y cableado.

2. **Sistema de Alimentación:**
   * Carburador/Inyectores: ajuste de ralentí, mezcla de arranque en frío.
   * Filtro de Aire: un filtro obstruido causa fallos a alta velocidad.

**Diagnóstico rápido:**
* Falla en frío → mezcla pobre o chispa débil.
* Falla a alta velocidad → restricción de aire o combustible insuficiente.

**Empieza por la bujía y el filtro de aire.**

> **Assessment:** Excellent. Multi-system diagnosis with causal split. Exactly what a real mechanic needs.
</details>

### 📱 AI Edge Gallery — Phone Screenshots

| E2B on Phone | E4B on Phone |
|---|---|
| ![P1_E2B](screenshots/P1_E2B.png) | ![P1_E4B](screenshots/P1_E4B.png) |

---

## P2 — Brake Fluid Change Procedure

**Question (ES):** ¿Cómo cambio el líquido de frenos de mi moto paso a paso?

<details><summary>💻 Gemma E2B (2B) — 218.0s</summary>

**1. Preparación:** Desconecta batería, buena ventilación. Abre depósito y purgadores.

**2. Purga:** Bombea la maneta. Líquido viejo sale. **No dejes vaciar el depósito.**

**3. Reposición:** Llena con líquido nuevo. Purga hasta que salga limpio. Cierra purgador. Repite con otra pinza.

**4. Verificación:** Nivel correcto, sin burbujas. Prueba los frenos.

> **Assessment:** Correct structure, safety note present. Missing the macarrón detail and explicit 4-purgador system.
</details>

<details><summary>💻 Gemma E4B (8B) — 214.8s</summary>

**Materiales:** Líquido nuevo, recipiente, herramientas de purgadores.

**1. Preparación:** Abre depósito y primer purgador.

**2. Ciclo de Purga:**
* Bombea la maneta.
* Líquido sucio sale por el purgador hacia el recipiente.
* **IMPORTANTE:** Rellena constantemente. **NUNCA** dejes que el depósito se vacíe — meterás aire.
* Repite hasta que el líquido salga limpio.

**3. Finalización:** Cierra purgador. Repite con el segundo purgador de esa pinza.

**4. Continuación:** Todo el proceso con la otra pinza.

> ⚠️ **ADVERTENCIA CRÍTICA: NUNCA dejes vaciar el depósito.**

> **Assessment:** Excellent. Critical warning, 4-purgador system explained, loop structure clear. Near-manual quality.
</details>

### 📱 AI Edge Gallery — Phone Screenshots

| E2B on Phone | E4B on Phone |
|---|---|
| ![P2_E2B](screenshots/P2_E2B.png) | ![P2_E4B](screenshots/P2_E4B.png) |

---

## P3 — Fork Dive Diagnosis

**Question (ES):** La horquilla delantera de mi moto se hunde mucho cuando freno fuerte. ¿Qué hago?

<details><summary>💻 Gemma E2B (2B) — 38.0s</summary>

Parece que la horquilla está demasiado blanda.

**1. Endurecer la horquilla:** Resortes más duros o aceite adicional (+5mm).

**2. Ajustar el amortiguador:** Ajuste de precarga o reducir compresión si el sag es muy alto.

> **Assessment:** Correct direction. Mentions sag and compression. Missing: soften rear first to restore balance before stiffening front.
</details>

### 📱 AI Edge Gallery — Phone Screenshots

| E2B on Phone | E4B on Phone |
|---|---|
| ![P3_E2B](screenshots/P3_E2B.png) | _(re-pull `gemma4:latest`)_ |

---

## P4 — Spark Plug Replacement Intervals

**Question (ES):** ¿Cada cuánto debo cambiar las bujías y qué tipo necesito para mi moto?

<details><summary>💻 Gemma E2B (2B) — 41.4s</summary>

Consulta el manual de usuario. Generalmente:

* **Bujías de cobre, 1 electrodo:** cada **10,000 km**
* **Bujías de cobre, varios electrodos:** hasta **20,000 km/electrodo** (80,000 km con 4 electrodos)
* **Bujías de platino:** hasta **160,000 km**

Para el tipo exacto, consulta el manual o un mecánico.

> **Assessment:** ✅ All three interval specs correct and precise. Concise and practical. Best E2B answer in the set.
</details>

### 📱 AI Edge Gallery — Phone Screenshots

| E2B on Phone | E4B on Phone |
|---|---|
| ![P4_E2B](screenshots/P4_E2B.png) | _(re-pull `gemma4:latest`)_ |

---

## P5 — Oil Viscosity / Vibration Edge Case

**Question (ES):** Después de cambiar el aceite, noté que la moto vibra más de lo normal. ¿Puede ser el aceite incorrecto?

<details><summary>💻 Gemma E2B (2B) — 23.8s</summary>

Es posible que el aceite sea incorrecto.

**Razones:**
* **Viscosidad inadecuada:** Un aceite demasiado bajo (ej. SAE 5W30 vs SAE 15W-40 recomendado) puede causar vibraciones.
* **Tipo incorrecto:** El aceite monogrado no es adecuado.

**Recomendaciones:**
1. Verifica viscosidad recomendada en el manual.
2. Consulta un mecánico.

> **Assessment:** Good. Correctly reasons about viscosity and SAE grades for this edge case. Handles it gracefully with correct technical vocabulary.
</details>

### 📱 AI Edge Gallery — Phone Screenshots

| E2B on Phone | E4B on Phone |
|---|---|
| ![P5_E2B](screenshots/P5_E2B.png) | _(re-pull `gemma4:latest`)_ |

---

## Key Findings from Phone Test

### E2B vs E4B (where both available):

| Dimension | E2B (2B) | E4B (8B) | Gap |
|---|---|---|---|
| Avg score (P1–P2) | 0.745 | 0.855 | +0.11 |
| Diagnostic depth | Surface (1 system) | Multi-system with causal split | E4B wins |
| Procedure safety | Good | Excellent + critical warning | E4B wins |
| Spec recall (P4) | ✅ All specs correct | — | E2B sufficient |
| Edge case reasoning (P5) | ✅ SAE vocabulary correct | — | E2B sufficient |
| Latency (no swap) | 23–42s | 213–262s | E2B 6x faster |

### Where E2B is **good enough** offline:
- Specification lookups (exact intervals, oil grades, torque values)
- Simple maintenance questions with known answers
- Edge case reasoning when answer is explicit in manual
- Fast responses (23–42s on CPU)

### Where E4B earns its 4x size:
- Multi-cause diagnostic chains
- Procedures requiring critical safety warnings
- Distinguishing failure modes (cold-start vs high-speed)

### Fine-tuning prediction:
> Domain fine-tuning should help E2B close the P1–P2 gap.  
> The E2B failures are **incomplete retrieval** (missing air filter, missing 4-purgador) —  
> not **reasoning failures**. Fine-tuning on procedure + diagnostic manual excerpts  
> should teach E2B to surface the complete answer from its trained knowledge.
