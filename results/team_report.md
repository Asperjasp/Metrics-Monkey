# Metrics Monkey — Team Report
> Generated 2026-05-18 13:35

---

## 1. Executive Summary

| Model | Composite | Keyword Coverage | Rouge L | Spec Recall | Step Completeness | Hallucination Risk |
|---|---|---|---|---|---|---|
| **Gemma E2B (2B local)** | 🟡 0.731 | 🟡 0.652 | 🔴 0.249 | 🟢 0.900 | 🟢 1.000 | 🟢 1.000 |
| **GPT-4o** | 🟡 0.781 | 🟢 0.817 | 🔴 0.254 | 🟢 0.940 | 🟢 0.972 | 🟢 1.000 |
| **Mistral Large** | 🟡 0.703 | 🟢 0.812 | 🔴 0.115 | 🟢 0.940 | 🟢 1.000 | 🔴 0.488 |
| **Qwen 2.5 72B** | 🟡 0.769 | 🟡 0.781 | 🔴 0.190 | 🟢 0.975 | 🟢 1.000 | 🟢 1.000 |
| **Claude Sonnet** | 🟢 0.806 | 🟢 0.909 | 🔴 0.239 | 🟢 0.940 | 🟢 1.000 | 🟢 1.000 |

> 🟢 ≥ 0.80 · 🟡 0.60–0.79 · 🔴 < 0.60

---

## 2. Finetuning Impact Assessment

The table below shows the **minimum composite score the finetuned model must reach** to
demonstrate meaningful improvement over the base model on each difficulty tier.

| Difficulty | Baseline | Target (baseline + 0.10) | Pass bar |
|---|---|---|---|
| Easy | 0.740 | **0.840** | 🟢 |
| Medium | 0.746 | **0.846** | 🟢 |
| Hard | 0.663 | **0.763** | 🟡 |

---

## 3. Weakest Test Cases (Finetuning Priorities)

These are the questions where the baseline model scored **below 0.60**.
The finetuned model should be evaluated on these first.

| ID | Question | Category | Diff | Score | Model |
|---|---|---|---|---|---|
| TC009 | En una motocicleta de motocross, la parte trasera tiende a adelantar a… | diagnostic | medium | 0.513 | Claude Sonnet |
| TC009 | En una motocicleta de motocross, la parte trasera tiende a adelantar a… | diagnostic | medium | 0.521 | GPT-4o |
| TC020 | En una motocicleta de enduro, ¿por qué podría ser necesario ajustar di… | diagnostic | hard | 0.549 | Gemma E2B (2B local) |
| TC012 | What is the specified torque for the final gearbox cover bolts on a Su… | specification | easy | 0.550 | Mistral Large |
| TC024 | Cuando se cambia la puesta a punto de suspensión entre la primera y se… | procedure | hard | 0.597 | Mistral Large |

---

## 4. Full Question-by-Question Results

Every test case with question, ground truth, and per-model responses.

### TC001 · specification · easy · `es`

**Question:** ¿Cuáles son las dos funciones principales de la bujía en un motor de motocicleta?

**Ground truth:** Las dos funciones principales de la bujía son: 1) Encender la mezcla de aire-combustible transmitiendo energía eléctrica de la bobina para producir una chispa de alto voltaje. 2) Remover el calor de la cámara de combustión, trabajando como intercambiador de calor hacia el sistema de enfriamiento.

<details><summary>🤖 <b>Gemma E2B (2B local)</b> — composite=0.795 · kw=0.71 · rouge=0.36 · spec=1.00 · halluc_risk=1.00</summary>

Las dos funciones principales de la bujía en un motor de motocicleta son:

1. **Ignición:** La bujía recibe energía eléctrica de la bobina y produce una chispa de alto voltaje que enciende la mezcla de combustible y aire comprimida dentro de cada cilindro, iniciando el proceso de combustión.
2. **Disipación de calor:** La bujía actúa como un intercambiador de calor, extrayendo la energía calorífica no deseada en la cámara de combustión al sistema de enfriamiento del motor. 


**Advertencia:** Es importante recordar que la bujía es un componente crucial y delicado. Cualquier daño o mal funciona…

</details>

<details><summary>🤖 <b>GPT-4o</b> — composite=0.878 · kw=1.00 · rouge=0.50 · spec=1.00 · halluc_risk=1.00</summary>

Las dos funciones principales de la bujía en un motor de motocicleta son:

1. **Encender la mezcla de aire-combustible**: La bujía es el componente final en el circuito de ignición. Recibe una carga de voltaje de la bobina y produce una chispa de alto voltaje que enciende la mezcla comprimida de combustible y aire dentro de cada cilindro, transformando el combustible en energía de trabajo.

2. **Remover el calor de la cámara de combustión**: La bujía actúa como un intercambiador de calor, extrayendo el calor no deseado de la cámara de combustión y transfiriéndolo al sistema de enfriamiento del…

</details>

<details><summary>🤖 <b>Mistral Large</b> — composite=0.833 · kw=1.00 · rouge=0.21 · spec=1.00 · halluc_risk=1.00</summary>

Según el contexto del manual de taller proporcionado, las **dos funciones principales de la bujía en un motor de motocicleta** son:

1. **Encender la mezcla aire-combustible**:
   - La bujía recibe alto voltaje de la bobina de encendido y genera una chispa eléctrica que inflama la mezcla comprimida dentro del cilindro, iniciando la combustión y transformando la energía química del combustible en energía mecánica (movimiento del pistón).

2. **Disipar el calor de la cámara de combustión**:
   - Actúa como un **intercambiador de calor**, extrayendo el exceso de temperatura generado durante la co…

</details>

<details><summary>🤖 <b>Qwen 2.5 72B</b> — composite=0.866 · kw=1.00 · rouge=0.36 · spec=1.00 · halluc_risk=1.00</summary>

Las dos funciones principales de la bujía en un motor de motocicleta son:

1. **Encender la mezcla de aire-combustible**: La bujía es el último componente en el circuito de ignición. Su función es transmitir la energía eléctrica de la bobina y producir una chispa de alto voltaje que enciende la mezcla de aire y combustible comprimida dentro del cilindro. Esta chispa es crucial para iniciar la combustión y generar la energía necesaria para el funcionamiento del motor.

2. **Remover el calor de la cámara de combustión**: La bujía actúa como un intercambiador de calor, extrayendo el exceso de cal…

</details>

<details><summary>🤖 <b>Claude Sonnet</b> — composite=0.855 · kw=1.00 · rouge=0.39 · spec=1.00 · halluc_risk=1.00</summary>

Según el manual de taller, las **dos funciones principales de la bujía** son:

## 1. **Encender la mezcla de aire-combustible**
La bujía actúa como el último paso en el circuito de ignición. Recibe carga de alto voltaje de la bobina y produce una chispa eléctrica que enciende la mezcla comprimida de aire y combustible dentro del cilindro, transformando el combustible en energía de trabajo.

## 2. **Remover el calor de la cámara de combustión**
La bujía funciona como un intercambiador de calor, extrayendo la energía calorífica no deseada de la cámara de combustión hacia el sistema de enfriamien…

</details>

---

### TC002 · specification · easy · `es`

**Question:** ¿Cada cuántos kilómetros se deben cambiar las bujías de cobre de un solo electrodo en una motocicleta?

**Ground truth:** Las bujías de cobre con un electrodo se cambian cada 10,000 km. Las de cobre con varios electrodos pueden durar hasta 20,000 km por electrodo.

<details><summary>🤖 <b>Gemma E2B (2B local)</b> — composite=0.750 · kw=0.80 · rouge=0.60 · spec=0.50 · halluc_risk=1.00</summary>

De acuerdo con el manual, las bujías de cobre con un electrodo se cambian cada **10,000 km**.

</details>

<details><summary>🤖 <b>GPT-4o</b> — composite=0.767 · kw=1.00 · rouge=0.24 · spec=0.50 · halluc_risk=1.00</summary>

Las bujías de cobre con un solo electrodo en una motocicleta deben cambiarse cada 10,000 km. Esto asegura que el motor funcione de manera eficiente y evita el desperdicio de combustible debido al desgaste del electrodo que aumenta la distancia de salto de chispa. Recuerda siempre seguir las recomendaciones específicas del fabricante de la motocicleta y utilizar bujías adecuadas según el catálogo del fabricante de bujías. Además, asegúrate de realizar el cambio de bujías con el motor frío para evitar quemaduras y daños en el motor.

</details>

<details><summary>🤖 <b>Mistral Large</b> — composite=0.700 · kw=0.80 · rouge=0.16 · spec=0.50 · halluc_risk=1.00</summary>

Según el contexto del manual de taller proporcionado, **las bujías de cobre con un solo electrodo deben cambiarse cada 10,000 km** en una motocicleta.

### Consideraciones adicionales:
1. **Calidad de la gasolina**: Si el combustible es de mala calidad (con impurezas o bajo octanaje), el desgaste puede acelerarse, reduciendo la vida útil de la bujía.
2. **Condiciones de manejo**: Conducción en ciudad (con paradas frecuentes) o en terrenos polvorientos puede acortar el intervalo.
3. **Síntomas de desgaste**: Si notas fallos de encendido, pérdida de potencia o dificultad para arrancar, revisa la…

</details>

<details><summary>🤖 <b>Qwen 2.5 72B</b> — composite=0.718 · kw=0.80 · rouge=0.26 · spec=0.50 · halluc_risk=1.00</summary>

Según el manual de taller, las bujías de cobre con un solo electrodo deben cambiarse cada 10,000 km.

**Advertencia de seguridad:**
- Asegúrate de que el motor esté frío antes de cambiar las bujías para evitar quemaduras.
- Utiliza una llave de bujías adecuada para evitar dañar la rosca del cilindro.
- Verifica la tensión del cable de la bujía al instalar la nueva para asegurar una conexión segura y evitar problemas de encendido.

</details>

<details><summary>🤖 <b>Claude Sonnet</b> — composite=0.690 · kw=0.80 · rouge=0.20 · spec=0.50 · halluc_risk=1.00</summary>

Según el manual de taller, **las bujías de cobre con un solo electrodo se deben cambiar cada 10,000 km**.

Es importante seguir este intervalo de mantenimiento porque:

- Con el uso, las bujías sufren **electro-erosión** que desgasta el electrodo
- Este desgaste aumenta la distancia de salto de chispa
- La bujía necesitará mayor voltaje para funcionar
- Pueden perderse explosiones en el motor, causando:
  - Desperdicio de combustible
  - Pérdida de potencia
  - Funcionamiento ineficiente del motor

**Nota importante:** Este intervalo puede variar dependiendo de:
- La calidad de la gasolina uti…

</details>

---

### TC003 · diagnostic · medium · `es`

**Question:** ¿Qué problemas causa usar una bujía con un rango térmico incorrecto en una motocicleta?

**Ground truth:** Usar bujías con rango térmico incorrecto reduce considerablemente la eficiencia del motor y la vida de las bujías. Una bujía muy fría en motor frío causa depósitos en el aislante. Una bujía muy caliente en motor de alto desempeño puede causar pre-ignición y destrucción de electrodos.

<details><summary>🤖 <b>Gemma E2B (2B local)</b> — composite=0.675 · kw=0.40 · rouge=0.20 · spec=1.00 · halluc_risk=1.00</summary>

Usar una bujía con un rango térmico incorrecto en una motocicleta puede causar varios problemas, incluyendo: 

**1. Pérdida de eficiencia del motor:**  Un rango térmico incorrecto puede afectar la combustión y el rendimiento del motor. Esto se traduce en una menor potencia, mayor consumo de combustible y menor eficiencia general.
**2. Daño a las bujías:** Las bujías con un rango térmico inadecuado pueden sufrir daños prematuros debido al calor excesivo o insuficiente. 
**3. Problemas de arranque:**  Un rango térmico incorrecto puede dificultar el arranque del motor, especialmente en climas frí…

</details>

<details><summary>🤖 <b>GPT-4o</b> — composite=0.826 · kw=1.00 · rouge=0.19 · spec=1.00 · halluc_risk=1.00</summary>

Usar una bujía con un rango térmico incorrecto en una motocicleta puede causar varios problemas que afectan tanto el rendimiento del motor como su durabilidad. Aquí te detallo los problemas más comunes:

1. **Depósitos de Carbono**: Si utilizas una bujía demasiado caliente en un motor que no lo requiere, puede no disipar adecuadamente el calor, lo que lleva a la acumulación de depósitos de carbono en el extremo del aislante. Esto puede causar fallos en la ignición y reducir la eficiencia del motor.

2. **Pre-ignición y Golpeteo**: Una bujía demasiado fría en un motor de alto rendimiento puede …

</details>

<details><summary>🤖 <b>Mistral Large</b> — composite=0.659 · kw=0.80 · rouge=0.10 · spec=1.00 · halluc_risk=0.00</summary>

