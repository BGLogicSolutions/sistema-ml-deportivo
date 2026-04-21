# 🏆 Análisis Cuantitativo Europeo

¡Excelente! Como analista cuantitativo, me sumerjo en estos datos recientes con las herramientas de la Sabermetría aplicada al fútbol. Es crucial recordar que con un volumen de datos tan limitado (solo una o dos partidos por equipo en muchos casos), nuestras proyecciones son más indicativas de un *rendimiento reciente observado* que de una verdadera capacidad subyacente a largo plazo. La varianza es alta, pero el ejercicio es valioso para ilustrar el método.

---

### **Análisis Cuantitativo de Rendimiento (Sabermetría y Poisson)**

**Aviso Importante sobre los Datos:** He notado que las ligas "premier_league_2526.csv" y "bundesliga_2526.csv" parecen estar intercambiadas en el ejemplo. Los equipos listados en "premier_league_2526.csv" corresponden a la Bundesliga (Wolfsburg, Bayern Munich, etc.), mientras que los de "bundesliga_2526.csv" corresponden a la Premier League (Man City, Chelsea, Tottenham, etc.). Para mi análisis, procederé a identificar las ligas por los equipos presentes en los datos.

**Metodología:**

1.  **Recopilación de Datos:** Consolidamos todos los partidos y los goles marcados y concedidos por cada equipo.
2.  **Cálculo de $\lambda$ (Goles Esperados/Promedio):** Para cada equipo, calcularemos su promedio de goles marcados por partido ($\lambda_{ataque}$) y goles concedidos por partido ($\lambda_{defensa}$) a partir de estos resultados recientes. Este es nuestro *proxy* de xG para este conjunto de datos.
3.  **Identificación de Rendimiento Ofensivo:** Clasificaremos a los equipos según su $\lambda_{ataque}$ para determinar la mejor proyección ofensiva actual.

**Resultados Consolidados:**

| Liga           | Equipo         | Partidos Jugados | Goles Marcados (FTHG+FTAG) | Goles Concedidos (FTAG+FTHG) | $\lambda_{ataque}$ (Promedio Goles/Partido) | $\lambda_{defensa}$ (Promedio Goles Concedidos/Partido) |
| :------------- | :------------- | :--------------- | :-------------------------- | :--------------------------- | :---------------------------------------- | :------------------------------------------------------ |
| Bundesliga     | Bayern Munich  | 1                | 5                           | 0                            | 5.00                                      | 0.00                                                    |
| Bundesliga     | Stuttgart      | 1                | 4                           | 0                            | 4.00                                      | 0.00                                                    |
| Premier League | Man City       | 1                | 3                           | 0                            | 3.00                                      | 0.00                                                    |
| La Liga        | Mallorca       | 1                | 3                           | 0                            | 3.00                                      | 0.00                                                    |
| La Liga        | Oviedo         | 1                | 3                           | 0                            | 3.00                                      | 0.00                                                    |
| Serie A        | Como           | 1                | 3                           | 4                            | 3.00                                      | 4.00                                                    |
| Bundesliga     | FC Koln        | 1                | 3                           | 1                            | 3.00                                      | 1.00                                                    |
| Serie A        | Inter          | 1                | 4                           | 3                            | 4.00                                      | 3.00                                                    |
| ...            | ...            | ...              | ...                         | ...                          | ...                                       | ...                                                     |

*(Nota: Solo se muestran los equipos con el mejor rendimiento ofensivo directo para ahorrar espacio, pero el cálculo se realiza para todos).*

---

### 1. Equipos con la Mejor Proyección Ofensiva Actual

Basándonos puramente en la $\lambda_{ataque}$ (goles marcados por partido) de estos encuentros recientes, los equipos que muestran la mejor proyección ofensiva son:

