# Power BI storytelling model - Choose Your Side

Este documento convierte la nueva vision en un modelo practico para Power BI.

Objetivo del informe:

> Descubrir que experiencia Star Wars debe recibir cada tipo de audiencia para reactivar su conexion con la marca.

Campana recomendada:

> Choose Your Side - Star Wars Rebellion Lab

## Flujo recomendado

1. Ejecutar `notebooks/01_limpieza_star_wars.ipynb`.
   - Limpia datos raw.
   - Normaliza claves como `character_key`, `film_key` y `respondent_id`.
   - Exporta tablas base a `data/processed`.

2. Ejecutar `notebooks/02_eda_storytelling_star_wars.ipynb`.
   - Hace el EDA orientado a audiencia, peliculas, personajes, mundos, naves y sesgos.
   - Exporta tablas resumen `eda_*.csv`.

3. Ejecutar `scripts/build_rebellion_lab_outputs.py`.
   - Crea la capa estrategica del nuevo enfoque.
   - Genera segmentos de audiencia, mapa emocional de personajes y rutas finales de activacion.
   - Actualiza las tablas narrativas `story_*.csv`.

4. Regenerar el workbook `powerbi/starwars_powerbi_import.xlsx`.
   - El script `scripts/build_powerbi_import_workbook.mjs` incluye todos los CSV de `data/processed`.

## Tablas que importaria primero

Estas tablas son suficientes para construir la version principal del dashboard.

| Tabla | Uso en el informe | Relacion principal |
|---|---|---|
| `eda_survey_kpis.csv` | KPIs de conexion de audiencia | tabla resumen |
| `eda_fan_by_age.csv` | Fan rate por edad | tabla resumen |
| `eda_fan_by_gender.csv` | Fan rate por genero | tabla resumen |
| `strategy_audience_segments.csv` | Segmentos Choose Your Side | tabla resumen |
| `strategy_audience_age_matrix.csv` | Segmento x edad | tabla resumen |
| `strategy_survey_respondents.csv` | Encuestados con `audience_type` | `respondent_id` |
| `strategy_character_emotional_map.csv` | Personajes como emociones de marca | `character_key` |
| `eda_character_merchandising_opportunities.csv` | Scores originales de afinidad/presencia | `character_key` |
| `eda_quote_character_summary.csv` | Frases por personaje | `character_key` |
| `eda_movie_opportunities.csv` | Score de puerta de entrada por pelicula | `film_key` |
| `eda_movie_commercial_audience_summary.csv` | Audiencia + negocio por pelicula | `film_key` |
| `films_business_clean.csv` | Taquilla, ROI y negocio | `film_key` |
| `strategy_planet_experiences.csv` | Planetas como experiencias | tabla auxiliar |
| `story_featured_assets.csv` | Mundos, naves y simbolos destacados | tabla auxiliar |
| `eda_planet_business_summary.csv` | Ranking cuantitativo de planetas | `planet_key` |
| `eda_starship_business_summary.csv` | Naves por presencia/coste | `starship_key` |
| `eda_weapon_business_summary.csv` | Armas por presencia | `weapon_key` |
| `strategy_experience_routes.csv` | Rutas finales por segmento | `audience_type` |
| `story_campaign_lines.csv` | Matriz final de campana | tabla auxiliar |
| `eda_survey_bias_visual.csv` | Sesgos principales | tabla auxiliar |
| `eda_conclusions.csv` | Conclusiones ejecutivas | tabla auxiliar |

## Tablas que dejaria como apoyo

Usalas si necesitas mas detalle o anexos.