Usar una bujía con un **rango térmico incorrecto** en una motocicleta puede causar varios problemas graves, tanto en el rendimiento como en la integridad del motor. Aquí los detalles basados en el contexto del manual y buenas prácticas mecánicas:

---

### **1. Bujía demasiado caliente (para un motor frío o de bajo desempeño)**
**Problemas:**
- **Pre-encendido (detonación):**
  La bujía retiene demasiado calor, lo que puede causar que la mezcla aire-combustible se encienda **antes** de la chispa (por puntos calientes en la cámara). Esto genera:
  - Pérdida de potencia.
  - Daño a pistones, vál…

</details>

<details><summary>🤖 <b>Qwen 2.5 72B</b> — composite=0.767 · kw=0.80 · rouge=0.11 · spec=1.00 · halluc_risk=1.00</summary>

Usar una bujía con un rango térmico incorrecto en una motocicleta puede causar varios problemas, tanto en el rendimiento del motor como en su durabilidad. Aquí te detallo los principales problemas que pueden surgir:

### 1. **Pre-Encendido (Detonación)**
- **Bujías Frías en Motores Calientes:** Si usas una bujía fría en un motor de alto desempeño, el calor generado en la cámara de combustión no se disipará adecuadamente. Esto puede llevar a la formación de puntos calientes en la bujía, causando pre-encendido o detonación. La detonación es una combustión prematura del combustible que puede daña…

</details>

<details><summary>🤖 <b>Claude Sonnet</b> — composite=0.853 · kw=1.00 · rouge=0.28 · spec=1.00 · halluc_risk=1.00</summary>

# Problemas causados por usar una bujía con rango térmico incorrecto

Según el manual, usar bujías con el rango térmico equivocado causa **dos problemas principales**:

## 1. **Reducción considerable de la eficiencia del motor**
- El motor no funcionará a su máximo rendimiento
- Pérdida de potencia
- Consumo inadecuado de combustible
- Arranque difícil

## 2. **Reducción de la vida útil de las bujías**
- Desgaste prematuro
- Necesidad de reemplazo más frecuente

---

## Problemas específicos según el tipo de error:

### **Si usas una bujía MUY CALIENTE** (en un motor de alto desempeño):
- ❌ **…

</details>

---

### TC004 · procedure · medium · `es`

**Question:** Describe el procedimiento paso a paso para cambiar el líquido de frenos de una motocicleta.

**Ground truth:** 1. Colocar macarrón en el purgador, el otro extremo en un recipiente. 2. Abrir el depósito de freno. 3. Abrir un purgador y bombear la maneta para sacar el líquido viejo. 4. Rellenar continuamente con líquido nuevo sin dejar vaciar el depósito. 5. Cuando salga líquido limpio cerrar el purgador y rep…

<details><summary>🤖 <b>Gemma E2B (2B local)</b> — composite=0.780 · kw=0.86 · rouge=0.15 · spec=1.00 · halluc_risk=1.00</summary>

## Procedimiento paso a paso para cambiar el líquido de frenos de una motocicleta:

**1. Preparación:**

* **Abrir el depósito de freno:**  Se debe abrir el depósito de freno del vehículo, como se describe en el manual. 
* **Abrir un purgador:** Se deben abrir los purgadores (o válvulas) que se encuentran en las pinzas de freno. 
* **Bombea la maneta del freno:**  Se debe bombear la maneta del freno para eliminar el líquido viejo y contaminado del circuito. 
* **Observar el nivel del líquido:**  Se debe observar el nivel del líquido de frenos en el depósito, asegurándose que no se quede vacío.…

</details>

<details><summary>🤖 <b>GPT-4o</b> — composite=0.789 · kw=0.86 · rouge=0.17 · spec=1.00 · halluc_risk=1.00</summary>

Para cambiar el líquido de frenos de una motocicleta de manera segura y efectiva, sigue estos pasos detallados:

1. **Preparación:**
   - Asegúrate de tener a mano todo el equipo necesario: líquido de frenos nuevo, una llave adecuada para los purgadores, un macarrón transparente, un recipiente para recoger el líquido viejo, y un embudo si es necesario.
   - Usa guantes y gafas de protección para evitar el contacto con el líquido de frenos, ya que es corrosivo.

2. **Acceso al Depósito de Freno:**
   - Abre el depósito de líquido de frenos de la motocicleta. Ten cuidado de no derramar el líquid…

</details>

<details><summary>🤖 <b>Mistral Large</b> — composite=0.671 · kw=0.86 · rouge=0.10 · spec=1.00 · halluc_risk=0.00</summary>

**Procedimiento paso a paso para cambiar el líquido de frenos en una motocicleta (basado en el manual de taller proporcionado):**

**⚠️ ADVERTENCIAS DE SEGURIDAD PREVIAS:**
1. **Líquido de frenos es corrosivo:** Usa guantes de nitrilo y gafas de protección. Evita el contacto con la piel, pintura o plásticos (puede dañarlos).
2. **Trabaja en un área ventilada:** Los vapores del líquido de frenos son tóxicos.
3. **Nunca reutilices líquido viejo:** Desecha el líquido usado según normativas locales (es residuo peligroso).
4. **No dejes el depósito abierto:** La humedad del aire contamina el líquid…

</details>

<details><summary>🤖 <b>Qwen 2.5 72B</b> — composite=0.782 · kw=0.86 · rouge=0.12 · spec=1.00 · halluc_risk=1.00</summary>

Claro, aquí tienes el procedimiento paso a paso para cambiar el líquido de frenos de una motocicleta, basado en el contexto del manual de taller proporcionado:

### Materiales Necesarios:
- Líquido de frenos nuevo (recomendado por el fabricante)
- Llave para purgadores
- Lata o bote para recoger el líquido viejo
- Tubo de goma o macarrón para la purga
- Guantes y gafas de protección

### Procedimiento:

1. **Preparación:**
   - Asegúrate de que la motocicleta esté apagada y en un lugar bien iluminado y plano.
   - Coloca la motocicleta en el caballete central o lateral para mantenerla estable.…

</details>

<details><summary>🤖 <b>Claude Sonnet</b> — composite=0.791 · kw=0.86 · rouge=0.20 · spec=1.00 · halluc_risk=1.00</summary>

# Procedimiento para Cambiar el Líquido de Frenos de una Motocicleta

## **Preparación:**
1. Localiza el depósito de líquido de frenos
2. Prepara una lata o bote para recoger el líquido usado
3. Consigue líquido de frenos nuevo (verifica el tipo correcto para tu moto)
4. Ten a mano un macarrón/manguera transparente y una llave para los purgadores

---

## **Proceso de Renovación del Líquido:**

### **Paso 1: Vaciado del líquido viejo**
- Abre el depósito de freno
- Conecta el macarrón al purgador y coloca el otro extremo en el bote
- Abre un purgador de la pinza
- Bombea la maneta del freno re…

</details>

---

### TC005 · safety · easy · `es`

**Question:** ¿Por qué el líquido de frenos es peligroso para la carrocería y partes de goma de la motocicleta?

**Ground truth:** El líquido de frenos reacciona químicamente con la pintura, plásticos y materiales de goma, dañándolos severamente. Por eso debe limpiarse inmediatamente si entra en contacto con estas partes.

<details><summary>🤖 <b>Gemma E2B (2B local)</b> — composite=0.601 · kw=0.17 · rouge=0.17 · spec=1.00 · halluc_risk=1.00</summary>

El líquido de frenos no es peligroso para la carrocería y partes de goma de la motocicleta. 

**ADVERTENCIA:**  Es importante recordar que el **líquido de frenos contiene componentes químicos que pueden ser corrosivos**.  Si se contacta con la carrocería o partes de goma, puede causar daños a estas. 

**Recomendaciones:**

* Siempre use guantes de protección al manipular el líquido de frenos.
* Nunca mezcle el líquido de frenos con otros productos químicos sin consultar con un profesional.
* Limpie las superficies donde se haya derramado el líquido de frenos con agua y jabón neutro. 


Si tien…

</details>

<details><summary>🤖 <b>GPT-4o</b> — composite=0.664 · kw=0.33 · rouge=0.18 · spec=1.00 · halluc_risk=1.00</summary>

El líquido de frenos es peligroso para la carrocería y partes de goma de la motocicleta porque es un fluido altamente corrosivo. Si entra en contacto con la pintura de la carrocería, puede causar daños significativos, como decoloración o desprendimiento de la pintura. Además, el líquido de frenos puede deteriorar las partes de goma, como las mangueras y los sellos, provocando que se vuelvan frágiles y se agrieten con el tiempo.

**Advertencia de seguridad:** Siempre maneja el líquido de frenos con cuidado. Usa guantes y asegúrate de limpiar cualquier derrame inmediatamente con un paño limpio y…

</details>

<details><summary>🤖 <b>Mistral Large</b> — composite=0.718 · kw=0.67 · rouge=0.06 · spec=1.00 · halluc_risk=1.00</summary>

El líquido de frenos es peligroso para la carrocería y las partes de goma de la motocicleta debido a sus propiedades químicas y físicas. Aquí te explico con detalle, basado en conocimientos técnicos y advertencias de seguridad estándar en manuales de taller:

### **1. Composición química corrosiva**
El líquido de frenos (generalmente **DOT 3, DOT 4 o DOT 5.1**, a base de glicol) es **higroscópico** (absorbe humedad del ambiente) y contiene aditivos que pueden ser agresivos para:
- **Pinturas y plásticos**: El líquido de frenos actúa como un **disolvente** para muchos tipos de pintura, barnices…

</details>

<details><summary>🤖 <b>Qwen 2.5 72B</b> — composite=0.693 · kw=0.50 · rouge=0.12 · spec=1.00 · halluc_risk=1.00</summary>

El líquido de frenos es peligroso para la carrocería y partes de goma de la motocicleta debido a su composición química. Específicamente:

1. **Daño a la Pintura y la Carrocería**: El líquido de frenos es altamente corrosivo y puede dañar rápidamente la pintura y la superficie de la carrocería de la motocicleta. Si se derrama, puede causar manchas, decoloración y hasta la degradación del material.

2. **Degradación de las Partes de Goma**: El líquido de frenos puede disolver o degradar las partes de goma, como las mangueras, sellos y juntas. Esto puede provocar fugas, pérdida de presión y, en …

</details>

<details><summary>🤖 <b>Claude Sonnet</b> — composite=0.683 · kw=0.50 · rouge=0.11 · spec=1.00 · halluc_risk=1.00</summary>

Basándome en el contexto del manual proporcionado, **no encuentro información específica sobre el líquido de frenos y sus efectos en la carrocería o partes de goma**.

Sin embargo, como mecánico experto puedo informarte que el líquido de frenos es peligroso para estos componentes porque:

1. **Es altamente corrosivo para la pintura** - Puede disolver o dañar permanentemente el acabado de la carrocería
2. **Ataca componentes de goma** - Degrada sellos, mangueras y juntas que no sean específicamente resistentes al líquido de frenos
3. **Actúa rápidamente** - El daño puede ocurrir en minutos

**⚠…

</details>

---

### TC006 · safety · medium · `es`

**Question:** ¿Cuál es el error crítico que no se debe cometer al purgar el circuito de frenos y qué consecuencia tiene?

**Ground truth:** El error crítico es dejar vaciar completamente el depósito de líquido de frenos. Esto hace que entre aire en el circuito, lo cual hace que la maneta se vuelva esponjosa y complica mucho el proceso de purgado posterior.

<details><summary>🤖 <b>Gemma E2B (2B local)</b> — composite=0.658 · kw=0.50 · rouge=0.20 · spec=1.00 · halluc_risk=1.00</summary>

El error crítico que no se debe cometer al purgar el circuito de frenos es **no asegurarse de que el bote con líquido esté lleno** antes de comenzar a bombear. 

Si el bote no está lleno, el aire puede entrar por succión desde el purgador, lo que causará que el circuito quede incompleto y **el proceso de purga sea ineficaz**.  Esto podría llevar a problemas como:

* **Frenos con menor eficacia:** El aire atrapado en el circuito puede afectar la presión del líquido de frenos, causando que los frenos funcionen con menos eficiencia.
* **Pérdida de control:** Un circuito incompleto puede provocar …

</details>

<details><summary>🤖 <b>GPT-4o</b> — composite=0.793 · kw=0.83 · rouge=0.31 · spec=1.00 · halluc_risk=1.00</summary>

El error crítico que no se debe cometer al purgar el circuito de frenos es permitir que el depósito del líquido de frenos se vacíe completamente. Si esto ocurre, el circuito puede aspirar aire, lo que complicaría el proceso de purgado y podría afectar negativamente el rendimiento del sistema de frenos. La presencia de aire en el circuito de frenos puede provocar una sensación esponjosa en la maneta del freno y una pérdida de eficacia en el frenado, lo cual es un riesgo significativo para la seguridad al conducir. Por lo tanto, es crucial mantener siempre el nivel adecuado de líquido en el depó…

