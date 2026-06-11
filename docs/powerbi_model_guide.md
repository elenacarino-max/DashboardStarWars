# Guia de modelado Power BI - Star Wars BI

Esta guia parte de los CSV regenerados en `data/processed`.

## Objetivo

Crear un dashboard ejecutivo que responda:

Que elementos del universo Star Wars tienen mayor potencial para campanas de merchandising, contenido o experiencias interactivas?

## CSV prioritarios para importar

Importar primero estas tablas:

- `survey_respondents.csv`
- `survey_movies_seen.csv`
- `survey_movie_rankings.csv`
- `survey_character_opinions.csv`
- `universe_assets.csv`
- `universe_characters_clean.csv`
- `universe_planets_clean.csv`
- `universe_starships_clean.csv`
- `universe_quality_summary.csv`
- `eda_survey_kpis.csv`
- `eda_movie_views_summary.csv`
- `eda_movie_rank_summary.csv`
- `eda_character_opinion_summary.csv`
- `eda_character_merchandising_opportunities.csv`
- `eda_governance_missing_top.csv`
- `eda_conclusions.csv`

El resto de CSV limpios del universo se pueden importar si hacen falta paginas mas detalladas:

- `universe_films_clean.csv`
- `universe_species_clean.csv`
- `universe_vehicles_clean.csv`
- `universe_quotes_clean.csv`
- `universe_weapons_clean.csv`
- `universe_droids_clean.csv`
- `eda_planet_business_summary.csv`
- `eda_starship_business_summary.csv`
- `eda_weapon_business_summary.csv`
- `eda_quote_character_summary.csv`

## Relaciones recomendadas

Crear estas relaciones en el modelo:

- `survey_respondents[respondent_id]` 1 -> * `survey_movies_seen[respondent_id]`
- `survey_respondents[respondent_id]` 1 -> * `survey_movie_rankings[respondent_id]`
- `survey_respondents[respondent_id]` 1 -> * `survey_character_opinions[respondent_id]`

Mantener estas tablas como resumen independiente, sin forzar relaciones si Power BI no las necesita:

- `eda_survey_kpis`
- `eda_movie_views_summary`
- `eda_movie_rank_summary`
- `eda_character_opinion_summary`
- `eda_character_merchandising_opportunities`
- `eda_governance_missing_top`
- `eda_conclusions`
- `universe_quality_summary`
- `universe_assets`

Si se desea cruzar personajes de encuesta con personajes del universo, usar el campo de texto:

- `survey_character_opinions[character_name]`
- `eda_character_merchandising_opportunities[character_name]`
- `universe_characters_clean[name]`

Recomendacion: para la primera version del dashboard, usar la tabla ya preparada `eda_character_merchandising_opportunities` y evitar relaciones de texto complejas.

## Tipos de datos

Revisar en Power BI:

- `respondent_id`: texto o numero entero sin decimales. Lo importante es que tenga el mismo tipo en las 3 tablas relacionadas.
- Campos `*_binary`: numero entero.
- `movie_rank`: decimal o numero entero.
- Porcentajes `*_pct`: decimal.
- Indices y scores: decimal.
- `episode_order`: numero entero.

## Medidas DAX base

Crear una tabla de medidas llamada `Medidas`.

```DAX
Total Respondents =
DISTINCTCOUNT(survey_respondents[respondent_id])
```

```DAX
Fans % =
AVERAGE(survey_respondents[is_star_wars_fan_binary])
```

Formato recomendado: porcentaje.

```DAX
Seen Any Film % =
AVERAGE(survey_respondents[has_seen_any_star_wars_film_binary])
```

Formato recomendado: porcentaje.

```DAX
Avg Movies Seen =
AVERAGE(survey_respondents[total_movies_seen])
```

```DAX
Movies Seen =
SUM(survey_movies_seen[has_seen_movie])
```

```DAX
Movie View Rate =
DIVIDE(
    SUM(survey_movies_seen[has_seen_movie]),
    DISTINCTCOUNT(survey_movies_seen[respondent_id])
)
```

Formato recomendado: porcentaje.

```DAX
Avg Movie Rank =
AVERAGE(survey_movie_rankings[movie_rank])
```

Menor ranking medio significa mejor preferencia.

```DAX
Character Favorable Responses =
CALCULATE(
    COUNTROWS(survey_character_opinions),
    survey_character_opinions[opinion_score] > 0
)
```

```DAX
Character Opinion Responses =
CALCULATE(
    COUNTROWS(survey_character_opinions),
    survey_character_opinions[has_character_opinion] = 1
)
```

```DAX
Character Favorable % =
DIVIDE(
    [Character Favorable Responses],
    [Character Opinion Responses]
)
```

Formato recomendado: porcentaje.

```DAX
Average Character Opinion =
AVERAGE(survey_character_opinions[opinion_score])
```