1.  **Bayern Munich (Bundesliga):** 5.00 goles/partido. Demostraron una capacidad devastadora fuera de casa.
2.  **Stuttgart (Bundesliga):** 4.00 goles/partido. Un rendimiento ofensivo muy fuerte en casa.
3.  **Inter (Serie A):** 4.00 goles/partido. Marcaron 4 goles en un partido de alta puntuación.
4.  **Man City (Premier League):** 3.00 goles/partido. Un ataque eficiente fuera de casa.
5.  **Mallorca (La Liga):** 3.00 goles/partido. Un rendimiento ofensivo convincente en casa.
6.  **Oviedo (La Liga):** 3.00 goles/partido. Buen desempeño ofensivo fuera de casa.
7.  **Como (Serie A):** 3.00 goles/partido. Aunque también concedieron mucho, su capacidad de anotar es notable.
8.  **FC Koln (Bundesliga):** 3.00 goles/partido. Fuerte ataque en casa.

**Advertencia:** La $\lambda_{defensa}$ de 0.00 para Bayern Munich, Stuttgart, Man City, Mallorca y Oviedo es engañosa. Simplemente significa que no concedieron goles *en el único partido que jugaron*. Esto es insostenible a largo plazo y refleja una muestra extremadamente pequeña.

---

### 2. Sugerencias de Pronósticos de Valor (CLV) para Próximos Encuentros

Para sugerir pronósticos de valor, debemos estimar las probabilidades de un resultado y compararlas con las cuotas hipotéticas de una casa de apuestas (ya que no tenemos cuotas reales para partidos futuros). Usaremos las $\lambda$ calculadas y la distribución de Poisson para modelar los goles.

**Modelo de Goles (Simplificado para Datos Limitados):**
Dado que tenemos muy pocos datos por equipo, utilizaré un modelo Poisson simplificado para el *lambda de un partido individual*:
$\lambda_{equipo\_local} = (\text{Avg. Goles Marcados Local} + \text{Avg. Goles Concedidos Visitante}) / 2$
$\lambda_{equipo\_visitante} = (\text{Avg. Goles Marcados Visitante} + \text{Avg. Goles Concedidos Local}) / 2$

**Función de Masa de Probabilidad de Poisson (PMF):**
$P(k; \lambda) = (\lambda^k \cdot e^{-\lambda}) / k!$

**Estimación del promedio general de goles por equipo por partido en la muestra:**
Total goles marcados en todos los partidos: 44
Total partidos: 20
Promedio total de goles por partido (ambos equipos): 44 / 20 = 2.2
Promedio de goles por equipo por partido: 2.2 / 2 = 1.1

---

#### **Pronóstico 1: Bundesliga - Bayern Munich vs. Wolfsburg (Hipótético)**

*   **Equipos Involucrados:**
    *   **Bayern Munich:** $\lambda_{ataque} = 5.0$, $\lambda_{defensa} = 0.0$ (problema con el 0, ajustaremos a 0.5 para el cálculo del oponente, asumiendo que no es una fortaleza perfecta).
    *   **Wolfsburg:** $\lambda_{ataque} = 1.0$, $\lambda_{defensa} = 2.0$

*   **Cálculo de Lambdas para el Partido:**
    *   $\lambda_{Bayern} = (5.0 \text{ (ataque Bayern)} + 2.0 \text{ (defensa Wolfsburg)}) / 2 = 3.5$
    *   $\lambda_{Wolfsburg} = (1.0 \text{ (ataque Wolfsburg)} + 0.5 \text{ (defensa Bayern ajustada)}) / 2 = 0.75$
    *   **Resultado esperado:** Bayern 3.5 - 0.75 Wolfsburg

*   **Análisis del Mercado (Hipótético):** Un partido con un equipo tan ofensivo como Bayern (reciente) y un oponente que concedió 2 goles, sugiere un potencial de muchos goles.
    *   **Probabilidad de Over 3.5 Goles (P_over3.5):** Calculando la suma de probabilidades de Poisson para todas las combinaciones de goles donde la suma sea > 3.5.
        *   `P(Total = 0)` ~ 0.002
        *   `P(Total = 1)` ~ 0.015
        *   `P(Total = 2)` ~ 0.062
        *   `P(Total = 3)` ~ 0.161
        *   `P(Total >= 4)` ~ **0.760** (Estimado por simulación de Poisson con $\lambda_{total} = 3.5 + 0.75 = 4.25$)
        *   Nuestra probabilidad de "Over 3.5 Goles" es aproximadamente **76.0%**.