</details>

<details><summary>🤖 <b>Mistral Large</b> — composite=0.777 · kw=0.83 · rouge=0.10 · spec=1.00 · halluc_risk=1.00</summary>

**Error crítico que NO se debe cometer al purgar el circuito de frenos:**
**Dejar que el depósito del líquido de frenos se vacíe por completo durante el proceso de purgado.**

---

### **Consecuencias de cometer este error:**
1. **Entrada de aire en el circuito:**
   - Si el nivel del líquido en el depósito baja demasiado (o se vacía), el sistema succionará aire a través de la bomba de freno o los conductos.
   - El aire es compresible, a diferencia del líquido de frenos (que es hidráulico e incompresible), lo que provocará:
     - **Pérdida de presión en la maneta/pedal de freno:** La maneta …

</details>

<details><summary>🤖 <b>Qwen 2.5 72B</b> — </summary>

_error / no response_

</details>

<details><summary>🤖 <b>Claude Sonnet</b> — composite=0.796 · kw=0.83 · rouge=0.21 · spec=1.00 · halluc_risk=1.00</summary>

# Error Crítico al Purgar Frenos

## ⚠️ EL ERROR QUE NUNCA DEBES COMETER:

**Dejar que el depósito de líquido de frenos se vacíe completamente**

## Consecuencias:

Si permites que el depósito se vacíe:

1. **El circuito cogerá aire** - Entrará aire en el sistema hidráulico
2. **Complicación del proceso** - Será mucho más difícil purgar correctamente el circuito después
3. **Pérdida de eficacia** - El aire en el sistema compromete la capacidad de frenado

## ¿Por qué es tan importante?

El sistema de frenos hidráulico funciona porque el líquido **no se comprime**. Si entra aire:
- El aire SÍ s…

</details>

---

### TC007 · diagnostic · medium · `es`

**Question:** La horquilla delantera de la moto se hunde demasiado durante los frenajes. ¿Cuáles son las causas y soluciones posibles?

**Ground truth:** Causas y soluciones: 1) Horquilla muy blanda: endurecer la horquilla, agregar 5mm de aceite o conseguir resortes más duros. 2) Sag del amortiguador trasero muy alto con compresión muy dura: aflojarlo para conseguir balance. Si continúa, ajustar de forma más progresiva.

<details><summary>🤖 <b>Gemma E2B (2B local)</b> — composite=0.617 · kw=0.86 · rouge=0.08 · spec=0.00 · halluc_risk=1.00</summary>

La horquilla delantera de la moto se hunde demasiado durante los frenajes, es un problema común que puede deberse a varios factores. 

**Causas:**

* **Horquilla demasiado blanda:** La horquilla está diseñada para absorber el impacto del frenado, pero si está demasiado blanda, se hundirá excesivamente. Esto puede ser debido a una horquilla vieja o con desgaste, o a una configuración incorrecta de la precarga.
* **Amortiguador trasero con sag alto y compresión muy dura:** El amortiguador trasero juega un papel importante en la absorción del impacto del frenado. Si el amortiguador tiene un sag a…

</details>

<details><summary>🤖 <b>GPT-4o</b> — composite=0.813 · kw=1.00 · rouge=0.12 · spec=1.00 · halluc_risk=1.00</summary>

Cuando la horquilla delantera de la moto se hunde demasiado durante los frenajes, puede deberse a varias causas relacionadas con la configuración de la suspensión. Aquí te detallo las posibles causas y soluciones:

### Causas:
1. **Horquilla demasiado blanda:** Los resortes de la horquilla pueden ser demasiado suaves, lo que provoca un hundimiento excesivo.
2. **Compresión de la horquilla mal ajustada:** Si la compresión está demasiado blanda, la horquilla no resistirá adecuadamente la carga durante el frenado.
3. **Amortiguador trasero mal ajustado:** Un amortiguador trasero con un sag muy al…

</details>

<details><summary>🤖 <b>Mistral Large</b> — composite=0.628 · kw=0.71 · rouge=0.05 · spec=1.00 · halluc_risk=0.20</summary>

**Causas del hundimiento excesivo de la horquilla durante el frenaje:**

1. **Resortes de horquilla demasiado blandos:**
   - Los resortes no tienen la tasa de carga (spring rate) adecuada para el peso del piloto o el estilo de conducción (ej. frenadas bruscas en curvas).
   - *Verificación:* Revisar el *sag estático* (hundimiento con el peso de la moto) y el *sag con piloto* (hundimiento con el piloto sentado). Si el sag supera el 30-35% del recorrido total de la horquilla, los resortes son insuficientes.

2. **Presión de aire insuficiente (en horquillas neumáticas):**
   - Si la horquilla es…

</details>

<details><summary>🤖 <b>Qwen 2.5 72B</b> — </summary>

_error / no response_

</details>

<details><summary>🤖 <b>Claude Sonnet</b> — composite=0.828 · kw=1.00 · rouge=0.18 · spec=1.00 · halluc_risk=1.00</summary>

# Diagnóstico: Horquilla que se hunde excesivamente al frenar

## **Causas principales:**

1. **Horquilla muy blanda** - La configuración de compresión es insuficiente
2. **Amortiguador trasero mal ajustado** - Si tiene el sag muy alto y está muy duro en compresión, transmite más carga hacia adelante
3. **Resortes de horquilla inadecuados** - Pueden ser demasiado blandos para tu peso/uso

## **Soluciones recomendadas (en orden):**

### **1. Endurecer la horquilla:**
- Ajusta la compresión de la horquilla hacia el lado más duro
- Esto reducirá el hundimiento excesivo

### **2. Agregar aceite (5…

</details>

---

### TC008 · diagnostic · hard · `es`

**Question:** La suspensión de una motocicleta está configurada en suave pero se siente extremadamente dura. ¿Cuál es la causa más probable de este comportamiento paradójico?

**Ground truth:** La causa es que la horquilla y/o el amortiguador tienen muy poco rebote (rebote muy lento). Esto hace que al recibir un bache tras otro, la suspensión no llegue a tener nunca su recorrido completo, trabajando siempre en la parte más dura del recorrido (tercera parte hacia abajo). La solución es aume…

<details><summary>🤖 <b>Gemma E2B (2B local)</b> — composite=0.652 · kw=0.33 · rouge=0.16 · spec=1.00 · halluc_risk=1.00</summary>

La causa más probable de un comportamiento paradójico donde la suspensión de una moto está configurada en suave pero se siente extremadamente dura, es que **el amortiguador tenga muy poco rebote**. 

**Explicación:**

* La configuración "suave" implica un amortiguador con poca capacidad de absorber impactos y rebotar.
* Cuando la moto se encuentra sobre un piso duro, el amortiguador no tiene suficiente capacidad para absorber la energía del impacto y devolverla a la moto. Esto hace que la moto se sienta dura y rígida. 

**Advertencia:**  Es importante recordar que la configuración de la suspen…

</details>

<details><summary>🤖 <b>GPT-4o</b> — composite=0.790 · kw=0.67 · rouge=0.40 · spec=1.00 · halluc_risk=1.00</summary>

La causa más probable de que una suspensión configurada en suave se sienta extremadamente dura es que la horquilla y/o el amortiguador tienen muy poco rebote, es decir, el rebote es muy lento. Esto provoca que la suspensión trabaje en la parte más dura del recorrido, desde la tercera parte hacia abajo. Como resultado, al recibir impactos consecutivos, la suspensión no logra extenderse completamente entre cada impacto, lo que hace que se sienta dura. La solución a este problema es ajustar el rebote para que sea más rápido, permitiendo que la suspensión utilice todo su recorrido de manera más ef…

</details>

<details><summary>🤖 <b>Mistral Large</b> — composite=0.822 · kw=1.00 · rouge=0.14 · spec=1.00 · halluc_risk=1.00</summary>

**Respuesta basada en el manual de taller proporcionado:**

La causa más probable de que una suspensión configurada en **"suave"** (rebote y compresión con ajustes blandos) **se sienta extremadamente dura** es que el **rebote está demasiado lento** (poco rebote).

### Explicación técnica:
- Cuando el rebote es muy lento, la horquilla o el amortiguador **no tienen tiempo de recuperar su posición original** entre un impacto y otro (ej.: baches seguidos).
- Esto hace que la suspensión **trabaje solo en la parte más dura de su recorrido** (tercio inferior), sin aprovechar el recorrido completo.
- …

</details>

<details><summary>🤖 <b>Qwen 2.5 72B</b> — </summary>

_error / no response_

</details>

<details><summary>🤖 <b>Claude Sonnet</b> — composite=0.847 · kw=1.00 · rouge=0.27 · spec=1.00 · halluc_risk=1.00</summary>

Según el manual de taller, cuando la suspensión está configurada en **suave pero se siente dura**, la causa más probable es:

## **Rebote muy lento (insuficiente)**

### ¿Por qué ocurre esto?

Cuando la horquilla y/o el amortiguador tienen **muy poco rebote** (ajuste muy lento), la suspensión trabaja constantemente en la parte más dura de su recorrido (aproximadamente del tercio inferior hacia abajo). 

Al recibir impactos consecutivos (pozos, baches), la suspensión **no tiene tiempo de extenderse completamente** entre un impacto y otro, quedando "empaquetada" o comprimida. Esto hace que traba…

</details>

---

### TC009 · diagnostic · medium · `es`

**Question:** En una motocicleta de motocross, la parte trasera tiende a adelantar a la delantera en las curvas. ¿Cuál es el primer ajuste a realizar?

**Ground truth:** Bajar la horquilla delantera unos 2-3 mm en los topes de la tija y verificar si el síntoma cambia. Si persiste, conseguir resortes más duros para la horquilla, ya que muchas motos vienen con resortes muy blandos de fábrica generando falta de balance.

<details><summary>🤖 <b>Gemma E2B (2B local)</b> — composite=0.719 · kw=0.60 · rouge=0.17 · spec=1.00 · halluc_risk=1.00</summary>

En una motocicleta de motocross, la parte trasera tiende a adelantar a la delantera en las curvas debido a la configuración del chasis y la suspensión.  El primer ajuste a realizar es **ablandar la compresión de la horquilla** para mejorar el balance. 

**Explicación:**

* El manual menciona que la acción de la suspensión en una curva implica que la horquilla se carga con mucha presión y el amortiguador se descarga totalmente.
* Si la horquilla está muy blanda, se hundirá excesivamente, mientras que un amortiguador con sag alto y compresión alta transmitirá mucha más carga adelante. 
* Ablanda…

</details>

<details><summary>🤖 <b>GPT-4o</b> — composite=0.521 · kw=0.40 · rouge=0.17 · spec=0.00 · halluc_risk=1.00</summary>

En una motocicleta de motocross, si la parte trasera tiende a adelantar a la delantera en las curvas, el primer ajuste que deberías considerar es ablandar la compresión de la horquilla delantera y/o endurecer el amortiguador trasero. Esto ayudará a balancear la moto y mejorar la estabilidad en las curvas. 

Asegúrate de realizar estos ajustes en un entorno seguro y de probar la motocicleta en condiciones controladas después de cada cambio para evaluar el efecto. Si el problema persiste, podría ser necesario consultar a un especialista en amortiguación para un ajuste más preciso. Recuerda siemp…

</details>

<details><summary>🤖 <b>Mistral Large</b> — composite=0.809 · kw=1.00 · rouge=0.11 · spec=1.00 · halluc_risk=1.00</summary>

Basándome en el contexto del manual proporcionado y en tu descripción del problema (**la parte trasera tiende a adelantar a la delantera en curvas**), el **primer ajuste recomendado** es:

### **1. Aumentar la altura de la horquilla (bajarla en las tijas 2-3 mm)**
**¿Por qué?**
- Al bajar la horquilla en las tijas (sin modificar la suspensión trasera), **aumentas la carga sobre la rueda delantera**, mejorando la tracción y evitando que la trasera "adelante" o se sienta inestable en curvas.
- Esto es un ajuste rápido y reversible que suele corregir el desbalance inicial sin necesidad de modific…

</details>

<details><summary>🤖 <b>Qwen 2.5 72B</b> — </summary>

_error / no response_

</details>

<details><summary>🤖 <b>Claude Sonnet</b> — composite=0.513 · kw=0.40 · rouge=0.14 · spec=0.00 · halluc_risk=1.00</summary>

Según el manual de taller, cuando la parte trasera tiende a adelantar a la delantera en las curvas, **el primer ajuste NO debe ser reducir el rebote** (aunque sea la reacción instintiva).

## Primer ajuste recomendado:

**Ablandar la compresión de la horquilla delantera y/o endurecer el amortiguador trasero** para balancear la motocicleta.

## Ajustes adicionales si el problema persiste:

1. **Hacer más rápido el rebote trasero** (menos clicks de rebote)
2. **Darle más altura a la moto atrás** (reducir el sag trasero)

## Secuencia lógica de diagnóstico:

El problema indica que hay un desbalan…

</details>

---

### TC010 · diagnostic · medium · `es`

**Question:** Después de aterrizar de un salto, la horquilla hace mucho ruido pero el comportamiento de la suspensión se siente bien. ¿Cuál es la causa probable?

**Ground truth:** La causa probable es el guardabarro y no la horquilla. Los guardabarros con mucho uso o los que no son originales se sacuden y tocan la rueda durante los aterrizajes, produciendo el ruido. Es un diagnóstico importante para no hacer reparaciones innecesarias a la horquilla.

<details><summary>🤖 <b>Gemma E2B (2B local)</b> — composite=0.790 · kw=0.80 · rouge=0.25 · spec=1.00 · halluc_risk=1.00</summary>

La causa probable es que **el guardabarros está tocando la rueda delantera**. 

**Advertencia:**  Es importante destacar que este es un problema común y no necesariamente indica un mal funcionamiento de la horquilla. Sin embargo, el ruido al aterrizar después del salto puede ser síntoma de que el guardabarros está en contacto con la rueda. 

**Recomendaciones:**
* **Inspeccionar los guardabarros:** Verificar si están dañados o deformados y si se encuentran en buen estado.
* **Ajustar el guardabarro:** Si el guardabarro está demasiado cerca de la rueda, puede ser necesario ajustarlo para que no…

</details>

<details><summary>🤖 <b>GPT-4o</b> — composite=0.835 · kw=1.00 · rouge=0.22 · spec=1.00 · halluc_risk=1.00</summary>

La causa probable del ruido en la horquilla después de aterrizar de un salto, a pesar de que el comportamiento de la suspensión se sienta bien, podría ser un problema con el guardabarros. Como se menciona en el contexto del manual, los guardabarros que se sacuden y tocan la rueda pueden generar ruidos, especialmente si no son originales o tienen mucho uso. Esto no necesariamente indica un problema con la horquilla en sí.

**Advertencia de seguridad:** Antes de realizar cualquier inspección o ajuste, asegúrate de que la motocicleta esté apagada y estable para evitar accidentes. Si no estás segu…

</details>

<details><summary>🤖 <b>Mistral Large</b> — composite=0.657 · kw=0.80 · rouge=0.10 · spec=1.00 · halluc_risk=0.00</summary>

Basándome en el contexto del manual y en mi experiencia como mecánico, **el ruido que describes al aterrizar de un salto (pero con un comportamiento normal de la suspensión) tiene una causa muy probable: el guardabarros delantero**.

### **Posibles causas y soluciones:**
1. **Guardabarros flojo o en contacto con la rueda**
   - **Síntomas:** Ruido metálico o de rozamiento al comprimir la horquilla (especialmente después de saltos), pero sin afectar el rendimiento.
   - **Verificación:**
     - Inspecciona visualmente si el guardabarros está torcido, agrietado o mal ajustado.
     - Levanta la …

</details>

<details><summary>🤖 <b>Qwen 2.5 72B</b> — </summary>

_error / no response_

</details>

<details><summary>🤖 <b>Claude Sonnet</b> — composite=0.780 · kw=0.80 · rouge=0.19 · spec=1.00 · halluc_risk=1.00</summary>

Según el manual de taller, **la causa probable NO es un problema de la horquilla**, sino del **guardabarros**.

## Diagnóstico:

El manual indica textualmente que esto "va a sonar cómico", pero muchas veces el ruido proviene del **guardabarros que se sacude y toca la rueda**, especialmente cuando:

- El guardabarros tiene **mucho uso/desgaste**
- Es un guardabarros **no original** (aftermarket)

## Verificación recomendada:

1. **Inspecciona el guardabarros delantero** buscando:
   - Holguras en los puntos de montaje
   - Deformaciones o grietas
   - Distancia entre el guardabarros y la rueda
…

</details>

---

### TC011 · maintenance · easy · `es`

**Question:** ¿Cómo influye el nivel de habilidad del piloto en la configuración óptima de la suspensión de una motocicleta?

**Ground truth:** Un piloto PRO necesita más rebote rápido y compresión más dura porque ataca en todos los lugares de la pista y tiene mejor estado físico. Un piloto principiante necesita una moto que perdone más errores, con suspensión más blanda, ya que tiene menos estado físico y descansa en partes de la pista; un…

<details><summary>🤖 <b>Gemma E2B (2B local)</b> — composite=0.704 · kw=0.50 · rouge=0.23 · spec=1.00 · halluc_risk=1.00</summary>

La habilidad del piloto tiene un impacto significativo en la configuración óptima de la suspensión de una motocicleta. 

**Pilotos más experimentados y con mayor velocidad:**

* **Requieren mayor rigidez:**  Utilizan un rebote más rápido y una compresión más dura, lo que les permite atacar con mayor agresividad y control en la pista.
* **Necesitan mayor resistencia:**  La mayor cantidad de impactos durante el recorrido requiere una suspensión más resistente para soportar las vibraciones y los golpes.

**Pilotos menos experimentados o con menor velocidad:**

* **Requieren mayor comodidad:**  Bu…

</details>

<details><summary>🤖 <b>GPT-4o</b> — composite=0.676 · kw=0.67 · rouge=0.24 · spec=1.00 · halluc_risk=1.00</summary>

El nivel de habilidad del piloto influye significativamente en la configuración óptima de la suspensión de una motocicleta. Los pilotos más experimentados, como los corredores PRO, tienden a preferir configuraciones de suspensión más duras y con un rebote más rápido. Esto se debe a que atacan más agresivamente en la pista y su estado físico les permite manejar grandes impactos sin fatigarse rápidamente. Una suspensión más dura les proporciona la estabilidad y el control necesarios para mantener un ritmo alto en condiciones exigentes.

Por otro lado, los pilotos menos experimentados o más lento…

</details>

<details><summary>🤖 <b>Mistral Large</b> — composite=0.644 · kw=0.83 · rouge=0.06 · spec=1.00 · halluc_risk=0.00</summary>

El nivel de habilidad del piloto es **uno de los factores más críticos** en la configuración óptima de la suspensión de una motocicleta, ya que determina cómo la moto debe responder a las demandas de la conducción, el estilo de pilotaje y las condiciones físicas del piloto. Según el contexto del manual, estas son las influencias clave, explicadas de forma práctica y segura:

---

### **1. Diferencias en la configuración según el nivel del piloto**
#### **Piloto PRO (avanzado/experto)**
- **Compresión (horquilla y amortiguador):**
  - **Más dura** (especialmente en la horquilla).
  - *Razón:* U…

</details>

<details><summary>🤖 <b>Qwen 2.5 72B</b> — composite=0.716 · kw=0.67 · rouge=0.10 · spec=1.00 · halluc_risk=1.00</summary>

El nivel de habilidad del piloto tiene una influencia significativa en la configuración óptima de la suspensión de una motocicleta. Aquí te explico cómo:

### 1. **Compresión y Rebound (Rebote)**
- **Piloto Profesional (PRO):**
  - **Compresión:** Los pilotos profesionales suelen preferir una compresión más dura. Esto se debe a que atacan la pista con mayor agresividad y velocidad, lo que genera mayores impactos. Una compresión más dura ayuda a mantener el control y la estabilidad en situaciones extremas.
  - **Rebound:** El rebote también tiende a ser más rápido. Esto permite que la suspensió…

</details>

<details><summary>🤖 <b>Claude Sonnet</b> — composite=0.798 · kw=0.83 · rouge=0.33 · spec=1.00 · halluc_risk=1.00</summary>

# Influencia del Nivel de Habilidad en la Configuración de Suspensión

Según el manual, el nivel de habilidad del piloto tiene un **impacto directo y significativo** en la configuración óptima de la suspensión:

## **Piloto PRO/Experto:**

- **Rebote:** Mucho más rápido
- **Compresión:** Más dura
- **Razones:**
  - Ataca agresivamente en todos los sectores de la pista
  - La moto recibe grandes impactos constantes
  - Mejor condición física para soportar una suspensión más dura
  - Necesita respuesta inmediata y precisa

## **Piloto Principiante/Intermedio:**

- **Rebote:** Más lento
- **Compr…

</details>

---

### TC012 · specification · easy · `en`

**Question:** What is the specified torque for the final gearbox cover bolts on a Suzuki Burgman UH125?

**Ground truth:** The final gear box cover bolts must be tightened in ascending order of the numbered sequence to a torque of 22 N·m (2.2 kgf-m).

<details><summary>🤖 <b>Gemma E2B (2B local)</b> — composite=0.758 · kw=0.60 · rouge=0.49 · spec=1.00 · halluc_risk=1.00</summary>

The specified torque for the final gearbox cover bolts on a Suzuki Burgman UH125 is **22 N·m (2.2 kgf-m)**.

</details>

<details><summary>🤖 <b>GPT-4o</b> — composite=0.758 · kw=0.60 · rouge=0.49 · spec=1.00 · halluc_risk=1.00</summary>

The specified torque for the final gearbox cover bolts on a Suzuki Burgman UH125 is 22 N·m (2.2 kgf-m).

</details>

<details><summary>🤖 <b>Mistral Large</b> — composite=0.550 · kw=0.40 · rouge=0.15 · spec=0.50 · halluc_risk=0.50</summary>

Based on the **workshop manual context provided**, the **specified torque for the final gearbox cover bolts on a Suzuki Burgman UH125 is:**

**22 N·m (2.2 kgf·m / 16.2 lb-ft).**

### **Safety & Procedural Notes:**
1. **Always use a calibrated torque wrench** to ensure accurate tightening.
2. **Tighten bolts in ascending numerical order** (as marked on the cover) to prevent warping or leaks.
3. **Replace the O-ring with a new one** before reassembly to prevent oil leaks.
4. **Never rotate the shafts** when checking clearance with Plastigauge, as this can distort measurements.
5. **Apply engine …

</details>

<details><summary>🤖 <b>Qwen 2.5 72B</b> — composite=0.742 · kw=0.60 · rouge=0.23 · spec=1.00 · halluc_risk=1.00</summary>

The specified torque for the final gearbox cover bolts on a Suzuki Burgman UH125 is 22 N·m (2.2 kgf-m). 

**Safety Warning:**
Ensure that you use a torque wrench to tighten the bolts to the specified torque. Over-tightening can cause damage to the cover or the threads, while under-tightening can lead to oil leaks or the cover coming loose. Always follow the manufacturer's specifications and procedures to ensure safe and proper assembly.

</details>

<details><summary>🤖 <b>Claude Sonnet</b> — composite=0.837 · kw=1.00 · rouge=0.22 · spec=1.00 · halluc_risk=1.00</summary>

Based on the workshop manual provided, the specified torque for the final gearbox cover bolts is:

**22 N·m (2.2 kgf-m)**

**Important installation notes:**
- Tighten the bolts in **ascending order of numbers** (follow the numbered sequence on the cover)
- Replace the O-ring with a new one before installation
- Apply engine oil to each gear and shaft before assembly
- Fill the final gear box with the specified amount of oil after installation

This torque specification ensures proper sealing and prevents damage to the cover or housing threads.

</details>

---

### TC013 · specification · easy · `en`

**Question:** What is the torque specification for the clutch housing nut on a Suzuki scooter?

**Ground truth:** The clutch housing nut torque specification is 75 N·m (7.5 kgf-m).

<details><summary>🤖 <b>Gemma E2B (2B local)</b> — composite=0.841 · kw=1.00 · rouge=0.25 · spec=1.00 · halluc_risk=1.00</summary>

The torque specification for the clutch housing nut on a Suzuki scooter is **75 N·m (7.5 kgf-m)**. 

**Important Safety Warnings:**

* Always refer to your specific scooter's service manual for accurate torque specifications and procedures.  
* Use the correct tools and follow proper safety precautions when working on your motorcycle. 
* Never exceed the specified torque values, as this could damage the clutch housing or other components. 
* If you are unsure about any step in the repair process, consult a qualified mechanic.

</details>

<details><summary>🤖 <b>GPT-4o</b> — composite=0.858 · kw=1.00 · rouge=0.32 · spec=1.00 · halluc_risk=1.00</summary>

The torque specification for the clutch housing nut on a Suzuki scooter is 75 N·m (7.5 kgf-m). Make sure to use a torque wrench to accurately apply this torque, and ensure that the fixed drive face is held immovable using the special tool during the process. Always follow safety precautions to prevent injury or damage to the motorcycle.

</details>

<details><summary>🤖 <b>Mistral Large</b> — composite=0.606 · kw=0.67 · rouge=0.09 · spec=0.50 · halluc_risk=0.50</summary>

Based on the **workshop manual context provided**, the **torque specification for the clutch housing nut (rotor holder nut)** on the referenced Suzuki scooter is:

**75 N·m (7.5 kgf·m / 55 lb-ft)**