```DAX
Universe Assets =
COUNTROWS(universe_assets)
```

```DAX
Avg Data Completeness =
AVERAGE(universe_assets[data_completeness_pct])
```

Formato recomendado: porcentaje si se divide entre 100; si se deja como 0-100, mostrar con sufijo `%`.

```DAX
Avg Merchandising Potential =
AVERAGE(eda_character_merchandising_opportunities[merchandising_potential_index])
```

## Pagina 1 - Portada ejecutiva

Objetivo: situar el problema de negocio.

Visuales:

- Tarjeta: `Total Respondents`.
- Tarjeta: `Fans %`.
- Tarjeta: `Seen Any Film %`.
- Tarjeta: `Avg Movies Seen`.
- Tarjeta: `Universe Assets`.
- Tabla corta: `eda_conclusions`.

Mensaje:

Star Wars tiene una audiencia amplia y activos internos variados, pero la decision comercial debe cruzar popularidad, presencia narrativa y calidad del dato.

## Pagina 2 - Universo Star Wars

Objetivo: explicar la composicion interna del universo.

Visuales:

- Barras: `universe_assets[asset_type]` por recuento de activos.
- Barras: `universe_characters_clean[species]` por recuento de personajes.
- Barras: `universe_characters_clean[gender]` por recuento de personajes.
- Tabla: `universe_quality_summary`.

Filtros:

- `asset_type`
- `species`
- `gender`

## Pagina 3 - Planetas, naves y oportunidades narrativas

Objetivo: detectar elementos con potencial visual o narrativo.

Visuales:

- Tabla o barras: `universe_planets_clean[name]` por `film_count`, `resident_count`, `population`.
- Tabla o barras: `universe_starships_clean[name]` por `film_count`, `pilot_count`, `cost_in_credits`.
- Segmentadores: clima, terreno, fabricante o clase de nave.

Tablas utiles:

- `universe_planets_clean`
- `universe_starships_clean`
- `eda_planet_business_summary`
- `eda_starship_business_summary`

## Pagina 4 - Percepcion de audiencia

Objetivo: ver que conecta con el publico.

Visuales:

- Barras: `eda_movie_views_summary[movie_title]` por `view_rate_pct`.
- Barras ordenadas ascendente: `eda_movie_rank_summary[movie_title]` por `avg_rank`.
- Barras: `eda_character_opinion_summary[character_name]` por `favorable_pct`.
- Segmentadores desde `survey_respondents`: `fan_segment`, `age`, `gender`, `education`, `location_census_region`.

Lectura:

- La pelicula mas vista y mejor rankeada en el EDA es `Episode V - The Empire Strikes Back`.
- Han Solo aparece como personaje con mayor indice de merchandising.

## Pagina 5 - Oportunidades de merchandising

Objetivo: convertir el analisis en priorizacion comercial.

Tabla principal:

- `eda_character_merchandising_opportunities`

Visuales:

- Ranking por `merchandising_potential_index`.
- Barras por `audience_affinity_score`.
- Barras por `familiarity_score`.
- Matriz con `character_name`, `opportunity_quadrant`, `favorable_pct`, `data_completeness_pct`, `merchandising_potential_index`.

Mensaje:

Priorizar elementos con alta afinidad de audiencia, alta familiaridad, presencia narrativa y buena calidad de dato.

## Pagina 6 - Sesgos y gobernanza

Objetivo: demostrar lectura critica del dato.

Visuales:

- Barras: `eda_governance_missing_top[column]` por `porcentaje`.
- Tabla: `eda_survey_sample_bias`.
- Tabla: `universe_quality_summary`.

Mensaje:

Los datos orientan decisiones, pero no son una verdad absoluta. Hay nulos relevantes y sesgos de muestra.

## Pagina 7 - Recomendaciones estrategicas

Objetivo: cerrar con acciones.

Visuales:

- Tabla: `eda_conclusions`.
- Ranking final: `eda_character_merchandising_opportunities`.
- Texto ejecutivo con 4 recomendaciones:
  - Priorizar personajes con alta afinidad y familiaridad.
  - Usar peliculas con alto visionado y buena preferencia como ancla de campana.
  - Explorar oportunidades visuales en planetas, naves y especies.
  - Revisar calidad del dato antes de automatizar decisiones.

## Orden de trabajo recomendado

1. Abrir Power BI Desktop.
2. Importar los CSV prioritarios desde `data/processed`.
3. Revisar tipos de datos.
4. Crear relaciones por `respondent_id`.
5. Crear medidas DAX base.
6. Montar paginas 1 a 7.
7. Guardar el archivo en `powerbi/star_wars_bi_dashboard.pbix`.
8. Exportar capturas a `images`.
9. Actualizar README con capturas y estado final.
