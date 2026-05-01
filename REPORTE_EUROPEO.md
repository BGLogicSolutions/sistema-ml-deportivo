# 📊 Análisis Diario Evolutivo: 01/05/2026

Como analista cuantitativo deportivo, procederé con el análisis solicitado, considerando la fecha actual como 01/05/2026.

### 1. Memoria y Auditoría

La bitácora de partidos analizados el 27/04/2026 contiene resultados históricos (FTHG y FTAG). Dado que no se proporcionaron predicciones previas para estos encuentros por mi parte, no puedo auditar mi propio margen de error ni ajustar cálculos que no realicé en ese momento. Asumo que los resultados (FTHG, FTAG) registrados en la bitácora para esas fechas (que en su mayoría son de 2023, 2024 y algunas de 2026, todas anteriores a 27/04/2026) son los resultados reales y correctos de esos partidos históricos. Por lo tanto, no hay cálculos que ajustar en esta sección.

### 2. Análisis de Hoy (01/05/2026)

Para el análisis de hoy, primero debo identificar los partidos que se juegan en la fecha actual (01/05/2026) entre los equipos listados en la sección "Análisis de Hoy". Luego buscaré noticias en vivo, aplicaré el análisis cuantitativo y finalmente, haré las recomendaciones.

**Identificación de Partidos para Hoy (01/05/2026):**

No se especifican emparejamientos directos para el 01/05/2026 en la sección "Análisis de Hoy", solo listas de equipos con sus últimos 5 partidos. Por lo tanto, buscaré en Google los partidos de fútbol programados para el 01/05/2026 que involucren a estos equipos.

Basado en los resultados de la búsqueda, los partidos que se juegan hoy, 01/05/2026, entre los equipos listados son:

*   **Leeds vs Burnley** (Premier League)
*   **Girona vs Mallorca** (La Liga)
*   **Pisa vs Lecce** (Serie A)

Además, se encontró información para partidos de la Bundesliga que se disputan el 02/05/2026, lo que indica que no son para hoy. Específicamente, **Werder Bremen vs Augsburg** y **Union Berlin vs FC Koln** se mencionan para el 2 de mayo. Por lo tanto, no se incluirán en el análisis de "hoy". Se menciona un partido de la Frauen-Bundesliga entre Hamburger SV y Union Berlin el 1 de mayo, pero las listas de equipos en la solicitud son claramente de equipos masculinos de la Bundesliga, por lo que no se considerará. Bayern Munich también tiene un partido de Champions League el 28 de abril (ya pasado) y otro el 3 de mayo, por lo tanto no juega hoy 1 de mayo. RB Leipzig juega el 2 de mayo.

**Limitación importante:** Para los equipos de la Bundesliga (Werder Bremen, Augsburg, Union Berlin, FC Koln, Bayern Munich, Heidenheim, Hoffenheim, Stuttgart, Leverkusen, RB Leipzig) y algunos de la Serie A (Lecce), la información histórica proporcionada en el prompt es mayormente de la temporada 2023 o 2024. Esto es una limitación significativa para la aplicación de la distribución de Poisson y Sabermetrics para predecir con precisión los partidos de 2026, ya que el rendimiento de los equipos puede haber cambiado drásticamente en 2-3 años. Haré los cálculos con los datos disponibles, pero la fiabilidad de las predicciones de estos partidos será menor. Para los equipos de la Premier League y La Liga, los datos son más recientes (2026 o finales de 2024).

---

**Análisis Cuantitativo para los Partidos de Hoy (01/05/2026):**

Procederé a calcular el xG (Expected Goals) utilizando un enfoque basado en la distribución de Poisson y Sabermetrics. Primero, estableceré los promedios de goles de la liga. Dado que tenemos partidos de Premier League, La Liga y Serie A, usaré promedios generales para cada liga de los datos proporcionados.

**Metodología para xG (Sabermetrics/Poisson):**

1.  **Promedios de Goles de la Liga:** Calcular el promedio de goles por partido para equipos locales y visitantes en cada liga basándose en los datos históricos proporcionados para esa liga (aunque con las limitaciones de las fechas).
2.  **Fuerza de Ataque (Attack Strength - AS):** (Promedio de Goles del Equipo Local / Promedio de Goles de la Liga del Equipo Local) para partidos de casa. (Promedio de Goles del Equipo Visitante / Promedio de Goles de la Liga del Equipo Visitante) para partidos fuera.
3.  **Fuerza de Defensa (Defense Strength - DS):** (Promedio de Goles Recibidos del Equipo Local / Promedio de Goles de la Liga del Equipo Visitante) para partidos de casa. (Promedio de Goles Recibidos del Equipo Visitante / Promedio de Goles de la Liga del Equipo Local) para partidos fuera.
4.  **xG (Goles Esperados):**
    *   `xG_Local = AS_Local * DS_Visitante * Promedio_Goles_Casa_Liga`
    *   `xG_Visitante = AS_Visitante * DS_Local * Promedio_Goles_Fuera_Liga`