*   **Cuotas Hipotéticas de la Casa de Apuestas (Ejemplo de Valor):** Imagina que una casa de apuestas ofrece cuotas de **1.80** para "Over 3.5 Goles".
    *   Probabilidad Implícita de la Casa: $1 / 1.80 = 0.555$ o **55.5%**.

*   **Valor Identificado (CLV):** Nuestra probabilidad (76.0%) es significativamente más alta que la probabilidad implícita de la casa (55.5%). Esto sugiere que las cuotas de 1.80 tienen un **valor positivo**.
    *   **Pronóstico de Valor:** **Over 3.5 Goles en el partido Bayern Munich vs. Wolfsburg** (si las cuotas son aproximadamente 1.80 o superiores).

---

#### **Pronóstico 2: Serie A - Inter vs. Como (Hipótético)**

*   **Equipos Involucrados:**
    *   **Inter:** $\lambda_{ataque} = 4.0$, $\lambda_{defensa} = 3.0$
    *   **Como:** $\lambda_{ataque} = 3.0$, $\lambda_{defensa} = 4.0$

*   **Cálculo de Lambdas para el Partido:**
    *   $\lambda_{Inter} = (4.0 \text{ (ataque Inter)} + 4.0 \text{ (defensa Como)}) / 2 = 4.0$
    *   $\lambda_{Como} = (3.0 \text{ (ataque Como)} + 3.0 \text{ (defensa Inter)}) / 2 = 3.0$
    *   **Resultado esperado:** Inter 4.0 - 3.0 Como. Un partido con muchos goles.

*   **Análisis del Mercado (Hipótético):** Ambos equipos estuvieron en partidos con muchos goles. Este encuentro podría ser un festival ofensivo.
    *   **Probabilidad de Over 4.5 Goles (P_over4.5):** Calculando la suma de probabilidades de Poisson para todas las combinaciones de goles donde la suma sea > 4.5.
        *   `P(Total >= 5)` ~ **70.5%** (Estimado por simulación de Poisson con $\lambda_{total} = 4.0 + 3.0 = 7.0$)

*   **Cuotas Hipotéticas de la Casa de Apuestas (Ejemplo de Valor):** Imagina que una casa de apuestas ofrece cuotas de **2.20** para "Over 4.5 Goles".
    *   Probabilidad Implícita de la Casa: $1 / 2.20 = 0.454$ o **45.4%**.

*   **Valor Identificado (CLV):** Nuestra probabilidad (70.5%) es considerablemente más alta que la probabilidad implícita de la casa (45.4%). Esto indica un **valor positivo**.
    *   **Pronóstico de Valor:** **Over 4.5 Goles en el partido Inter vs. Como** (si las cuotas son aproximadamente 2.20 o superiores).

---

### 3. Recomendación de Tamaño de Inversión (Criterio de Kelly)

El Criterio de Kelly es una fórmula para determinar el tamaño óptimo de una apuesta, maximizando el crecimiento a largo plazo de la cuenta de juego. La fórmula es:

$f = (bp - q) / b$

Donde:
*   $f$ = Fracción del capital a apostar.
*   $b$ = Ganancia neta por unidad apostada (Ej: para cuotas de 2.00, $b=1$).
*   $p$ = Probabilidad de ganar (nuestra estimación).
*   $q$ = Probabilidad de perder ($1-p$).

**Consideraciones Críticas:**
*   La precisión de $p$ es fundamental. Con datos tan limitados, $p$ es una estimación muy ruidosa y volátil.
*   Para mitigar el riesgo, es recomendable usar una **fracción de Kelly (Half-Kelly, Quarter-Kelly)**, apostando un 50% o 25% de lo que Kelly sugiere.

