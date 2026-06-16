# Guia de modelado Power BI - Choose Your Side

Esta guia parte de los CSV regenerados en `data/processed`.

## Objetivo

Crear un dashboard ejecutivo que responda:

> Que experiencia Star Wars debe recibir cada segmento de audiencia para reactivar su conexion con la marca?

El modelo combina cuatro capas:

- Conexion de audiencia.
- Segmentacion estrategica.
- Emociones, peliculas y activos narrativos.
- Sesgos y calidad del dato.

## CSV prioritarios para importar

Importar primero estas tablas:

- `eda_survey_kpis.csv`
- `eda_fan_by_age.csv`
- `eda_fan_by_gender.csv`
- `strategy_audience_segments.csv`
- `strategy_audience_age_matrix.csv`
- `strategy_survey_respondents.csv`
- `strategy_character_emotional_map.csv`
- `eda_character_merchandising_opportunities.csv`
- `eda_quote_character_summary.csv`
- `eda_movie_opportunities.csv`
- `eda_movie_commercial_audience_summary.csv`
- `films_business_clean.csv`
- `strategy_planet_experiences.csv`
- `story_featured_assets.csv`
- `eda_planet_business_summary.csv`
- `eda_starship_business_summary.csv`
- `eda_weapon_business_summary.csv`
- `strategy_experience_routes.csv`
- `story_campaign_lines.csv`
- `eda_survey_bias_visual.csv`
- `eda_conclusions.csv`

## CSV de apoyo

Usar solo si se necesitan filtros cruzados o anexos:

- `survey_movies_seen.csv`
- `survey_movie_rankings.csv`
- `survey_character_opinions.csv`
- `universe_assets.csv`
- `universe_characters_clean.csv`
- `universe_films_clean.csv`
- `universe_planets_clean.csv`
- `universe_starships_clean.csv`
- `universe_vehicles_clean.csv`
- `universe_weapons_clean.csv`
- `universe_quotes_clean.csv`
- `universe_quality_summary.csv`
- `eda_governance_missing_top.csv`
- `eda_relationship_quality_checks.csv`

## Relaciones recomendadas

La primera version puede funcionar con tablas resumen sin relaciones complejas. Si se quiere un modelo relacional, crear estas:

- `strategy_survey_respondents[respondent_id]` 1 -> * `survey_movies_seen[respondent_id]`
- `strategy_survey_respondents[respondent_id]` 1 -> * `survey_movie_rankings[respondent_id]`
- `strategy_survey_respondents[respondent_id]` 1 -> * `survey_character_opinions[respondent_id]`
- `films_business_clean[film_key]` 1 -> * `survey_movies_seen[film_key]`
- `films_business_clean[film_key]` 1 -> * `survey_movie_rankings[film_key]`
- `films_business_clean[film_key]` 1 -> 1 `universe_films_clean[film_key]`
- `strategy_character_emotional_map[character_key]` 1 -> 1 `eda_character_merchandising_opportunities[character_key]`

Mantener estas tablas como resumen independiente salvo que haya una necesidad clara:

- `eda_survey_kpis`
- `eda_fan_by_age`
- `eda_fan_by_gender`
- `strategy_audience_segments`
- `strategy_audience_age_matrix`
- `eda_movie_opportunities`
- `eda_movie_commercial_audience_summary`
- `strategy_planet_experiences`
- `story_featured_assets`
- `strategy_experience_routes`
- `story_campaign_lines`
- `eda_survey_bias_visual`
- `eda_conclusions`

## Tipos de datos

Revisar en Power BI:

- `respondent_id`: texto o numero entero sin decimales, pero consistente entre tablas.
- `audience_type_order`: numero entero.
- Campos `*_binary`: numero entero.
- Campos `*_pct`: decimal.
- Scores e indices: decimal.
- `film_key`, `character_key`, `planet_key`: texto.
- Campos `*_usd`: numero entero, formato moneda USD.
- `roi`: decimal.
- `data_status`: texto.

## Medidas DAX base

Crear una tabla llamada `Medidas`.

### Audiencia

```DAX
Total Respondents =
MAX(eda_survey_kpis[respondents])
```

```DAX
Seen Any Film % =
DIVIDE(MAX(eda_survey_kpis[seen_any_star_wars_pct]), 100)
```