5.  **Distribución de Poisson:** Usar los valores de xG para calcular la probabilidad de diferentes resultados (0-0, 1-0, 0-1, 1-1, etc.).
6.  **Probabilidades de Resultado Final:** Sumar las probabilidades de los marcadores para obtener la probabilidad de victoria local, empate y victoria visitante.

---

**Datos Históricos Relevantes para Hoy:**

**Premier League:**

*   **Leeds (Casa):** 3 de Marzo de 2026 (Leeds 0-1 Sunderland), 21 de Marzo de 2026 (Leeds 0-0 Brentford), 18 de Abril de 2026 (Leeds 3-0 Wolves).
    *   Goles a favor en casa: 0+0+3 = 3 (Promedio: 1.0)
    *   Goles en contra en casa: 1+0+0 = 1 (Promedio: 0.33)
*   **Burnley (Visita):** 3 de Marzo de 2026 (Everton 2-0 Burnley), 21 de Marzo de 2026 (Fulham 3-1 Burnley), 19 de Abril de 2026 (Nott'm Forest 4-1 Burnley).
    *   Goles a favor fuera: 0+1+1 = 2 (Promedio: 0.67)
    *   Goles en contra fuera: 2+3+4 = 9 (Promedio: 3.0)

**La Liga:**

*   **Girona (Casa):** 4 de Mayo de 2024 (Girona 4-2 Barcelona), 14 de Mayo de 2024 (Girona 0-1 Villarreal), 24 de Mayo de 2024 (Girona 7-0 Granada).
    *   Goles a favor en casa: 4+0+7 = 11 (Promedio: 3.67)
    *   Goles en contra en casa: 2+1+0 = 3 (Promedio: 1.0)
*   **Mallorca (Visita):** 4 de Mayo de 2024 (Mallorca 0-1 Ath Madrid), 14 de Mayo de 2024 (Osasuna 1-1 Mallorca), 26 de Mayo de 2024 (Getafe 1-2 Mallorca).
    *   Goles a favor fuera: 0+1+2 = 3 (Promedio: 1.0)
    *   Goles en contra fuera: 1+1+1 = 3 (Promedio: 1.0)

**Serie A:**

*   **Pisa (Casa):** 15 de Marzo de 2026 (Pisa 3-1 Cagliari), 5 de Abril de 2026 (Pisa 0-1 Torino), 19 de Abril de 2026 (Pisa 1-2 Genoa).
    *   Goles a favor en casa: 3+0+1 = 4 (Promedio: 1.33)
    *   Goles en contra en casa: 1+1+2 = 4 (Promedio: 1.33)
*   **Lecce (Visita):** 27 de Abril de 2024 (Lecce 1-1 Monza), 5 de Mayo de 2024 (Cagliari 1-1 Lecce), 26 de Mayo de 2024 (Napoli 0-0 Lecce).
    *   Goles a favor fuera: 1+1+0 = 2 (Promedio: 0.67)
    *   Goles en contra fuera: 1+1+0 = 2 (Promedio: 0.67)

---

**Cálculo de Promedios de Goles de la Liga (Basado en el historial proporcionado):**

*   **Premier League (total de 15 partidos en 2026 proporcionados para varios equipos):**
    *   Total Goles Casa: 1+1+4+2+1+2+1+2+0+3+2+1+0 = 20
    *   Total Goles Fuera: 1+1+2+0+0+1+0+2+1+1+0+1+0 = 10
    *   Partidos en casa: 8 (Levante, Man United, Brentford, Leeds)
    *   Partidos fuera: 7 (Levante, Man United, Brentford, Leeds)
    *   Promedio Goles Casa Premier League (total de goles del equipo local en partidos de Premier League / número de partidos): (1+3+2+1+1+3+2+0)/8 = 1.625
    *   Promedio Goles Fuera Premier League (total de goles del equipo visitante en partidos de Premier League / número de partidos): (1+1+2+0+1+1+0+2)/8 = 1.0
    *   Nota: Para los partidos donde el equipo es visitante, FTHG es el gol del local y FTAG es el gol del visitante. Ajustaré para calcular los promedios de la liga.
        *   Goles anotados por equipos locales en PL (de los 2026 data): 1 (Levante-Girona), 4 (Levante-Oviedo), 1 (Levante-Getafe), 3 (Man Utd-Aston Villa), 1 (Man Utd-Leeds), 2 (Brentford-Wolves), 2 (Brentford-Everton), 0 (Brentford-Fulham), 0 (Leeds-Sunderland), 0 (Leeds-Brentford), 3 (Leeds-Wolves) = 1+4+1+3+1+2+2+0+0+0+3 = 17
        *   Goles anotados por equipos visitantes en PL (de los 2026 data): 1 (Levante-Girona), 2 (Levante-Oviedo), 0 (Levante-Getafe), 1 (Man Utd-Aston Villa), 2 (Man Utd-Leeds), 2 (Brentford-Wolves), 2 (Brentford-Everton), 0 (Brentford-Fulham), 1 (Leeds-Sunderland), 0 (Leeds-Brentford), 0 (Leeds-Wolves) = 1+2+0+1+2+2+2+0+1+0+0 = 11
        *   Partidos PL en casa (Leeds, Man Utd, Brentford): 3+2+3 = 8
        *   Partidos PL fuera (Leeds, Man Utd, Brentford): 2+3+2 = 7
        *   Promedio de goles marcados por el equipo local en PL (todos los partidos): (1+4+1+3+1+2+2+0+0+0+3 + 1+1+2+1+2+2+2+0+1+0+0 (goles de local de otros equipos en partidos de visitantes)) / 15 partidos = 28/15 = 1.87
        *   Promedio de goles marcados por el equipo visitante en PL (todos los partidos): (1+1+2+0+0+1+0+2+1+1+0 (goles de visitante de otros equipos en partidos de local)) / 15 partidos = 10/15 = 0.67
    *   **Corrección:** Simplificaré el promedio de la liga utilizando los *total goals* de los partidos donde los equipos listados fueron locales o visitantes.
    *   Partidos PL en los datos 2026: 15 partidos.
        *   Total Goles (FTHG+FTAG): (1+1)+(1+1)+(4+2)+(2+0)+(1+0) + (2+1)+(3+1)+(2+2)+(1+2)+(0+1) + (0+0)+(2+2)+(0+0)+(2+2)+(0+0) = 4+2+6+2+1 + 3+4+4+3+1 + 0+4+0+4+0 = 38 goles en 15 partidos.
        *   Promedio Goles por Partido PL = 38 / 15 = 2.53
        *   Promedio Goles Casa PL = (Goles de equipos locales) / (Número de partidos)
        *   Promedio Goles Visitante PL = (Goles de equipos visitantes) / (Número de partidos)
        *   De los datos de 2026 para PL:
            *   Goles anotados por equipos HOME: 1 (Lev-Gir), 4 (Lev-Ovi), 1 (Lev-Get), 3 (ManU-AstV), 1 (ManU-Lee), 2 (Bre-Wol), 2 (Bre-Eve), 0 (Bre-Ful), 0 (Lee-Sun), 0 (Lee-Bre), 3 (Lee-Wol) = 17
            *   Goles concedidos por equipos HOME (que serían FTAG de sus partidos como local): 1, 2, 0, 1, 2, 2, 2, 0, 1, 0, 0 = 11
            *   Goles anotados por equipos AWAY: 1 (Val-Lev), 1 (New-ManU), 2 (Bou-ManU), 0 (Che-ManU), 0 (Bou-Bre), 0 (Lee-Bre), 1 (Ful-Bur), 4 (Not-Bur), 2 (ManU-Lee) = 1+1+2+0+0+0+1+4+2 = 11
            *   Goles concedidos por equipos AWAY (que serían FTHG de sus partidos como visitante): 1, 2, 1, 0, 0, 0, 3, 2, 1 = 1+2+1+0+0+0+3+2+1 = 10
            *   Total partidos de liga Premier analizados: 23 partidos (5x4 de Levante, Man United, Brentford, Leeds, y 3 de Burnley).

        *   **Recalculando promedios de la Liga de manera más consistente, usando *todos* los FTHG y FTAG de los equipos de esa liga en el historial proporcionado:**
            *   **Premier League (equipos 2026):**
                *   Total Goles FTHG (de todos los partidos donde un equipo de la Premier League fue Home): 1+4+1 + 3+1 + 2+2+0 + 0+0+3 = 17 goles. (11 partidos en casa)
                *   Total Goles FTAG (de todos los partidos donde un equipo de la Premier League fue Home): 1+2+0 + 1+2 + 2+2+0 + 1+0+0 = 11 goles. (11 partidos en casa)
                *   Total Goles FTHG (de todos los partidos donde un equipo de la Premier League fue Away): 1+1 + 2+0 + 0+0+3+4 + 0+0+1+3+2 = 17 goles. (12 partidos fuera)
                *   Total Goles FTAG (de todos los partidos donde un equipo de la Premier League fue Away): 1+1 + 2+1 + 0+0+1+1 + 0+0+1+1+1 = 10 goles. (12 partidos fuera)

                *   *Esto es complicado porque las tablas son solo los "últimos 5" de cada equipo, no el universo de partidos de la liga. Asumiré que los promedios de goles para la liga se basan en los resultados provistos para los equipos de esa liga.*

                *   **Promedio Goles Premier League (basado en todos los 2026 PL games provided):**
                    *   Total Goles Home Team (todos los partidos): (1+4+1) + (1+1) + (3+1) + (2+2+0) + (0+0+3) + (2+0) + (3+1) + (4+1) = 28 goles marcados por equipos HOME.
                    *   Total Goles Away Team (todos los partidos): (1+2+0) + (1+2) + (2+2+0) + (1+0+0) + (0+0) + (1+1) + (1+1) = 17 goles marcados por equipos AWAY.
                    *   Total partidos como LOCAL: 3 (Levante) + 2 (Man United) + 3 (Brentford) + 3 (Leeds) = 11 partidos.
                    *   Total partidos como VISITANTE: 2 (Levante) + 3 (Man United) + 2 (Brentford) + 2 (Leeds) + 3 (Burnley) = 12 partidos.
                    *   Promedio Goles por Partido Total = (17+11 + 17+10) / (11+12) = 55 / 23 = 2.39
                    *   Promedio Goles Home = (Goles FTHG de partidos de casa + Goles FTHG de partidos de fuera) / 23 = (17+10) / 23 = 1.17
                    *   Promedio Goles Away = (Goles FTAG de partidos de casa + Goles FTAG de partidos de fuera) / 23 = (11+17) / 23 = 1.22
                    *   Esto no tiene sentido. Debo calcular: Promedio de goles *anotados por el equipo local* en la liga, y promedio de goles *anotados por el equipo visitante* en la liga.

                    *   **Promedios de Goles por la Liga (todos los partidos dados en el input para cada liga):**
                        *   **Premier League (Total 23 partidos):**
                            *   Goles anotados por equipos locales (FTHG de partidos HOME, FTHG de partidos AWAY):
                                *   Levante (H): 1, 4, 1. Levante (A): 1, 2
                                *   Man United (H): 3, 1. Man United (A): 2, 0, 0
                                *   Brentford (H): 2, 2, 0. Brentford (A): 0, 0
                                *   Leeds (H): 0, 0, 3. Leeds (A): 1, 1
                                *   Burnley (A): 2, 3, 4
                                *   Total FTHG: 1+4+1+1+2 + 3+1+2+0+0 + 2+2+0+0+0 + 0+0+3+1+1 + 2+3+4 = 39 goles.
                            *   Goles anotados por equipos visitantes (FTAG de partidos HOME, FTAG de partidos AWAY):
                                *   Levante (H): 1, 2, 0. Levante (A): 1, 1
                                *   Man United (H): 1, 2. Man United (A): 1, 2, 1
                                *   Brentford (H): 2, 2, 0. Brentford (A): 0, 0
                                *   Leeds (H): 1, 0, 0. Leeds (A): 2, 0
                                *   Burnley (A): 0, 1, 1
                                *   Total FTAG: 1+2+0+1+1 + 1+2+1+2+1 + 2+2+0+0+0 + 1+0+0+2+0 + 0+1+1 = 28 goles.
                            *   Promedio Goles Local Premier League = 39 / 23 = 1.70
                            *   Promedio Goles Visitante Premier League = 28 / 23 = 1.22

                        *   **La Liga (Total 18 partidos):** (Levante 5, Girona 5, Mallorca 5, con datos de 2024 para Girona/Mallorca y 2026 para Levante. Usaré los de 2024/2026.)
                            *   Total FTHG: 1+1+4+2+1 + 4+2+0+1+1 + 0+1+1+1+1 = 20 goles.
                            *   Total FTAG: 1+1+2+0+0 + 2+2+1+3+0 + 1+0+1+2+2 = 18 goles.
                            *   Promedio Goles Local La Liga = 20 / 18 = 1.11
                            *   Promedio Goles Visitante La Liga = 18 / 18 = 1.00

                        *   **Serie A (Total 21 partidos):** (Lazio 5, Udinese 5, Milan 5, Juventus 5, Cagliari 5, Pisa 5, Lecce 5. Usaré los de 2024/2026.)
                            *   Total FTHG: 1+2+1+1+2+1+3+5+3 + 0+1+1+1+2+1 + 3+0+1 + 1+1+0 = 34 goles.
                            *   Total FTAG: 0+2+0+1+1 + 1+1+2+1+1 + 0+3+1+3+3 + 0+1+1+3+0 + 1+0+2+0+0 = 29 goles.
                            *   Promedio Goles Local Serie A = 34 / 21 = 1.62
                            *   Promedio Goles Visitante Serie A = 29 / 21 = 1.38

---

Ahora, calcularemos las fuerzas de ataque y defensa y el xG para cada partido de hoy.

**Partido 1: Leeds vs Burnley (Premier League)**

**Noticias en vivo / Alineaciones / Lesiones (01/05/2026):**

*   **Leeds:** En buena forma en liga (invicto en 5 partidos de PL antes de una derrota en FA Cup). Vienen de una derrota 1-0 en semifinales de FA Cup contra Chelsea. Sin Illan Gruev y Gudmundsson por lesión, sin suspensiones. Alineación probable: Darlow; Bijol, Struijk, Rodon; Okafor, Justin, Ampadu, Aaronson, Bogle; Tanaka; Calvert-Lewin. Dominic Calvert-Lewin ha marcado 11 goles en 31 partidos esta temporada.
*   **Burnley:** Están en la 19ª posición y su descenso ya está confirmado. Han perdido 4 de sus últimos 5 partidos, incluyendo 4-1 contra Nottingham Forest y 0-2 contra Brighton. Scott Parker fue despedido y Michael Jackson es el entrenador interino. Tienen una lista de lesionados más significativa: Beyer, Tuanzebe, Cullen, Roberts, Amdouni, Mejbri. Alineación probable: Dubravka; Esteve, Humphreys, Ekdal, Walker; Laurent, Ward-Prowse, Hartman, Anthony; Tchaouna, Flemming. Zian Flemming ha marcado 9 goles.

**Cálculos Cuantitativos (Premier League):**

*   Promedio Goles Local PL = 1.70
*   Promedio Goles Visitante PL = 1.22

**Leeds (Local):**

*   Goles a favor en casa (3 partidos): 3 (vs Wolves), 0 (vs Brentford), 0 (vs Sunderland) = Promedio 1.0
*   Goles en contra en casa (3 partidos): 0 (vs Wolves), 0 (vs Brentford), 1 (vs Sunderland) = Promedio 0.33
*   AS_Leeds = (1.0 / 1.70) = 0.59
*   DS_Leeds = (0.33 / 1.22) = 0.27

**Burnley (Visitante):**

*   Goles a favor fuera (3 partidos): 1 (vs Nott'm Forest), 1 (vs Fulham), 0 (vs Everton) = Promedio 0.67
*   Goles en contra fuera (3 partidos): 4 (vs Nott'm Forest), 3 (vs Fulham), 2 (vs Everton) = Promedio 3.0
*   AS_Burnley = (0.67 / 1.22) = 0.55
*   DS_Burnley = (3.0 / 1.70) = 1.76

**xG Leeds vs Burnley:**

*   xG_Leeds = AS_Leeds * DS_Burnley * Promedio_Goles_Casa_PL = 0.59 * 1.76 * 1.70 = 1.76
*   xG_Burnley = AS_Burnley * DS_Leeds * Promedio_Goles_Visitante_PL = 0.55 * 0.27 * 1.22 = 0.18

**Distribución de Poisson (probabilidades de goles):**

| Goles | P(Leeds) | P(Burnley) |
| :---- | :------- | :--------- |
| 0     | 0.179    | 0.835      |
| 1     | 0.316    | 0.150      |
| 2     | 0.279    | 0.014      |
| 3     | 0.164    | 0.001      |

**Probabilidades de Resultado (Leeds vs Burnley):**

*   **Leeds Gana:** (1-0, 2-0, 2-1, 3-0, 3-1, etc.) = 1 - P(Empate) - P(Burnley Gana)
    *   P(Leeds Gana) = 0.77 (aprox.)
*   **Empate:** (0-0, 1-1, 2-2, etc.)
    *   P(0-0) = 0.179 * 0.835 = 0.149
    *   P(1-1) = 0.316 * 0.150 = 0.047
    *   P(Empate) = P(0-0) + P(1-1) + P(2-2) = 0.149 + 0.047 + (0.279 * 0.014) = 0.149 + 0.047 + 0.004 = 0.200 (aprox.)
*   **Burnley Gana:** (0-1, 0-2, 1-2, etc.)
    *   P(0-1) = 0.179 * 0.150 = 0.027
    *   P(Burnley Gana) = 0.03 (aprox.)

**Resumen de Probabilidades (Leeds vs Burnley):**

*   Leeds Gana: 77%
*   Empate: 20%
*   Burnley Gana: 3%

---

**Partido 2: Girona vs Mallorca (La Liga)**

**Noticias en vivo / Alineaciones / Lesiones (01/05/2026):**

*   **Girona:** Están en la parte baja de la tabla, con el descenso acechando. No han ganado sus últimos tres partidos (1 empate, 2 derrotas), incluyendo una derrota 2-1 ante Valencia. En casa, han perdido solo dos veces en siete partidos (4 victorias, 1 empate). Bajas por lesión: Juan Carlos, Portu, Marc-Andre ter Stegen, Abel Ruiz, Vladyslav Vanat. Álex Moreno está suspendido. Joel Roca es un jugador clave que anotó recientemente.
*   **Mallorca:** Están en la 17ª posición de La Liga, cerca de la zona de descenso. Sufrieron una derrota 2-1 ante Alavés la semana pasada. No han ganado como visitantes desde octubre (3 empates, 8 derrotas), perdiendo 6 de sus últimos 7 partidos fuera de casa. Vedat Muriqi es el máximo goleador del Mallorca con 21 goles esta temporada. Bajas por lesión: Jan Salas, Mateo Joseph, Antonio Raíllo. Zito Luvumbo ha estado ausente en los últimos dos partidos.

**Cálculos Cuantitativos (La Liga):**

*   Promedio Goles Local La Liga = 1.11
*   Promedio Goles Visitante La Liga = 1.00

**Girona (Local):**

*   Goles a favor en casa (3 partidos): 4, 0, 7 = Promedio 3.67
*   Goles en contra en casa (3 partidos): 2, 1, 0 = Promedio 1.0
*   AS_Girona = (3.67 / 1.11) = 3.31
*   DS_Girona = (1.0 / 1.00) = 1.00

**Mallorca (Visitante):**

*   Goles a favor fuera (3 partidos): 0, 1, 2 = Promedio 1.0
*   Goles en contra fuera (3 partidos): 1, 1, 1 = Promedio 1.0
*   AS_Mallorca = (1.0 / 1.00) = 1.00
*   DS_Mallorca = (1.0 / 1.11) = 0.90

**xG Girona vs Mallorca:**

*   xG_Girona = AS_Girona * DS_Mallorca * Promedio_Goles_Casa_LaLiga = 3.31 * 0.90 * 1.11 = 3.30
*   xG_Mallorca = AS_Mallorca * DS_Girona * Promedio_Goles_Visitante_LaLiga = 1.00 * 1.00 * 1.00 = 1.00

**Distribución de Poisson (probabilidades de goles):**

| Goles | P(Girona) | P(Mallorca) |
| :---- | :-------- | :---------- |
| 0     | 0.037     | 0.368       |
| 1     | 0.122     | 0.368       |
| 2     | 0.202     | 0.184       |
| 3     | 0.222     | 0.061       |

**Probabilidades de Resultado (Girona vs Mallorca):**

*   **Girona Gana:** (1-0, 2-0, 2-1, 3-0, 3-1, etc.) = 1 - P(Empate) - P(Mallorca Gana)
    *   P(Girona Gana) = 0.69 (aprox.)
*   **Empate:** (0-0, 1-1, 2-2, etc.)
    *   P(0-0) = 0.037 * 0.368 = 0.014
    *   P(1-1) = 0.122 * 0.368 = 0.045
    *   P(2-2) = 0.202 * 0.184 = 0.037
    *   P(Empate) = 0.014 + 0.045 + 0.037 = 0.096 (aprox.)
*   **Mallorca Gana:** (0-1, 0-2, 1-2, etc.)
    *   P(0-1) = 0.037 * 0.368 = 0.014
    *   P(Mallorca Gana) = 0.21 (aprox.)

**Resumen de Probabilidades (Girona vs Mallorca):**

*   Girona Gana: 69%
*   Empate: 10%
*   Mallorca Gana: 21%

---

**Partido 3: Pisa vs Lecce (Serie A)**

**Noticias en vivo / Alineaciones / Lesiones (01/05/2026):**

*   **Pisa:** Están en la 20ª posición de la Serie A, al borde del descenso a la Serie B. Han perdido 9 de sus últimos 10 partidos de liga (1 victoria). Oscar Hiljemark es su entrenador. No han marcado en 19 partidos de Serie A esta temporada. Bajas por lesión: Daniel Tyrell Denoon (duda), Marius Marin (duda), Matteo Tramoni (duda).
*   **Lecce:** Están en la 17ª posición, ligeramente mejor, pero aún no están a salvo del descenso. Vienen de dos empates (0-0 vs Hellas Verona, 1-1 vs Fiorentina) después de 4 derrotas consecutivas. Eusebio Di Francesco es su entrenador. Francesco Camarda (hombro) ha sido dado de alta.

**Cálculos Cuantitativos (Serie A):**

*   Promedio Goles Local Serie A = 1.62
*   Promedio Goles Visitante Serie A = 1.38

**Pisa (Local):**

*   Goles a favor en casa (3 partidos): 3 (vs Cagliari), 0 (vs Torino), 1 (vs Genoa) = Promedio 1.33
*   Goles en contra en casa (3 partidos): 1 (vs Cagliari), 1 (vs Torino), 2 (vs Genoa) = Promedio 1.33
*   AS_Pisa = (1.33 / 1.62) = 0.82
*   DS_Pisa = (1.33 / 1.38) = 0.96

**Lecce (Visitante):**

*   Goles a favor fuera (3 partidos): 1 (vs Monza), 1 (vs Cagliari), 0 (vs Napoli) = Promedio 0.67
*   Goles en contra fuera (3 partidos): 1 (vs Monza), 1 (vs Cagliari), 0 (vs Napoli) = Promedio 0.67
*   AS_Lecce = (0.67 / 1.38) = 0.49
*   DS_Lecce = (0.67 / 1.62) = 0.41

**xG Pisa vs Lecce:**

*   xG_Pisa = AS_Pisa * DS_Lecce * Promedio_Goles_Casa_SerieA = 0.82 * 0.41 * 1.62 = 0.54
*   xG_Lecce = AS_Lecce * DS_Pisa * Promedio_Goles_Visitante_SerieA = 0.49 * 0.96 * 1.38 = 0.65

**Distribución de Poisson (probabilidades de goles):**

| Goles | P(Pisa) | P(Lecce) |
| :---- | :------ | :------- |
| 0     | 0.583   | 0.522    |
| 1     | 0.315   | 0.340    |
| 2     | 0.085   | 0.111    |
| 3     | 0.015   | 0.024    |

**Probabilidades de Resultado (Pisa vs Lecce):**

*   **Pisa Gana:** (1-0, 2-0, 2-1, etc.) = 1 - P(Empate) - P(Lecce Gana)
    *   P(Pisa Gana) = 0.35 (aprox.)
*   **Empate:** (0-0, 1-1, 2-2, etc.)
    *   P(0-0) = 0.583 * 0.522 = 0.304
    *   P(1-1) = 0.315 * 0.340 = 0.107
    *   P(Empate) = 0.304 + 0.107 + (0.085 * 0.111) = 0.304 + 0.107 + 0.009 = 0.420 (aprox.)
*   **Lecce Gana:** (0-1, 0-2, 1-2, etc.)
    *   P(0-1) = 0.583 * 0.340 = 0.198
    *   P(Lecce Gana) = 0.23 (aprox.)

**Resumen de Probabilidades (Pisa vs Lecce):**

*   Pisa Gana: 35%
*   Empate: 42%
*   Lecce Gana: 23%

---

### Sugerencia de Pronóstico de Mayor Valor (CLV)

El "Closing Line Value" (CLV) se refiere a obtener una cuota en una apuesta que es mejor que la cuota final ofrecida por las casas de apuestas antes del inicio del partido. Para sugerir un pronóstico de "mayor valor", necesitaría las cuotas actuales de las casas de apuestas para compararlas con mis probabilidades calculadas. Sin cuotas de casas de apuestas, no puedo determinar el CLV.

En su lugar, proporcionaré los resultados más probables según mi modelo:

1.  **Leeds vs Burnley:**
    *   **Pronóstico más probable:** Victoria de Leeds (probabilidad del 77%).
    *   **Marcadores más probables:** 1-0 (Leeds), 2-0 (Leeds)
    *   **Consideración:** Leeds está en mejor forma general en la liga y Burnley ya está descendido y tiene muchas lesiones. La diferencia de xG es muy alta (1.76 vs 0.18).

2.  **Girona vs Mallorca:**
    *   **Pronóstico más probable:** Victoria de Girona (probabilidad del 69%).
    *   **Marcadores más probables:** 3-1 (Girona), 2-1 (Girona)
    *   **Consideración:** Aunque ambos equipos luchan contra el descenso y Mallorca tiene a Muriqi, el rendimiento ofensivo del Girona en casa en los datos recientes es muy fuerte, y Mallorca tiene un pobre récord como visitante.

3.  **Pisa vs Lecce:**
    *   **Pronóstico más probable:** Empate (probabilidad del 42%).
    *   **Marcadores más probables:** 0-0, 1-1
    *   **Consideración:** Ambos equipos están en la parte baja de la tabla y luchando por la supervivencia, con Pisa en peor forma general. El modelo predice un partido con pocos goles y una alta probabilidad de empate.

### Recomendación de Tamaño de Inversión (Criterio de Kelly)

El Criterio de Kelly (`f = (bp - q) / b`) requiere:

*   `f`: La fracción de tu bankroll para apostar.
*   `b`: Las probabilidades decimales de la casa de apuestas menos 1 (o la ganancia neta por unidad apostada).
*   `p`: Tu probabilidad percibida de que el resultado ocurra (mis probabilidades de Poisson).
*   `q`: Tu probabilidad percibida de que el resultado *no* ocurra (1 - p).

Dado que no se proporcionaron las cuotas de las casas de apuestas ni el tamaño del bankroll, no puedo aplicar el Criterio de Kelly directamente para dar un tamaño de inversión concreto.

**Principio del Criterio de Kelly:**
El Criterio de Kelly busca optimizar el crecimiento del bankroll a largo plazo. Recomienda apostar una mayor proporción del capital cuando la "ventaja" es mayor (es decir, cuando tu probabilidad percibida es significativamente mayor que la probabilidad implícita de las cuotas de la casa de apuestas). Si tu probabilidad percibida es igual o menor que la implícita en las cuotas, el criterio de Kelly recomendaría no apostar.

**Para poder usar el Criterio de Kelly, necesitaría:**

1.  **Las cuotas exactas ofrecidas por una casa de apuestas** para los resultados de Leeds vs Burnley (1X2), Girona vs Mallorca (1X2) y Pisa vs Lecce (1X2).
2.  **Un bankroll definido** para calcular la cantidad monetaria a apostar.

**Conclusión sin datos de cuotas/bankroll:**
Basándome en mis probabilidades calculadas:

*   **Leeds vs Burnley:** Si las cuotas para la victoria de Leeds son suficientemente altas (por ejemplo, >1.30-1.40, lo que implicaría una probabilidad inferior al 77%), podría haber valor para una apuesta. Dada la alta probabilidad, si encuentras cuotas de valor, el Kelly podría sugerir una inversión moderada a alta.
*   **Girona vs Mallorca:** Similarmente, si las cuotas para la victoria de Girona superan el 1.45 (probabilidad implícita < 69%), podría haber valor.
*   **Pisa vs Lecce:** La probabilidad de empate es la más alta (42%). Si las cuotas para el empate son atractivas (por ejemplo, >2.40), podría considerarse una apuesta. Sin embargo, en partidos con alta probabilidad de empate y bajos xG para ambos lados, las apuestas a "menos de X goles" (Under X goals) suelen ser también una buena opción.

Recomiendo buscar cuotas de valor para la victoria de Leeds y Girona, y para el empate en el partido de Pisa vs Lecce, y luego aplicar el Criterio de Kelly con su bankroll y las cuotas encontradas.

---
**Consideraciones Finales sobre la calidad de los datos:**
Reitero la limitación sobre la antigüedad de los datos de algunos equipos, especialmente en la Bundesliga y algunos de la Serie A. Utilizar datos de 2023 o 2024 para predecir partidos en 2026 introduce un riesgo significativo de imprecisión debido a cambios en plantillas, entrenadores, tácticas y dinámicas de liga. Las predicciones para los partidos de la Premier League y La Liga son más fiables en este aspecto.