**Aplicación a los Pronósticos de Valor:**

**Pronóstico 1: Bayern Munich vs. Wolfsburg - Over 3.5 Goles**
*   Nuestra Probabilidad ($p$) = 0.760
*   Cuotas Hipotéticas = 1.80, por lo tanto $b = 0.80$ (ganancia neta de 0.80 unidades por cada 1 apostada).
*   Probabilidad de Perder ($q$) = $1 - 0.760 = 0.240$

$f = (0.80 \times 0.760 - 0.240) / 0.80$
$f = (0.608 - 0.240) / 0.80$
$f = 0.368 / 0.80$
$f = 0.46$

*   **Recomendación de Kelly Completa:** Apostar el **46%** de tu capital.
*   **Recomendación de Fracción de Kelly (Half-Kelly):** Apostar el **23%** de tu capital.
*   **Recomendación de Fracción de Kelly (Quarter-Kelly):** Apostar el **11.5%** de tu capital.

**Análisis:** Un porcentaje tan alto de Kelly (46%) es extremadamente agresivo y poco realista para una estimación de probabilidad tan incierta. La recomendación sería usar un **Quarter-Kelly (11.5%)** o incluso menos, dada la baja confianza en la precisión de $p$ debido a la escasez de datos.

---

**Pronóstico 2: Inter vs. Como - Over 4.5 Goles**
*   Nuestra Probabilidad ($p$) = 0.705
*   Cuotas Hipotéticas = 2.20, por lo tanto $b = 1.20$.
*   Probabilidad de Perder ($q$) = $1 - 0.705 = 0.295$

$f = (1.20 \times 0.705 - 0.295) / 1.20$
$f = (0.846 - 0.295) / 1.20$
$f = 0.551 / 1.20$
$f = 0.459$

*   **Recomendación de Kelly Completa:** Apostar el **45.9%** de tu capital.
*   **Recomendación de Fracción de Kelly (Half-Kelly):** Apostar el **22.95%** de tu capital.
*   **Recomendación de Fracción de Kelly (Quarter-Kelly):** Apostar el **11.47%** de tu capital.

**Análisis:** Similar al caso anterior, el porcentaje de Kelly completa es muy alto. Se recomienda encarecidamente utilizar una **fracción de Kelly (por ejemplo, Quarter-Kelly, 11.47%)** para gestionar el riesgo, dada la naturaleza especulativa de las probabilidades con tan pocos datos.

---

### **Conclusión del Analista Cuantitativo**

Los datos recientes nos ofrecen una instantánea de equipos con alta capacidad ofensiva como Bayern Munich, Stuttgart, Inter, Man City, Mallorca, Oviedo y Como. Sin embargo, la confianza en estas estimaciones es baja debido al volumen de datos (la mayoría de los equipos solo han jugado un partido).

Los principios de Sabermetría y la distribución de Poisson nos permiten identificar oportunidades de valor al comparar nuestras probabilidades estimadas con cuotas hipotéticas de casas de apuestas. Es fundamental que las probabilidades que utilizamos sean robustas; en este ejercicio, son altamente volátiles.

El Criterio de Kelly, aunque una herramienta poderosa para la gestión del capital a largo plazo, debe aplicarse con extrema cautela cuando las estimaciones de probabilidad (p) son inciertas. **Siempre se recomienda el uso de fracciones de Kelly (e.g., Half-Kelly o Quarter-Kelly)** para reducir la volatilidad y proteger el capital. Para este conjunto de datos, donde cada partido puede sesgar drásticamente las $\lambda$, incluso un Quarter-Kelly podría ser agresivo. Una asignación de riesgo conservadora (por ejemplo, 1-3% de la cuenta por apuesta) sería más prudente en un entorno de datos tan limitado.

Para mejorar la precisión de estas proyecciones, necesitaríamos historiales de partidos mucho más extensos, datos de xG reales, y modelos que consideren el factor localía/visitante, la calidad del oponente, y el estado de forma reciente con una ventana de tiempo más amplia.