```DAX
Fans % =
DIVIDE(MAX(eda_survey_kpis[star_wars_fan_pct]), 100)
```

```DAX
Avg Movies Seen =
MAX(eda_survey_kpis[avg_movies_seen])
```

### Segmentos

```DAX
Audience Segment Count =
SUM(strategy_audience_segments[respondents])
```

```DAX
Audience Segment Share % =
DIVIDE(SUM(strategy_audience_segments[share_pct]), 100)
```

```DAX
Audience Avg Movies Seen =
AVERAGE(strategy_audience_segments[avg_movies_seen])
```

```DAX
Audience Avg Character Affinity =
AVERAGE(strategy_audience_segments[avg_character_affinity])
```

### Peliculas

```DAX
Movie Campaign Score =
AVERAGE(eda_movie_opportunities[movie_campaign_score])
```

```DAX
Movie View Rate % =
DIVIDE(AVERAGE(eda_movie_commercial_audience_summary[view_rate_pct]), 100)
```

```DAX
Movie Preference Score =
AVERAGE(eda_movie_commercial_audience_summary[preference_score])
```

```DAX
Worldwide Box Office =
SUM(eda_movie_commercial_audience_summary[worldwide_box_office_usd])
```

```DAX
Average ROI =
AVERAGE(eda_movie_commercial_audience_summary[roi])
```

### Personajes

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

## Paginas del modelo

### 1. La senal perdida

Visuales:

- Tarjetas: `Total Respondents`, `Seen Any Film %`, `Fans %`, `Avg Movies Seen`.
- Barras: `eda_fan_by_age[age]` por `fan_rate_pct`.
- Barras: `eda_fan_by_gender[gender]` por `fan_rate_pct`.

### 2. Los clanes de la galaxia

Visuales:

- Barras o donut: `strategy_audience_segments[audience_type]` por `respondents`.
- Barras: `audience_type` por `avg_movies_seen`.
- Matriz: `strategy_audience_age_matrix[audience_type]` x `age`.
- Tabla: `strategic_role`, `recommended_message`, `activation_goal`.

### 3. El mapa emocional de Star Wars

Visuales:

- Dispersion: `familiarity_score` vs `audience_affinity_score`.
- Dispersion: `favorable_pct` vs `unfavorable_pct`.
- Tabla: `character_name`, `brand_emotion`, `emotional_role`, `activation_use`, `polarization_risk`.

### 4. Las puertas de entrada al universo

Visuales:

- Barras: `movie_title` por `movie_campaign_score`.
- Dispersion: `view_rate_pct` vs `preference_score`, tamano `first_place_pct`.
- Dispersion: `worldwide_box_office_usd` vs `view_rate_pct`, tamano `roi`, leyenda `era`.

### 5. Planetas como experiencias

Visuales:

- Tarjetas desde `strategy_planet_experiences`.
- Barras: `eda_planet_business_summary[name]` por `film_count`.
- Barras: `eda_planet_business_summary[name]` por `resident_count`.

Nota: Hoth y Dagobah aparecen como activos narrativos, no como ganadores cuantitativos del ranking de planetas.

### 6. Tecnologia, poder y velocidad

Visuales:

- Barras: `eda_starship_business_summary[name]` por `film_count`.
- Barras: `universe_starships_clean[starship_class]` por recuento.
- Dispersion: `cost_in_credits` vs `film_count`, tamano `length`.
- Barras: `eda_weapon_business_summary[name]` por `film_count`.

### 7. La estrategia de reactivacion

Visuales:

- Matriz: `strategy_experience_routes`.
- Tarjetas por `audience_type`.
- Tabla: `eda_conclusions`.
- Bloque de sesgos: `eda_survey_bias_visual`.

## Orden de trabajo recomendado

1. Importar el workbook `powerbi/starwars_powerbi_import.xlsx` o los CSV individuales.
2. Revisar tipos de datos.
3. Crear medidas base.
4. Montar paginas 1, 2 y 3 para validar la nueva narrativa.
5. Montar paginas 4, 5 y 6 con peliculas y activos visuales.
6. Montar pagina 7 con rutas finales y sesgos.
7. Refrescar visuales y revisar porcentajes, moneda y orden de rankings.
8. Guardar el `.pbix` final en `powerbi/graficos_PBI.pbix`.
