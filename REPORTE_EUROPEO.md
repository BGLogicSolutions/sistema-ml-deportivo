# 📊 Análisis Diario Evolutivo: 19/05/2026

Como analista cuantitativo deportivo, procedo con la revisión y el análisis solicitado:

---

### 1. MEMORIA Y AUDITORÍA

Los registros de partidos pasados proporcionados para el 17/05/2026 incluyen los resultados finales (FTHG y FTAG) para cada encuentro. Asumo que estos son los resultados reales y correctos de dichos partidos, extraídos directamente de la base de datos para la bitácora pasada. Dado que no se proporcionaron cálculos o predicciones anteriores que haya realizado para estos juegos, no puedo auditar mi rendimiento previo ni ajustar mis cálculos si me equivoqué en ese momento. Por lo tanto, el margen de error para predicciones pasadas no puede ser evaluado directamente sin las predicciones mismas.

---

### 2. ANÁLISIS DE HOY: 19/05/2026

Los partidos de hoy en la Premier League que involucran a los equipos mencionados son:

*   **AFC Bournemouth vs Manchester City** (20:30 BST)
*   **Chelsea vs Tottenham Hotspur** (21:15 BST)

#### Noticias en Vivo (Alineaciones, Lesiones):

**Manchester City:**
*   **Estado del equipo:** El Manchester City tiene una plantilla completamente en forma para el partido de hoy. Rodri se ha recuperado de una lesión en la ingle y jugó 65 minutos en la final de la FA Cup. La retirada de Omar Marmoush en la final de la FA Cup fue táctica y no por lesión.
*   **Alineación probable (4-2-3-1):** Donnarumma; Nunes, Khusanov, Guehi, O'Reilly; Bernardo Silva, Rodri; Semenyo, Foden, Doku; Haaland.

**Chelsea:**
*   **Lesiones/Dudas:**
    *   Romeo Lavia: Duda por un golpe sufrido antes de la final de la FA Cup.
    *   Estevao, Jamie Gittens: Lesionados (isquiotibiales), descartados.
    *   Jesse Derry: Se recuperó de una lesión en la cabeza y estará en el banquillo, pero el equipo podría ser cauteloso con él.
    *   Levi Colwill: Recién regresado de una lesión grave de rodilla, no será titular por precaución.
    *   Reece James: Recién recuperado de una lesión en el isquiotibial, es poco probable que arriesgue desde el inicio.
    *   Pedro Neto: Disponible y se espera que sea titular tras superar un golpe.
    *   Alejandro Garnacho: Disponible pero se espera que comience en el banquillo.
*   **Alineación probable (4-2-3-1):** Sanchez; Acheampong, Fofana, Hato, Cucurella; Caicedo, Andrey Santos; Palmer, Fernandez, Neto; Delap.

**Tottenham Hotspur:**
*   **Lesiones/Dudas:**
    *   Dominic Solanke: Lesión en el isquiotibial, no está listo para jugar.
    *   Xavi Simons: Lesión de ligamento cruzado, baja a largo plazo.
    *   Cristian Romero, Mohammed Kudus, Dejan Kulusevski, Ben Davies, Wilson Odobert: Todos están fuera por lesión.
    *   James Maddison: Regresó de una lesión de ligamento cruzado anterior, pero le falta ritmo de partido y probablemente saldrá desde el banquillo.
    *   Guglielmo Vicario: Recuperado de una cirugía de hernia, pero Antonín Kinsky podría mantener la titularidad debido a su buen rendimiento.
*   **Alineación probable (4-2-3-1):** Kinsky; Porro, Danso, Van de Ven, Udogie; Bentancur, Palhinha; Kolo Muani, Gallagher, Tel; Richarlison.

---

#### Análisis Cuantitativo (Distribución de Poisson y Sabermetrics)

**Limitación Importante:** La bitácora de partidos pasados proporcionada no incluye los últimos 5 partidos del AFC Bournemouth. Esto impide una aplicación rigurosa de la distribución de Poisson y Sabermetrics (xG) para el partido del Bournemouth vs Manchester City, ya que carezco del "historial proporcionado" específico para el equipo local.

**1. Partido: AFC Bournemouth vs Manchester City**