### **Important Notes & Safety Warnings:**
1. **Use the Special Tool** – The fixed drive face must be held **immovable** using the designated special tool (e.g., a rotor holder or clutch holding tool) to prevent damage or slippage while tightening.
2. **Washer Orientation** – Install the washer with its **convex side facing outward** (away from the clutch components).
3. **Prevent Roller Dislocatio…

</details>

<details><summary>🤖 <b>Qwen 2.5 72B</b> — composite=0.834 · kw=1.00 · rouge=0.19 · spec=1.00 · halluc_risk=1.00</summary>

The torque specification for the clutch housing nut on the Suzuki scooter, as provided in the manual context, is 75 N·m (7.5 kgf-m).

**Safety Warning:**
- Ensure that the fixed drive face is held immovable using the special tool while tightening the nut to prevent damage to the components and to ensure proper torque application.
- Check that the movable drive face is properly engaged with the spline to avoid any issues with the clutch operation.
- Be cautious when handling the assembly to prevent the roller from dislocating, which could lead to assembly failure or injury.

Always follow the m…

</details>

<details><summary>🤖 <b>Claude Sonnet</b> — composite=0.834 · kw=1.00 · rouge=0.19 · spec=1.00 · halluc_risk=1.00</summary>

Based on the workshop manual context provided:

**Clutch Housing Nut Torque Specification: 75 N·m (7.5 kgf-m)**

## Important Installation Notes:

When tightening this nut, you should:

1. **Use the special tool** to hold the fixed drive face immovable while tightening
2. **Install the washer correctly** with its convex (curved) side facing outward
3. **Work carefully** to prevent roller dislocation during assembly
4. **Verify engagement** - ensure the movable drive face is properly engaged with the spline
5. **Belt positioning** - pull the center area of upper and lower belt lines close toget…

</details>

---

### TC014 · procedure · medium · `en`

**Question:** Describe the correct procedure for installing a drive V-belt on a Suzuki CVT system.

**Ground truth:** 1. Compress the movable driven face towards the clutch shoe by hand. 2. Install the drive V-belt between the movable and fixed driven faces. 3. Position the belt so that the arrows point in the engine rotating direction. 4. Degrease the belt contacting surfaces. 5. Check that no roller inside the mo…

<details><summary>🤖 <b>Gemma E2B (2B local)</b> — composite=0.786 · kw=0.86 · rouge=0.18 · spec=1.00 · halluc_risk=1.00</summary>

Here's how to install a drive V-belt on a Suzuki CVT system, based on the provided manual context:

**1. Preparation:**

* **Safety First!**  Always disconnect the battery before working on any motorcycle electrical components. 
* **Degrease:** Use a suitable degreaser and clean cloth to thoroughly degrease the contact surfaces of the drive V-belt where it will make contact with the movable and fixed driven faces. This helps ensure proper belt alignment and reduces friction.

**2. Installing the Drive V-Belt:**

* **Position the Belt:**  Using your hands, compress the movable driven face towar…

</details>

<details><summary>🤖 <b>GPT-4o</b> — composite=0.813 · kw=0.86 · rouge=0.27 · spec=1.00 · halluc_risk=1.00</summary>

To correctly install a drive V-belt on a Suzuki CVT system, follow these steps carefully, ensuring all safety precautions are observed:

1. **Preparation:**
   - Ensure the motorcycle is on a stable surface and the engine is off. Allow the engine to cool down if it has been running.
   - Gather all necessary tools, including the special tool for holding the clutch housing immovable.

2. **Compress the Movable Driven Face:**
   - Use your hands to compress the movable driven face towards the clutch shoe. This will create enough space to install the drive V-belt.

3. **Install the Drive V-Belt:*…

</details>

<details><summary>🤖 <b>Mistral Large</b> — composite=0.661 · kw=0.86 · rouge=0.09 · spec=1.00 · halluc_risk=0.00</summary>

Here’s the **correct, safe, and step-by-step procedure** for installing a drive V-belt on a Suzuki CVT (Continuously Variable Transmission) system, based on the workshop manual context provided. **Safety warnings** are included where critical.

---

### **Tools & Materials Required**
- New drive V-belt (OEM or equivalent)
- Clutch spring compressor (special tool)
- Torque wrench
- Degreaser (e.g., brake cleaner)
- Clean lint-free rags
- Suzuki service manual (for torque specs)
- Nitrile gloves (to prevent contamination)

---

### **Safety Warnings**
1. **Spring Tension Hazard**: The clutch spr…

</details>

<details><summary>🤖 <b>Qwen 2.5 72B</b> — composite=0.756 · kw=0.71 · rouge=0.21 · spec=1.00 · halluc_risk=1.00</summary>

To install a drive V-belt on a Suzuki CVT (Continuously Variable Transmission) system, follow these steps carefully, ensuring safety and precision:

### Safety Precautions:
1. **Ensure the motorcycle is stable and supported** on a stand to prevent it from tipping over.
2. **Disconnect the battery** to prevent accidental starts.
3. **Wear appropriate personal protective equipment (PPE)**, including gloves and safety glasses.

### Procedure:

1. **Prepare the Components:**
   - **Degrease the drive V-belt contacting surfaces** to ensure a clean and secure fit.
   - **Inspect the rollers** for an…

</details>

<details><summary>🤖 <b>Claude Sonnet</b> — composite=0.822 · kw=0.86 · rouge=0.36 · spec=1.00 · halluc_risk=1.00</summary>

# Drive V-Belt Installation Procedure for Suzuki CVT System

Based on the workshop manual, here's the correct step-by-step procedure:

## Installation Steps

### 1. **Belt Positioning**
- Manually compress the movable driven face towards the clutch shoe
- While holding compression, install the drive V-belt between the movable and fixed driven faces
- **Important:** Position the belt so the directional arrows point in the engine's rotating direction

### 2. **Pre-Installation Preparation**
- Thoroughly degrease all drive V-belt contacting surfaces on both drive and driven faces
- Verify that no…

</details>

---

### TC015 · procedure · medium · `en`

**Question:** How do you safely remove brake caliper pistons when servicing the brakes on a motorcycle?

**Ground truth:** Place a rag over the brake caliper pistons to prevent them from popping out, then force out the pistons using compressed air. Before removal, place a rag underneath the union bolt on the brake caliper to catch any spilled brake fluid.

<details><summary>🤖 <b>Gemma E2B (2B local)</b> — composite=0.770 · kw=0.80 · rouge=0.17 · spec=1.00 · halluc_risk=1.00</summary>

Here's how to safely remove brake caliper pistons, based on the provided manual context:

**Safety First:**

* **Disconnect Battery:**  Always disconnect the battery before working on any motorcycle system. This prevents electrical shorts and potential injury from accidental contact with live wires. 
* **Work in a Well-Ventilated Area:** Brake fluid is toxic and can cause serious health problems if inhaled or absorbed through skin. Ensure you're working in a well-ventilated area, preferably outdoors.

**Procedure:**

1. **Prepare the Caliper:**  Place a rag underneath the union bolt of the bra…

</details>

<details><summary>🤖 <b>GPT-4o</b> — composite=0.826 · kw=1.00 · rouge=0.15 · spec=1.00 · halluc_risk=1.00</summary>

To safely remove brake caliper pistons when servicing the brakes on a motorcycle, follow these steps:

1. **Preparation:**
   - Ensure the motorcycle is securely supported on a stable surface to prevent any movement.
   - Wear appropriate personal protective equipment, such as gloves and safety glasses, to protect yourself from brake fluid and compressed air.

2. **Protect Surrounding Areas:**
   - Place a rag underneath the union bolt on the brake caliper to catch any spilled brake fluid.
   - Immediately wipe off any brake fluid that comes into contact with painted, plastic, or rubber parts,…

</details>

<details><summary>🤖 <b>Mistral Large</b> — composite=0.717 · kw=1.00 · rouge=0.12 · spec=1.00 · halluc_risk=0.00</summary>

### **Safe Removal of Brake Caliper Pistons (Motorcycle)**

Based on the workshop manual context, here’s the **correct and safe procedure** for removing brake caliper pistons:

---

### **Step-by-Step Procedure**

#### **1. Preparation & Safety**
- **Wear safety glasses** – Brake fluid is corrosive and can cause eye damage.
- **Work in a well-ventilated area** – Brake fluid fumes can be harmful.
- **Use nitrile gloves** – Brake fluid damages skin and paint.
- **Place a rag under the caliper** – To catch spilled brake fluid.
- **Do not reuse brake fluid** – Always use fresh DOT 4 (or specified)…

</details>

<details><summary>🤖 <b>Qwen 2.5 72B</b> — composite=0.811 · kw=1.00 · rouge=0.11 · spec=1.00 · halluc_risk=1.00</summary>

To safely remove the brake caliper pistons when servicing the brakes on a motorcycle, follow these steps carefully:

1. **Prepare the Work Area:**
   - Ensure the motorcycle is securely supported on a stand to prevent it from tipping over.
   - Place a rag underneath the union bolt on the brake caliper to catch any split brake fluid. Brake fluid can damage paint, plastics, and rubber materials, so it's important to prevent any spills.

2. **Remove the Brake Caliper:**
   - Loosen and remove the bolts that secure the brake caliper to the motorcycle. Carefully lift the caliper off the brake roto…

</details>

<details><summary>🤖 <b>Claude Sonnet</b> — composite=0.834 · kw=1.00 · rouge=0.19 · spec=1.00 · halluc_risk=1.00</summary>

# Safe Removal of Brake Caliper Pistons

Based on the workshop manual, here's the proper procedure:

## Step-by-Step Process:

1. **Preparation**
   - Place a rag underneath the union bolt on the brake caliper to catch any spilled brake fluid
   - Remove the brake caliper from the motorcycle
   - Remove the brake pads, brake pad spring, and brake caliper holder

2. **Piston Removal**
   - **Place a rag over the brake caliper pistons** - This is critical to prevent the pistons from popping out uncontrollably
   - **Use compressed air** to force out the pistons gradually
   - Apply air pressure …

</details>

---

### TC016 · safety · easy · `en`

**Question:** What safety precautions must be followed when running a motorcycle engine indoors during service work?

**Ground truth:** When running the engine indoors, make sure that exhaust gas is forced outdoors. When working with toxic or flammable materials, ensure the work area is well-ventilated and follow all manufacturer's instructions. Never use gasoline as a cleaning solvent.

<details><summary>🤖 <b>Gemma E2B (2B local)</b> — composite=0.658 · kw=0.29 · rouge=0.27 · spec=1.00 · halluc_risk=1.00</summary>

When running a motorcycle engine indoors for service work, **you MUST ensure that exhaust gas is forced outdoors.** 

This is crucial to prevent the buildup of potentially dangerous fumes in your workspace.  

**Safety Warning:** Improperly venting exhaust gases can lead to carbon monoxide poisoning and other health hazards. Always prioritize safety when working with engines.

</details>

<details><summary>🤖 <b>GPT-4o</b> — composite=0.742 · kw=0.71 · rouge=0.13 · spec=1.00 · halluc_risk=1.00</summary>

When running a motorcycle engine indoors during service work, it is crucial to follow these safety precautions:

1. **Ventilation**: Ensure that the area is well-ventilated. Exhaust gases, including carbon monoxide, are hazardous and can accumulate quickly in enclosed spaces. Use exhaust extraction systems if available, or ensure that doors and windows are open to allow exhaust gases to be forced outdoors.

2. **Exhaust Gas Management**: Direct the exhaust gases outside using appropriate ducting or ventilation equipment to prevent the buildup of harmful fumes indoors.

3. **Fire Safety**: Keep…

</details>

<details><summary>🤖 <b>Mistral Large</b> — composite=0.780 · kw=0.86 · rouge=0.12 · spec=1.00 · halluc_risk=1.00</summary>

When running a motorcycle engine indoors during service work, the following **safety precautions** must be strictly followed to prevent **carbon monoxide poisoning, fire hazards, and other risks**:

### **1. Exhaust Gas Ventilation (Most Critical)**
- **Force exhaust outdoors** using a **properly rated exhaust extraction system** (e.g., a hose connected to the exhaust pipe leading outside).
- **Never rely on open windows or general ventilation alone**—carbon monoxide (CO) is odorless, colorless, and deadly.
- **Use a CO detector** in the workspace as an additional safety measure.

### **2. Fir…

</details>

<details><summary>🤖 <b>Qwen 2.5 72B</b> — composite=0.743 · kw=0.71 · rouge=0.13 · spec=1.00 · halluc_risk=1.00</summary>

When running a motorcycle engine indoors during service work, it is crucial to follow specific safety precautions to ensure the safety of the mechanic and the reliability of the motorcycle. Here are the key safety precautions:

1. **Exhaust Ventilation**: Ensure that the exhaust gases are properly vented to the outside. This can be achieved by using an exhaust extraction system or by opening windows and doors to create adequate ventilation. Exhaust gases contain carbon monoxide, which is toxic and can be fatal if inhaled in high concentrations.

2. **Fire Safety**: Keep the work area free of f…