| Tabla | Motivo |
|---|---|
| `survey_movies_seen.csv` | Analisis a nivel respondent x pelicula. |
| `survey_movie_rankings.csv` | Ranking detallado por persona. |
| `survey_character_opinions.csv` | Opinion detallada por persona y personaje. |
| `universe_characters_clean.csv` | Dimension de personajes. |
| `universe_films_clean.csv` | Dimension de peliculas. |
| `universe_planets_clean.csv` | Detalle de mundos. |
| `universe_starships_clean.csv` | Detalle de naves. |
| `universe_vehicles_clean.csv` | Detalle de vehiculos. |
| `universe_weapons_clean.csv` | Detalle de armas. |
| `universe_quotes_clean.csv` | Frases completas si se crea anexo narrativo. |
| `universe_quality_summary.csv` | Calidad de datos del universo. |
| `eda_governance_missing_top.csv` | Ranking de nulos para gobernanza. |

## Relaciones recomendadas

Modelo base si usas tablas detalladas:

```text
strategy_survey_respondents[respondent_id] 1 -> * survey_movies_seen[respondent_id]
strategy_survey_respondents[respondent_id] 1 -> * survey_movie_rankings[respondent_id]
strategy_survey_respondents[respondent_id] 1 -> * survey_character_opinions[respondent_id]

films_business_clean[film_key] 1 -> * survey_movies_seen[film_key]
films_business_clean[film_key] 1 -> * survey_movie_rankings[film_key]
films_business_clean[film_key] 1 -> 1 universe_films_clean[film_key]

strategy_character_emotional_map[character_key] 1 -> 1 eda_character_merchandising_opportunities[character_key]
```

Para la primera version:

- No relaciones todas las tablas `eda_*` por defecto.
- Usa muchas tablas resumen como tablas independientes listas para graficos.
- Si un visual no necesita filtros cruzados, no fuerces una relacion.
- Empieza con las tablas estrategicas y anade detalle solo cuando haga falta.

## Medidas DAX utiles

### Conexion de audiencia

```DAX
Total Respondents =
MAX(eda_survey_kpis[respondents])
```

```DAX
Seen Any Star Wars % =
DIVIDE(MAX(eda_survey_kpis[seen_any_star_wars_pct]), 100)
```

```DAX
Star Wars Fan % =
DIVIDE(MAX(eda_survey_kpis[star_wars_fan_pct]), 100)
```

```DAX
Avg Movies Seen =
MAX(eda_survey_kpis[avg_movies_seen])
```

### Segmentos

```DAX
Segment Respondents =
SUM(strategy_audience_segments[respondents])
```

```DAX
Segment Share % =
DIVIDE(SUM(strategy_audience_segments[share_pct]), 100)
```

```DAX
Segment Avg Movies Seen =
AVERAGE(strategy_audience_segments[avg_movies_seen])
```

### Peliculas

```DAX
Top Entry Gate Score =
MAX(eda_movie_opportunities[movie_campaign_score])
```

```DAX
Movie View Rate % =
DIVIDE(AVERAGE(eda_movie_commercial_audience_summary[view_rate_pct]), 100)
```

```DAX
Worldwide Box Office =
SUM(eda_movie_commercial_audience_summary[worldwide_box_office_usd])
```

```DAX
Average ROI =
AVERAGE(eda_movie_commercial_audience_summary[roi])
```

### Personajes y emociones

```DAX
Avg Audience Affinity =
AVERAGE(strategy_character_emotional_map[audience_affinity_score])
```

```DAX
Avg Familiarity =
AVERAGE(strategy_character_emotional_map[familiarity_score])
```

```DAX
Avg Favorable % =
DIVIDE(AVERAGE(strategy_character_emotional_map[favorable_pct]), 100)
```

```DAX
Avg Unfavorable % =
DIVIDE(AVERAGE(strategy_character_emotional_map[unfavorable_pct]), 100)
```

### Sesgos

```DAX
Max Bias Metric % =
DIVIDE(MAX(eda_survey_bias_visual[bias_metric_pct]), 100)
```

## Storytelling por paginas

### Pagina 1 - La senal perdida

Pregunta:

> Donde sigue viva la conexion con Star Wars?

Visuales:

- Tarjetas KPI: `respondents`, `seen_any_star_wars_pct`, `star_wars_fan_pct`, `avg_movies_seen`.
- Barras: `eda_fan_by_age[age]` por `fan_rate_pct`.
- Barras: `eda_fan_by_gender[gender]` por `fan_rate_pct`.

Mensaje:

> La marca tiene reconocimiento, pero reconocimiento no siempre significa conexion activa.

### Pagina 2 - Los clanes de la galaxia

Pregunta:

> Que tipos de audiencia necesita reactivar la marca?

Visuales:

- Barras o donut: `audience_type` por `respondents`.
- Barras: `audience_type` por `avg_movies_seen`.
- Matriz: `audience_type` x `age`.
- Tabla: `strategic_role`, `recommended_message`, `activation_goal`.

Mensaje:

> La estrategia debe cambiar segun el vinculo: fan fiel, nostalgico, casual o neutral.

### Pagina 3 - El mapa emocional de Star Wars

Pregunta:

> Que emocion de marca activa cada personaje?

Visuales:

- Dispersion: X `familiarity_score`, Y `audience_affinity_score`, tamano `quote_count`, leyenda `brand_emotion`.
- Dispersion amor vs rechazo: X `favorable_pct`, Y `unfavorable_pct`, tamano `opinion_responses`.
- Tabla: `character_name`, `brand_emotion`, `emotional_role`, `activation_use`, `polarization_risk`.

Mensaje:

> Los personajes no solo son vendibles: son emociones de marca.

### Pagina 4 - Las puertas de entrada al universo

Pregunta:

> Que pelicula abre mejor la conversacion con cada publico?

Visuales:

- Barras: `movie_title` por `movie_campaign_score`.
- Dispersion: X `view_rate_pct`, Y `preference_score`, tamano `first_place_pct`.
- Dispersion comercial: X `worldwide_box_office_usd`, Y `view_rate_pct`, tamano `roi`, leyenda `era`.

Mensaje:

> The Empire Strikes Back funciona como puerta emocional, aunque The Force Awakens gane en taquilla mundial.

### Pagina 5 - Planetas como experiencias

Pregunta:

> Que atmosfera debe vivir cada publico?

Visuales:

- Tarjetas desde `strategy_planet_experiences`.
- Barras de `eda_planet_business_summary[name]` por `film_count`.
- Barras de `eda_planet_business_summary[name]` por `resident_count`.

Mensaje:

> Elegir un planeta es elegir una sensacion: aventura, batalla, misterio, tecnologia, lifestyle o comunidad.

### Pagina 6 - Tecnologia, poder y velocidad

Pregunta:

> Que activos generan impacto visual y accion?

Visuales:

- Barras: `eda_starship_business_summary[name]` por `film_count`.
- Barras: `universe_starships_clean[starship_class]` por recuento.
- Dispersion: `cost_in_credits` vs `film_count`, tamano `length`.
- Barras: `eda_weapon_business_summary[name]` por `film_count`.

Mensaje:

> Naves y armas convierten la estrategia en espectaculo reconocible.

### Pagina 7 - La estrategia de reactivacion

Pregunta:

> Como convertir los datos en rutas de experiencia?

Visuales:

- Matriz final desde `strategy_experience_routes`.
- Tarjetas por `audience_type`.
- Tabla de `eda_conclusions`.
- Mini bloque de sesgos desde `eda_survey_bias_visual`.

Mensaje:

> Una misma marca, varias rutas de conexion.

## Lectura critica obligatoria

Mencionar siempre:

- 78,92% de la muestra ha visto alguna pelicula.
- 66,03% se declara fan.
- La encuesta no debe tratarse como mercado general neutral.
- La nueva segmentacion es una herramienta estrategica, no una prediccion de ventas.
- Hoth y Dagobah son activos narrativos para la experiencia, no ganadores cuantitativos del ranking de planetas.