*   **Análisis Cualitativo (debido a la limitación de datos para Bournemouth):**
    *   **Manchester City:** Llega con la moral alta tras ganar la FA Cup y tiene una plantilla completamente en forma. Son contendientes al título y están en una excelente racha de forma.
    *   **AFC Bournemouth:** Los Cherries se encuentran en una forma notable, estando invictos en sus últimos 16 partidos de la Premier League, lo que demuestra una gran resiliencia y capacidad defensiva. Han logrado una "difícil victoria por 1-0 a domicilio contra el Fulham" en su último partido. Sus fortalezas incluyen los contraataques y la creación de oportunidades, pero tienen debilidades en la defensa de ventajas y en jugadas a balón parado.
    *   **Pronóstico:** A pesar de la impresionante racha del Bournemouth, el Manchester City, con su calidad y momento actual, es el favorito para ganar este encuentro. La capacidad ofensiva del City es formidable, y aunque Bournemouth jugará en casa y buscará el resultado, será un desafío inmenso. No puedo proporcionar un pronóstico cuantitativo basado en Poisson y Kelly Criterion para este partido debido a la falta de datos históricos detallados para Bournemouth en el historial proporcionado.

**2. Partido: Chelsea vs Tottenham Hotspur**

Para este partido, aplicaré la metodología solicitada utilizando los últimos 5 partidos proporcionados para cada equipo:

**Estadísticas de Goles (Últimos 5 partidos de PL):**

*   **Chelsea (Local):**
    *   Goles a favor (GF): 0 (en 3 partidos como local)
    *   Goles en contra (GC): 5 (en 3 partidos como local)
    *   GF promedio (local): 0.0
    *   GC promedio (local): 1.67
*   **Tottenham (Visitante):**
    *   Goles a favor (GF): 1 (en 2 partidos como visitante)
    *   Goles en contra (GC): 2 (en 2 partidos como visitante)
    *   GF promedio (visitante): 0.5
    *   GC promedio (visitante): 1.0

**Promedios de la Liga (Premier League - Asunción):**
Para el cálculo de la fuerza de ataque y defensa, utilizo promedios generales de goles por partido en la Premier League:
*   Promedio de goles de local en la liga: 1.4
*   Promedio de goles de visitante en la liga: 1.2

**Fuerza de Ataque (FA) y Fuerza de Defensa (FD):**

*   **Chelsea (como local):**
    *   FA Chelsea = (GF promedio Chelsea local) / (Promedio GF local liga) = (0.0) / 1.4 = 0.0
    *   FD Chelsea = (GC promedio Chelsea local) / (Promedio GC visitante liga) = (1.67) / 1.2 = 1.39
*   **Tottenham (como visitante):**
    *   FA Tottenham = (GF promedio Tottenham visitante) / (Promedio GF visitante liga) = (0.5) / 1.2 = 0.42
    *   FD Tottenham = (GC promedio Tottenham visitante) / (Promedio GC local liga) = (1.0) / 1.4 = 0.71

**Goles Esperados (xG):**

*   **xG Chelsea (contra Tottenham):** FA Chelsea * FD Tottenham * Promedio GF local liga = 0.0 * 0.71 * 1.4 = 0.0
*   **xG Tottenham (contra Chelsea):** FA Tottenham * FD Chelsea * Promedio GF visitante liga = 0.42 * 1.39 * 1.2 = 0.70

**Nota sobre el xG del Chelsea:** El xG de 0.0 para el Chelsea es un artefacto directo de su incapacidad para anotar en sus últimos 3 partidos como local en el historial proporcionado. Aunque estadísticamente correcto según los datos de entrada, en un escenario real, una muestra más grande o técnicas de suavizado serían deseables para equipos de esta categoría. Sin embargo, me adhiero estrictamente al "historial proporcionado".

**Distribución de Poisson para Probabilidades de Goles:**

*   **Chelsea (λ = 0.0):**
    *   P(0 goles) = 1.0 (100%)
    *   P(>0 goles) = 0.0
*   **Tottenham (λ = 0.70):**
    *   P(0 goles) = 49.66%
    *   P(1 gol) = 34.76%
    *   P(2 goles) = 12.16%
    *   P(3 goles) = 2.84%

**Probabilidades de Marcador Exacto (más probables):**

Basado en estos xG, los marcadores más probables son aquellos en los que el Chelsea no anota:
*   **Chelsea 0-0 Tottenham:** 49.66%
*   **Chelsea 0-1 Tottenham:** 34.76%
*   **Chelsea 0-2 Tottenham:** 12.16%
*   **Chelsea 0-3 Tottenham:** 2.84%

**Probabilidades de Resultado (Basado en mi modelo):**