</details>

<details><summary>🤖 <b>Claude Sonnet</b> — composite=0.797 · kw=0.86 · rouge=0.18 · spec=1.00 · halluc_risk=1.00</summary>

# Safety Precautions for Running Engine Indoors

Based on the workshop manual, when running a motorcycle engine indoors during service work, you **MUST** follow this critical safety precaution:

## Primary Requirement:
**Ensure that exhaust gas is forced outdoors.** This means you must have a proper exhaust extraction system in place that vents the fumes outside the building.

## Why This Is Critical:
- Motorcycle exhaust contains **carbon monoxide (CO)**, which is a colorless, odorless, and deadly gas
- Carbon monoxide poisoning can occur quickly in enclosed spaces
- Symptoms include headache…

</details>

---

### TC017 · diagnostic · medium · `en`

**Question:** On a Suzuki GSX-R600, how would you diagnose whether the combination meter (speedometer cluster) needs to be replaced after checking the coolant temperature indicator?

**Ground truth:** Connect a variable resistor between the ECT sensor coupler terminals. Turn ignition switch ON. Adjust resistance to specified values and check if the coolant temperature meter and indicator LED operate correctly. If either indication is abnormal, replace the combination meter assembly. Also check th…

<details><summary>🤖 <b>Gemma E2B (2B local)</b> — composite=0.698 · kw=0.50 · rouge=0.18 · spec=1.00 · halluc_risk=1.00</summary>

Here's how to diagnose if your Suzuki GSX-R600's combination meter needs replacement after checking the coolant temperature indicator:

**1. Understand the Manual:**

* The manual states that you should check the **engine coolant temperature meter (3) and indicator light (LED) (4)** operations *after* adjusting the variable resistor. 
* If either the meter or the indicator light is abnormal, you need to replace the combination meter assembly with a new one.

**2. Check for Abnormal Readings:**

* **Engine Coolant Temperature Meter:**  Look at the gauge on your instrument cluster. Does it show …

</details>

<details><summary>🤖 <b>GPT-4o</b> — composite=0.836 · kw=1.00 · rouge=0.21 · spec=1.00 · halluc_risk=1.00</summary>

To diagnose whether the combination meter on a Suzuki GSX-R600 needs to be replaced after checking the coolant temperature indicator, follow these steps:

1. **Safety Precautions**: Ensure the motorcycle is on a stable surface and the ignition is off before starting any diagnostic work. Wear appropriate personal protective equipment, such as gloves and safety glasses.

2. **Access the Combination Meter**: Remove any necessary panels or covers to access the combination meter and its connections. Refer to the motorcycle's service manual for specific instructions on accessing these components.

3…

</details>

<details><summary>🤖 <b>Mistral Large</b> — composite=0.697 · kw=1.00 · rouge=0.11 · spec=1.00 · halluc_risk=0.00</summary>

To diagnose whether the **Suzuki GSX-R600 combination meter (speedometer cluster)** needs replacement after checking the **coolant temperature indicator**, follow this **step-by-step, safe, and accurate** procedure based on the workshop manual context provided:

---

### **Tools & Materials Needed:**
- **Variable resistor (0–10 kΩ range, preferably 10-turn precision type)**
- **Digital multimeter (DMM) with resistance measurement**
- **Service manual (for exact resistance values at specific temperatures)**
- **Basic hand tools (screwdrivers, pliers, etc.)**
- **Safety gloves & eye protection**…

</details>

<details><summary>🤖 <b>Qwen 2.5 72B</b> — composite=0.826 · kw=1.00 · rouge=0.20 · spec=1.00 · halluc_risk=1.00</summary>

To diagnose whether the combination meter (speedometer cluster) on a Suzuki GSX-R600 needs to be replaced after checking the coolant temperature indicator, follow these steps:

### Step-by-Step Diagnosis

1. **Prepare the Motorcycle:**
   - Ensure the motorcycle is on a stable, level surface.
   - Turn off the engine and allow it to cool down to avoid burns or injuries.
   - Ensure the battery is fully charged to avoid any power issues during testing.

2. **Connect a Variable Resistor:**
   - Locate the engine coolant temperature (ECT) sensor terminals.
   - Connect a variable resistor (as spe…

</details>

<details><summary>🤖 <b>Claude Sonnet</b> — composite=0.844 · kw=1.00 · rouge=0.29 · spec=1.00 · halluc_risk=1.00</summary>

# Diagnosing Combination Meter Replacement on Suzuki GSX-R600

Based on the workshop manual procedure, here's how to diagnose if the combination meter needs replacement:

## Testing Procedure

1. **Disconnect the ECT (Engine Coolant Temperature) sensor coupler**

2. **Connect a variable resistor between the ECT sensor terminals**

3. **Turn the ignition switch ON**

4. **Test the meter response** by adjusting the variable resistor to specified resistance values and observe:
   - Engine coolant temperature meter (gauge) operation
   - Temperature indicator light (LED) operation

## Diagnosis Cr…

</details>

---

### TC018 · maintenance · medium · `es`

**Question:** ¿Cómo se mide el descentramiento del disco de freno y cuándo se debe reemplazar?

**Ground truth:** El descentramiento del disco de freno se mide usando un comparador de cuadrante (reloj comparador) montado en un soporte magnético. Si el descentramiento excede el límite de funcionamiento especificado por el fabricante, se debe cambiar el disco por uno nuevo.

<details><summary>🤖 <b>Gemma E2B (2B local)</b> — composite=0.820 · kw=0.80 · rouge=0.38 · spec=1.00 · halluc_risk=1.00</summary>

El descentramiento del disco de freno se mide utilizando un **comparador de cuadrante**. 

**Procedimiento:**

1.  **Mide el descentrado:** El manual indica que se debe usar un comparador de cuadrante para medir el descentrado del disco de freno. 
2.  **Límite de funcionamiento:** Si el descenso excede el límite de funcionamiento, **debe reemplazar el disco de freno por uno nuevo**.

**Advertencia:**

*   Es importante seguir las instrucciones del manual de taller con precisión para evitar daños a la motocicleta o lesiones personales. 
*   Si no estás seguro de cómo realizar este procedimiento…

</details>

<details><summary>🤖 <b>GPT-4o</b> — composite=0.837 · kw=1.00 · rouge=0.20 · spec=1.00 · halluc_risk=1.00</summary>

Para medir el descentramiento del disco de freno, sigue estos pasos:

1. **Herramientas necesarias**: Necesitarás un comparador de cuadrante y un soporte magnético para realizar la medición.

2. **Preparación**: Asegúrate de que la motocicleta esté en una posición estable y segura. Levanta la rueda de manera que pueda girar libremente.

3. **Instalación del comparador**: Fija el soporte magnético en una parte estable de la motocicleta, cerca del disco de freno. Coloca el comparador de cuadrante de manera que su punta toque la superficie del disco de freno.

4. **Medición**: Gira lentamente la …

</details>

<details><summary>🤖 <b>Mistral Large</b> — composite=0.664 · kw=0.80 · rouge=0.09 · spec=1.00 · halluc_risk=0.00</summary>

### **Procedimiento para medir el descentrado del disco de freno y criterios de reemplazo**

#### **1. Herramientas necesarias**
- **Comparador de cuadrante** (con soporte magnético o base estable).
- **Soporte magnético** (para fijar el comparador a la horquilla o basculante).
- **Llave dinamométrica** (si es necesario desmontar componentes para acceder al disco).
- **Manual de taller específico del modelo** (para conocer el **límite de descentrado permitido**).

---

#### **2. Pasos para medir el descentrado**
**⚠️ Advertencias de seguridad:**
- **Trabaje con la moto en un soporte estable** …

</details>

<details><summary>🤖 <b>Qwen 2.5 72B</b> — composite=0.828 · kw=1.00 · rouge=0.17 · spec=1.00 · halluc_risk=1.00</summary>

Para medir el descentramiento del disco de freno, sigue estos pasos:

1. **Preparación**:
   - Asegúrate de que la motocicleta esté en un lugar estable y seguro. Utiliza el caballete central o un soporte adecuado.
   - Retira la rueda correspondiente si es necesario para acceder al disco de freno.

2. **Uso del Comparador de Cuadrante**:
   - Coloca el disco de freno en un soporte magnético o en un banco de trabajo donde pueda girar libremente.
   - Posiciona el comparador de cuadrante en el borde del disco de freno. Asegúrate de que el pie del comparador esté en contacto con la superficie del…

</details>

<details><summary>🤖 <b>Claude Sonnet</b> — composite=0.842 · kw=1.00 · rouge=0.24 · spec=1.00 · halluc_risk=1.00</summary>

# Medición del Descentramiento del Disco de Freno

## Procedimiento de Medición

Para medir el descentramiento del disco de freno, siga estos pasos:

1. **Herramienta necesaria:**
   - Comparador de cuadrante (reloj comparador)
   - Soporte magnético

2. **Método:**
   - Monte el comparador de cuadrante en un soporte magnético
   - Coloque el palpador del comparador contra la superficie del disco de freno
   - Gire el disco completamente y observe las lecturas
   - Registre la variación máxima (diferencia entre la lectura más alta y más baja)

## Criterio de Reemplazo

**Debe reemplazar el dis…

</details>

---

### TC019 · procedure · hard · `en`

**Question:** What is the critical check to perform after assembling the CVT movable drive face, and what problem does it prevent?

**Ground truth:** After assembly, check that the movable drive face is properly engaged. During assembly, verify that no roller inside the movable drive face is out of its slot. Failure to check this can cause the roller to dislocate, which can damage the CVT system during operation.

<details><summary>🤖 <b>Gemma E2B (2B local)</b> — composite=0.781 · kw=0.60 · rouge=0.44 · spec=1.00 · halluc_risk=1.00</summary>

The critical check to perform after assembling the CVT movable drive face is **to ensure that no roller inside the movable drive face is out of the slot.** 

**Problem prevented:**  If a roller is out of its slot, it can cause **the belt to slip or become misaligned**, leading to **reduced power transmission and potential damage to the CVT system**. This could result in jerky acceleration, loss of engine power, and ultimately, failure of the drive train.

</details>

<details><summary>🤖 <b>GPT-4o</b> — composite=0.808 · kw=0.80 · rouge=0.32 · spec=1.00 · halluc_risk=1.00</summary>

After assembling the CVT movable drive face, it is critical to check that no roller inside the movable drive face is out of the slot. This check is essential because if any roller is dislocated, it can lead to improper functioning of the CVT system, causing issues such as uneven power transmission, increased wear, or even damage to the CVT components. Ensuring that all rollers are correctly positioned prevents these potential problems and ensures smooth operation of the drivetrain.

**Safety Warning:** Always ensure the motorcycle is securely supported and the engine is off before performing a…

</details>

<details><summary>🤖 <b>Mistral Large</b> — composite=0.796 · kw=0.80 · rouge=0.26 · spec=1.00 · halluc_risk=1.00</summary>

After assembling the **CVT movable drive face**, the **critical check** is to **verify that no roller inside the movable drive face is out of its slot**.

### **Why This Check is Critical:**
1. **Prevents CVT Malfunction** – If a roller is dislodged or misaligned, it can cause improper engagement between the movable and fixed drive faces, leading to **poor acceleration, belt slippage, or erratic clutch behavior**.
2. **Avoids Belt Damage** – A misaligned roller can cause uneven belt tension, leading to **premature belt wear or failure**.
3. **Prevents Internal Damage** – A dislocated roller ma…

</details>

<details><summary>🤖 <b>Qwen 2.5 72B</b> — composite=0.760 · kw=0.60 · rouge=0.33 · spec=1.00 · halluc_risk=1.00</summary>

After assembling the CVT movable drive face, the critical check to perform is to ensure that no roller inside the movable drive face is out of the slot. This check is crucial because it prevents the rollers from dislocating, which can cause the drive V-belt to malfunction or fail. If a roller is out of its slot, it can lead to improper engagement of the drive faces, resulting in poor transmission performance, potential belt damage, or even a complete failure of the CVT system.

**Safety Warning:**
Ensure that the drive V-belt is properly positioned and that all components are securely assemble…

</details>

<details><summary>🤖 <b>Claude Sonnet</b> — composite=0.838 · kw=1.00 · rouge=0.22 · spec=1.00 · halluc_risk=1.00</summary>

# Critical Check After CVT Movable Drive Face Assembly

## The Critical Check:

**Check that no roller inside the movable drive face is out of the slot.**

This inspection must be performed after installing the movable drive face and before final assembly.

## Problem It Prevents:

If rollers are dislocated or out of their slots, it will cause:

1. **Improper CVT operation** - The centrifugal mechanism won't function correctly
2. **Uneven engagement** - Leading to jerky acceleration and poor performance
3. **Severe mechanical damage** - Dislocated rollers can:
   - Jam the CVT mechanism
   - D…

</details>

---

### TC020 · diagnostic · hard · `es`

**Question:** En una motocicleta de enduro, ¿por qué podría ser necesario ajustar diferente la suspensión para terreno arenoso comparado con terreno de tierra normal?

**Ground truth:** En pistas arenosas los pozos son más grandes, más profundos y más separados que en tierra. Por eso la compresión y el rebote deben ser más duros y lentos, y el sag debe aumentarse unos 5mm. La analogía útil es: piso duro (arena compactada) = amortiguación y cubiertas blandas; piso blando (arena suel…

<details><summary>🤖 <b>Gemma E2B (2B local)</b> — composite=0.549 · kw=0.57 · rouge=0.11 · spec=0.00 · halluc_risk=1.00</summary>

En una motocicleta de enduro, la suspensión debe ajustarse para terrenos arenosos en comparación con terrenos de tierra normal por las siguientes razones:

**1.  El tipo de suelo:** 
    * **Arenas:** Son superficies irregulares y con baja adherencia, lo que dificulta el control de la moto. Esto requiere una mayor capacidad de rebote y compresión para absorber los impactos y mantener un buen agarre.
    * **Tierra:**  Es más consistente y estable, permitiendo una mayor estabilidad y menor necesidad de amortiguación.

**2.  La dinámica del terreno:** 
    * **Arenas:** Las superficies arenosas …

</details>

<details><summary>🤖 <b>GPT-4o</b> — composite=0.756 · kw=0.71 · rouge=0.21 · spec=1.00 · halluc_risk=1.00</summary>

En una motocicleta de enduro, ajustar la suspensión de manera diferente para terrenos arenosos en comparación con terrenos de tierra normal es crucial debido a las características únicas de cada tipo de superficie.

1. **Terreno Arenoso:**
   - **Compresión y Rebote:** En terrenos arenosos, los pozos y las irregularidades suelen ser más profundos y están más separados. Por lo tanto, es recomendable aumentar la compresión y el rebote (hacerlos más duros y lentos) para evitar que la suspensión se hunda demasiado rápido y pierda estabilidad.
   - **Sag:** Se sugiere aumentar el sag en aproximadam…

</details>

<details><summary>🤖 <b>Mistral Large</b> — composite=0.705 · kw=0.71 · rouge=0.07 · spec=1.00 · halluc_risk=1.00</summary>

En una motocicleta de enduro, el ajuste de la suspensión para **terreno arenoso** difiere del de **tierra normal** (compacta o con baches estándar) debido a las características físicas y dinámicas de cada superficie. Aquí las razones técnicas y prácticas, basadas en el contexto del manual y principios de suspensión:

---

### **1. Comportamiento de la arena vs. tierra compacta**
- **Arena**:
  - **Baja tracción y hundimiento**: La arena suelta ofrece poca resistencia al neumático, lo que genera mayor hundimiento de la rueda y reduce la estabilidad. La moto tiende a "flotar" o perder dirección.…

</details>

<details><summary>🤖 <b>Qwen 2.5 72B</b> — composite=0.698 · kw=0.57 · rouge=0.10 · spec=1.00 · halluc_risk=1.00</summary>

En una motocicleta de enduro, ajustar la suspensión de manera diferente para terreno arenoso comparado con terreno de tierra normal es crucial para mantener el control, la estabilidad y el rendimiento óptimo de la moto. Aquí te explico por qué:

### Terreno Arenoso:
1. **Menor Adherencia**:
   - **Compresión y Rebound**: En terreno arenoso, la adherencia es menor, lo que significa que la moto puede perder tracción más fácilmente. Para contrarrestar esto, se recomienda ajustar la compresión y el rebote de la suspensión para que sean más suaves. Esto permite que las ruedas mantengan mejor contac…

</details>

<details><summary>🤖 <b>Claude Sonnet</b> — composite=0.841 · kw=1.00 · rouge=0.24 · spec=1.00 · halluc_risk=1.00</summary>

# Ajuste de Suspensión: Terreno Arenoso vs. Tierra Normal

Según el manual, el terreno arenoso requiere ajustes específicos debido a sus características particulares:

## Diferencias del Terreno Arenoso

**Las pistas arenosas generan:**
- Pozos mucho más grandes y separados
- Pozos más profundos que en tierra normal
- Impactos más violentos y menos frecuentes

## Ajustes Necesarios para Arena

**1. Compresión y Rebote:**
- Deben ser **más elevados** (más duros, más lentos)
- Esto ayuda a absorber los impactos más grandes sin que la suspensión llegue al fondo

**2. Sag (hundimiento estático):**…

</details>

---

### TC021 · maintenance · easy · `es`

**Question:** ¿Por qué es importante el torque correcto al instalar bujías y cuáles son los riesgos de apretarlas mal?

**Ground truth:** El torque correcto es crítico: una bujía floja puede provocar fuga de gases de combustión. Una bujía muy apretada puede dañar la rosca de la cabeza del motor. Los valores varían si la cabeza es de hierro o aluminio y deben consultarse en el catálogo del fabricante.

<details><summary>🤖 <b>Gemma E2B (2B local)</b> — composite=0.811 · kw=0.86 · rouge=0.26 · spec=1.00 · halluc_risk=1.00</summary>

El torque correcto al instalar bujías es crucial porque **garantiza una conexión segura entre la bujía y la cabeza del motor, evitando fugas de gases de combustión y daños en la rosca**. 

**Si se instalan las bujías con un torque inadecuado, los riesgos son:**

* **Fuga de gases de combustión:** Una bujía floja puede causar una mala conexión entre la bujía y el motor, lo que podría provocar fugas de gases de combustión.
* **Daño en la rosca del motor:** Una bujía muy apretada puede dañar la rosca de la cabeza del motor, lo que podría requerir un reemplazo de la cabeza del motor o incluso una …

</details>

<details><summary>🤖 <b>GPT-4o</b> — composite=0.804 · kw=0.86 · rouge=0.23 · spec=1.00 · halluc_risk=1.00</summary>

Es crucial aplicar el torque correcto al instalar las bujías por varias razones:

1. **Fuga de gases de combustión**: Si una bujía está floja, puede provocar una fuga de gases de combustión. Esto no solo afecta el rendimiento del motor, sino que también puede causar daños a largo plazo debido a la acumulación de residuos de combustión en el área de la bujía.

2. **Daño a la rosca de la cabeza del motor**: Apretar demasiado una bujía puede dañar la rosca de la cabeza del motor. Esto es especialmente crítico en cabezas de motor de aluminio, que son más susceptibles a daños por sobreapriete. Repa…

</details>

<details><summary>🤖 <b>Mistral Large</b> — composite=0.710 · kw=1.00 · rouge=0.11 · spec=1.00 · halluc_risk=0.00</summary>

**Respuesta basada en el manual y buenas prácticas mecánicas:**

### **Importancia del torque correcto en las bujías**
El torque (apriete controlado) es crítico por dos razones principales:

1. **Sellado hermético de la cámara de combustión**
   - La bujía debe comprimir la junta (arandela de cobre o material similar) contra la cabeza del motor para evitar fugas de gases a alta presión y temperatura.
   - Un torque insuficiente deja la bujía floja, permitiendo que los gases escapen, lo que puede causar:
     - **Pérdida de compresión** (reducción de potencia).
     - **Sobrecalentamiento de la…

</details>

<details><summary>🤖 <b>Qwen 2.5 72B</b> — composite=0.715 · kw=0.57 · rouge=0.14 · spec=1.00 · halluc_risk=1.00</summary>

El torque correcto al instalar bujías es crucial por varias razones:

1. **Prevención de Fugas de Gases de Combustión**: Si las bujías están demasiado sueltas, pueden provocar fugas de gases de combustión. Estas fugas no solo reducen la eficiencia del motor y el rendimiento, sino que también pueden causar problemas de encendido y un aumento en el consumo de combustible.

2. **Protección de la Rosca de la Cabeza del Motor**: Si las bujías están demasiado apretadas, pueden dañar la rosca de la cabeza del motor. Este daño puede ser costoso de reparar y puede comprometer la integridad estructural …

</details>

<details><summary>🤖 <b>Claude Sonnet</b> — composite=0.850 · kw=1.00 · rouge=0.27 · spec=1.00 · halluc_risk=1.00</summary>

# Importancia del Torque Correcto en Bujías

## ¿Por qué es crucial el torque correcto?

El torque adecuado asegura un sellado óptimo entre la bujía y la cabeza del motor, garantizando:
- Transferencia correcta de calor
- Sellado hermético de la cámara de combustión
- Integridad de las roscas del motor

## Riesgos de Apretado Incorrecto

### **Bujía Floja (poco apretada):**
- ⚠️ **Fuga de gases de combustión** - pérdida de compresión
- Sobrecalentamiento de la bujía
- Carbonización prematura
- Pérdida de potencia del motor
- Posible daño al electrodo por temperatura excesiva

### **Bujía Muy A…

</details>

---

### TC022 · diagnostic · medium · `es`

**Question:** Durante la aceleración fuerte o a alta velocidad, el motor pierde potencia y el consumo de combustible aumenta. ¿Cuál es la causa más probable según el estado de las bujías?

**Ground truth:** La causa probable es el desgaste de las bujías por electro-erosión. El desgaste aumenta la distancia de salto de chispa entre electrodos, lo que requiere mayor voltaje para producir la chispa. En situaciones de alta demanda no se genera suficiente voltaje, causando pérdidas de explosión, desperdicio…

<details><summary>🤖 <b>Gemma E2B (2B local)</b> — composite=0.796 · kw=0.83 · rouge=0.23 · spec=1.00 · halluc_risk=1.00</summary>

La causa más probable para el aumento del consumo de combustible y pérdida de potencia durante aceleraciones fuertes o altas velocidades, en un motor con bujías desgastadas, es **la falta de chispa eficiente**. 

**Explicación:**

* **Electro-erosión:** Las bujías sufren desgaste debido a la electro-erosión, lo que afecta la distancia de salto de la chispa.
* **Disminución de potencia:**  Con un menor voltaje en la chispa, el motor no puede generar la misma cantidad de energía para impulsar el vehículo. 
* **Aumento del consumo de combustible:** El motor trabaja con mayor esfuerzo para compens…

</details>

<details><summary>🤖 <b>GPT-4o</b> — composite=0.870 · kw=1.00 · rouge=0.39 · spec=1.00 · halluc_risk=1.00</summary>

Según el contexto del manual proporcionado, la causa más probable de la pérdida de potencia y el aumento en el consumo de combustible durante la aceleración fuerte o a alta velocidad es el desgaste de las bujías debido a la electro-erosión. Este desgaste provoca un aumento en la distancia de salto de chispa, lo que requiere un mayor voltaje para encender la mezcla de aire-combustible. Si el voltaje no es suficiente, pueden perderse explosiones en el motor, lo que resulta en un desperdicio de combustible y una pérdida de potencia.

**Advertencia de seguridad:** Al revisar o cambiar las bujías, …

</details>

<details><summary>🤖 <b>Mistral Large</b> — composite=0.729 · kw=1.00 · rouge=0.18 · spec=1.00 · halluc_risk=0.00</summary>

Según el contexto del manual de taller proporcionado, **la causa más probable de la pérdida de potencia y el aumento en el consumo de combustible durante aceleraciones fuertes o altas velocidades es el desgaste de las bujías**.

### Explicación detallada:
1. **Electro-erosión y aumento de la distancia de salto de chispa**:
   - Con el uso, los electrodos de la bujía se desgastan, aumentando la distancia que debe recorrer la chispa (gap).
   - Esto obliga al sistema de encendido a generar un voltaje más alto para que la chispa salte correctamente.
   - En condiciones de alta demanda (aceleració…

</details>

<details><summary>🤖 <b>Qwen 2.5 72B</b> — composite=0.855 · kw=1.00 · rouge=0.30 · spec=1.00 · halluc_risk=1.00</summary>

La causa más probable de la pérdida de potencia y el aumento del consumo de combustible durante la aceleración fuerte o a alta velocidad es el desgaste de las bujías. Según el manual de taller, con el uso, las bujías sufren electro-erosión, lo que provoca un desgaste en el electrodo y aumenta la distancia de salto de chispa. Esto hace que la bujía requiera un mayor voltaje para producir la chispa necesaria, y en situaciones de alta demanda, como la aceleración a fondo o altas velocidades, puede no ser suficiente para encender completamente la mezcla de aire y combustible. Como resultado, se pi…

</details>

<details><summary>🤖 <b>Claude Sonnet</b> — composite=0.866 · kw=1.00 · rouge=0.37 · spec=1.00 · halluc_risk=1.00</summary>

Según el manual, la causa más probable es el **desgaste de los electrodos de las bujías por electro-erosión**.

## ¿Por qué ocurre esto?

Con el uso normal, las bujías sufren electro-erosión que provoca:

1. **Desgaste del electrodo** → aumenta la distancia de salto de chispa
2. **Mayor voltaje requerido** → la bujía necesita más energía para generar la chispa
3. **Pérdida de explosiones** → especialmente durante aceleración a fondo o altas velocidades

## Consecuencias:

- ❌ Desperdicio de combustible
- ❌ Pérdida de potencia
- ❌ Funcionamiento ineficiente del motor

## Solución:

✅ **Cambiar …

</details>

---

### TC023 · specification · medium · `es`

**Question:** ¿Cómo se debe calibrar la distancia entre electrodos de una bujía antes de instalarla?

**Ground truth:** Las bujías actuales se venden pre-calibradas de fábrica, sin embargo esta calibración puede no ser la correcta para todos los vehículos. Antes de instalar se debe verificar y ajustar la distancia entre electrodos al valor especificado por el fabricante del vehículo, usando un calibrador de bujías.

<details><summary>🤖 <b>Gemma E2B (2B local)</b> — composite=0.726 · kw=0.67 · rouge=0.18 · spec=1.00 · halluc_risk=1.00</summary>

El manual no proporciona instrucciones detalladas sobre cómo calibrar la distancia entre los electrodos de una bujía. 

**Advertencia:**  La calibración de bujías es un proceso delicado que requiere conocimientos técnicos y herramientas especializadas. **Si no estás seguro de cómo hacerlo, contacta con un mecánico cualificado.** 

Sin embargo, el manual menciona que las bujías actuales se venden pre-calibradas. Esto significa que la distancia entre los electrodos ya está ajustada en fábrica.

</details>

<details><summary>🤖 <b>GPT-4o</b> — composite=0.727 · kw=0.67 · rouge=0.09 · spec=1.00 · halluc_risk=1.00</summary>

Para calibrar la distancia entre los electrodos de una bujía antes de instalarla, sigue estos pasos:

1. **Consulta el Manual del Vehículo**: Antes de realizar cualquier ajuste, verifica en el manual del propietario o en el manual de taller de la motocicleta la especificación exacta de la distancia entre electrodos recomendada para tu modelo específico.

2. **Herramientas Necesarias**: Utiliza una galga de espesores o un calibrador de bujías. Estas herramientas te permitirán medir y ajustar con precisión la distancia entre los electrodos.

3. **Medición de la Distancia**: Inserta la galga de e…

</details>

<details><summary>🤖 <b>Mistral Large</b> — composite=0.654 · kw=0.83 · rouge=0.06 · spec=1.00 · halluc_risk=0.00</summary>

**Procedimiento para calibrar la distancia entre electrodos de una bujía (gap):**

### **Herramientas necesarias:**
- **Calibrador de bujías** (o galgas de espesores, preferiblemente de tipo *alambre* para mayor precisión).
- **Llave para bujías** (si es necesario retirar la bujía para ajustarla).
- **Manual de taller del vehículo** (para verificar la medida exacta del *gap* recomendado por el fabricante).

---

### **Pasos para calibrar el gap:**

#### **1. Verificar la especificación del fabricante**
- Consulta el **manual de taller de la motocicleta** o la etiqueta bajo el asiento/cubierta …

</details>

<details><summary>🤖 <b>Qwen 2.5 72B</b> — composite=0.765 · kw=0.83 · rouge=0.09 · spec=1.00 · halluc_risk=1.00</summary>

Para calibrar la distancia entre los electrodos de una bujía antes de instalarla, sigue estos pasos:

### Herramientas Necesarias:
- **Calibrador de bujías** (también conocido como calibrador de espesor o gap gauge).
- **Llave de bujías**.
- **Pinzas de ajuste** (si es necesario).

### Pasos:

1. **Verifica la Especificación del Fabricante:**
   - Consulta el manual del propietario o el manual de servicio del vehículo para determinar la distancia correcta entre los electrodos (gap) recomendada por el fabricante. Esta distancia varía según el modelo y año del vehículo.

2. **Inspecciona la Bují…

</details>

<details><summary>🤖 <b>Claude Sonnet</b> — composite=0.815 · kw=1.00 · rouge=0.14 · spec=1.00 · halluc_risk=1.00</summary>

# Calibración de la Distancia entre Electrodos de una Bujía

Aunque el manual menciona que es necesario calibrar la distancia entre electrodos, **no proporciona el procedimiento específico** de cómo hacerlo. Sin embargo, puedo orientarte con la práctica estándar:

## Procedimiento General:

1. **Consulta la especificación**: Verifica en el manual del fabricante de tu motocicleta cuál es la distancia (gap) correcta para tu modelo específico.

2. **Herramienta necesaria**: Utiliza un **calibrador de bujías** (galga de espesores) para medir y ajustar.

3. **Medición**: Inserta la galga entre el e…

</details>

---

### TC024 · procedure · hard · `es`

**Question:** Cuando se cambia la puesta a punto de suspensión entre la primera y segunda manga de una carrera, ¿cuál es la recomendación principal?

**Ground truth:** Cambiar la puesta a punto entre mangas es un arma de doble filo: puede mejorar o empeorar el rendimiento. Si la moto está funcionando bien, es mejor no cambiar nada. Para quienes no están capacitados para hacer cambios precisos, es mejor mantener la configuración y resistir la segunda manga. Solo ba…

<details><summary>🤖 <b>Gemma E2B (2B local)</b> — composite=0.670 · kw=0.40 · rouge=0.17 · spec=1.00 · halluc_risk=1.00</summary>

La recomendación principal al cambiar la puesta a punto de suspensión entre la primera y segunda manga de una carrera es **depende**. 

**No hay una respuesta única.**  El manual menciona que "a veces se ve a un corredor andar mal en la primer serie y ganar en la segunda, pero a veces se ve un corredor "volar" en la primer serie y llegar quinto en la segunda". Esto significa que **la mejor opción depende del piloto y de su estilo**.

**Aquí hay algunos puntos a considerar:**

* **Experiencia del piloto:** Un piloto experimentado con una buena técnica puede beneficiarse de una puesta a punto má…

</details>

<details><summary>🤖 <b>GPT-4o</b> — composite=0.730 · kw=0.60 · rouge=0.22 · spec=1.00 · halluc_risk=1.00</summary>

La recomendación principal al considerar cambiar la puesta a punto de la suspensión entre la primera y segunda manga de una carrera es evaluar cuidadosamente si el cambio es realmente necesario. Si la moto está funcionando bien y el piloto se siente cómodo, es mejor dejar la configuración tal como está. Cambiar la puesta a punto puede ser un arma de doble filo, ya que puede mejorar o empeorar el rendimiento.

Si decides realizar cambios, asegúrate de tener la experiencia necesaria para hacer ajustes precisos. En condiciones extremas, la ayuda de un mecánico experimentado o de un corredor con e…

</details>

<details><summary>🤖 <b>Mistral Large</b> — composite=0.597 · kw=0.20 · rouge=0.08 · spec=1.00 · halluc_risk=1.00</summary>

**Respuesta basada en el manual de taller y buenas prácticas mecánicas:**

### **Recomendación principal:**
**No cambies la puesta a punto de la suspensión entre mangas a menos que:**
1. **Haya un problema claro y medible** (ej.: la moto se hunde demasiado, rebota sin control, o el piloto reporta una pérdida de tracción o fatiga extrema).
2. **Tengas experiencia y datos objetivos** (telemetría, feedback del piloto, condiciones de pista cambiantes como humedad, temperatura o desgaste de neumáticos).
3. **Las condiciones de la pista hayan variado significativamente** (ej.: pista más resbaladiza,…

</details>

<details><summary>🤖 <b>Qwen 2.5 72B</b> — composite=0.670 · kw=0.40 · rouge=0.17 · spec=1.00 · halluc_risk=1.00</summary>

La recomendación principal al considerar cambiar la puesta a punto de la suspensión entre la primera y segunda manga de una carrera es **no hacer cambios si la moto está funcionando bien**. Aquí hay algunos puntos clave a tener en cuenta:

1. **Consistencia**: Si la moto ha funcionado bien en la primera manga, es mejor mantener la configuración tal cual. Los cambios innecesarios pueden introducir variables que pueden afectar negativamente el rendimiento.

2. **Experiencia y Conocimiento**: Si no estás capacitado para hacer ajustes precisos, es mejor no hacer cambios. Los ajustes incorrectos pu…

</details>

<details><summary>🤖 <b>Claude Sonnet</b> — composite=0.837 · kw=1.00 · rouge=0.23 · spec=1.00 · halluc_risk=1.00</summary>

Según el manual de taller, la **recomendación principal es NO cambiar la puesta a punto si la moto está funcionando bien**.

## Puntos clave:

**Si la moto trabaja bien:**
- Es mejor dejarla como está
- Cambiar es arriesgado si no se tiene certeza de que funcionará mejor

**Cuándo considerar NO cambiar:**
- Si no estás capacitado para hacer ajustes con exactitud
- Si no tienes experiencia suficiente
- Cuando hay duda sobre el resultado del cambio

**Alternativa recomendada:**
En lugar de cambiar la suspensión, es mejor **esforzarse físicamente** para aguantar la segunda serie con la configurac…

</details>

---

### TC025 · safety · medium · `en`

**Question:** What must you do immediately after spilling brake fluid on a motorcycle during caliper service?

**Ground truth:** Immediately wipe off any brake fluid that contacts any part of the motorcycle. Brake fluid reacts chemically with paint, plastics, and rubber materials, severely damaging them. It is important to act immediately before the fluid has time to react with these surfaces.

<details><summary>🤖 <b>Gemma E2B (2B local)</b> — composite=0.867 · kw=1.00 · rouge=0.36 · spec=1.00 · halluc_risk=1.00</summary>

Immediately after spilling brake fluid on a motorcycle during caliper service, you must **wipe off any brake fluid contacting any part of the motorcycle.** 

**Why is this important?**

* Brake fluid reacts chemically with paint, plastics, rubber materials, etc., and will damage them severely.  
 
**Safety Warning:** Always wear appropriate safety gear when working on a motorcycle, including eye protection and gloves. 


Let me know if you have any other questions about your motorcycle service! 🏍️

</details>

<details><summary>🤖 <b>GPT-4o</b> — composite=0.807 · kw=0.86 · rouge=0.36 · spec=1.00 · halluc_risk=1.00</summary>

Immediately after spilling brake fluid on a motorcycle during caliper service, you must wipe off any brake fluid that comes into contact with any part of the motorcycle. Brake fluid is highly corrosive and can damage paint, plastics, rubber materials, and other surfaces if not promptly removed. Use a clean rag to thoroughly clean the affected areas to prevent any chemical damage. Always ensure you have rags or absorbent materials ready when working with brake fluid to quickly address any spills.

</details>

<details><summary>🤖 <b>Mistral Large</b> — composite=0.779 · kw=0.86 · rouge=0.13 · spec=1.00 · halluc_risk=1.00</summary>

**Immediate Actions After Spilling Brake Fluid on a Motorcycle:**

1. **Stop the Spill:**
   - Quickly contain the spill by placing a clean, absorbent rag underneath the source (e.g., union bolt, caliper, or master cylinder) to prevent further spread.

2. **Wipe Off Brake Fluid:**
   - **Immediately** wipe off any brake fluid that has contacted any part of the motorcycle using a clean, damp cloth. Brake fluid is highly corrosive and will damage:
     - **Paint** (causes bubbling, discoloration, or peeling).
     - **Plastics** (causes cracking or melting).
     - **Rubber** (causes swelling, h…

</details>

<details><summary>🤖 <b>Qwen 2.5 72B</b> — composite=0.842 · kw=1.00 · rouge=0.35 · spec=1.00 · halluc_risk=1.00</summary>

Immediately after spilling brake fluid on any part of the motorcycle during caliper service, you must wipe off the brake fluid thoroughly. Brake fluid can chemically react with and severely damage paint, plastics, rubber, and other materials. Use a clean, dry rag to remove all traces of the fluid from the affected areas. Ensure that you inspect the area to confirm that no brake fluid remains to prevent any potential damage.

</details>

<details><summary>🤖 <b>Claude Sonnet</b> — composite=0.861 · kw=1.00 · rouge=0.34 · spec=1.00 · halluc_risk=1.00</summary>

# Immediate Action for Spilled Brake Fluid

According to the workshop manual, you must **immediately wipe off any brake fluid** that contacts any part of the motorcycle.

## Why This Is Critical:

The manual explicitly warns that **brake fluid reacts chemically with:**
- Paint
- Plastics
- Rubber materials
- Other components

This chemical reaction **will damage them severely**.

## Best Practice:

- Keep rags positioned underneath union bolts and connections **before** loosening them to catch spills
- Have clean rags readily available during all brake service work
- Act quickly - don't delay …

</details>

---

## 5. Recommendations for Finetuning Pipeline

Based on the metric breakdown, here are the highest-leverage improvements:

1. **ROUGE-L is low** — responses use different vocabulary than the manual. This may reflect paraphrasing (not always bad), but if spec terminology is substituted for generic language, fine-tuning on domain vocabulary will help.


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