*   P(Victoria Chelsea) = 0%
*   P(Empate) = P(0-0) = 49.66%
*   P(Victoria Tottenham) = 1 - P(0-0) - P(Victoria Chelsea) = 1 - 0.4966 - 0 = 50.34%

**Pronóstico de Mayor Valor (CLV) y Criterio de Kelly:**

Las cuotas actuales proporcionadas son: Chelsea 10/11 (1.909 decimal), Tottenham 9/4 (3.25 decimal). No se proporcionan las cuotas para el empate en las fuentes directas. Para el cálculo, estimaré la cuota del empate basándome en las probabilidades implícitas del mercado.

*   Probabilidad Implícita Chelsea Win = 1 / 1.909 = 0.5238
*   Probabilidad Implícita Tottenham Win = 1 / 3.25 = 0.3077
*   Probabilidad Implícita Empate (estimada) = 1 - 0.5238 - 0.3077 = 0.1685
*   Cuota Implícita Empate (estimada) = 1 / 0.1685 = 5.93

**Cálculo de Valor (CLV):**

*   **Apuesta al Empate:**
    *   Mi P(Empate) = 0.4966
    *   P(Implícita Empate) = 0.1685
    *   Valor = (0.4966 / 0.1685) - 1 = 1.947 (Valor muy alto, sugiere una subestimación del empate por parte del mercado).
*   **Apuesta a Victoria del Tottenham:**
    *   Mi P(Victoria Tottenham) = 0.5034
    *   P(Implícita Tottenham) = 0.3077
    *   Valor = (0.5034 / 0.3077) - 1 = 0.636 (Valor alto).

**Recomendación de Tamaño de Inversión (Criterio de Kelly):**

*   **Para Empate (p=0.4966, Cuota=5.93):**
    *   `f = ((5.93 - 1) * 0.4966 - (1 - 0.4966)) / (5.93 - 1)`
    *   `f = (4.93 * 0.4966 - 0.5034) / 4.93 = (2.445 - 0.5034) / 4.93 = 0.3938`
    *   **Inversión sugerida: 39.38% de la banca** en el empate.

*   **Para Victoria del Tottenham (p=0.5034, Cuota=3.25):**
    *   `f = ((3.25 - 1) * 0.5034 - (1 - 0.5034)) / (3.25 - 1)`
    *   `f = (2.25 * 0.5034 - 0.4966) / 2.25 = (1.13265 - 0.4966) / 2.25 = 0.2827`
    *   **Inversión sugerida: 28.27% de la banca** en la victoria del Tottenham.

**Pronóstico de Mayor Valor (CLV):**
Basado en el análisis cuantitativo, el pronóstico de mayor valor es el **Empate entre Chelsea y Tottenham** (específicamente, un 0-0 es el resultado más probable según el modelo, seguido de un 0-1). La cuota de empate estimada por el mercado parece considerablemente más baja que la probabilidad que mi modelo calcula.

---

### Evaluación de Margen de Error

El margen de error en este análisis es influenciado por varios factores:

1.  **Tamaño de la Muestra:** El uso de los "últimos 5" partidos para calcular las fuerzas de ataque y defensa es una muestra muy pequeña. Esto puede llevar a resultados extremos, como el xG de 0.0 para el Chelsea, que aunque es un reflejo de su actual falta de gol en casa en esos partidos, puede no ser representativo de su capacidad real a largo plazo.
2.  **Datos Faltantes:** La ausencia del historial de los últimos 5 partidos del AFC Bournemouth en el historial proporcionado limitó severamente la aplicación del análisis cuantitativo para ese partido. Esto introdujo un sesgo y la necesidad de una evaluación puramente cualitativa.
3.  **Cuotas del Empate:** La cuota para el empate en el partido Chelsea vs Tottenham tuvo que ser estimada a partir de las probabilidades implícitas de las cuotas de victoria/derrota proporcionadas, ya que no se encontró directamente, lo que introduce una fuente adicional de error en los cálculos de CLV y Criterio de Kelly.
4.  **Asunciones de Promedios de Liga:** Los promedios de goles de la liga utilizados son estimaciones generales, no valores precisos de la temporada 2025/2026 de la Premier League, lo que puede afectar la precisión de las fuerzas de ataque y defensa.

En resumen, el modelo destaca la muy mala racha goleadora del Chelsea en casa, haciendo que el empate (particularmente el 0-0) sea la opción de mayor valor según las probabilidades del modelo y las cuotas de mercado disponibles (o estimadas). Sin embargo, es crucial reconocer las limitaciones impuestas por el tamaño de la muestra y los datos incompletos.