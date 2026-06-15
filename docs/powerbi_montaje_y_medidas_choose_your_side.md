# Power BI - Montaje y medidas de Choose Your Side

Guia practica para montar el dashboard con los CSV locales. No requiere fuentes externas.

## Objetivo

Construir un dashboard de 7 paginas:

1. La senal perdida
2. Los clanes de la galaxia
3. El mapa emocional de Star Wars
4. Las puertas de entrada al universo
5. Planetas como experiencias
6. Tecnologia, poder y velocidad
7. La estrategia de reactivacion

## Importacion recomendada

Para una primera version clara, importa estas tablas:

| Archivo | Tabla sugerida en Power BI | Uso |
|---|---|---|
| `eda_survey_kpis.csv` | `eda_survey_kpis` | KPIs de conexion |
| `eda_fan_by_age.csv` | `eda_fan_by_age` | Fan rate por edad |
| `eda_fan_by_gender.csv` | `eda_fan_by_gender` | Fan rate por genero |
| `strategy_audience_segments.csv` | `strategy_audience_segments` | Segmentos Choose Your Side |
| `strategy_audience_age_matrix.csv` | `strategy_audience_age_matrix` | Segmento x edad |
| `strategy_character_emotional_map.csv` | `strategy_character_emotional_map` | Mapa emocional de personajes |
| `eda_movie_opportunities.csv` | `eda_movie_opportunities` | Puertas de entrada por pelicula |
| `eda_movie_commercial_audience_summary.csv` | `eda_movie_commercial_audience_summary` | Audiencia + negocio |
| `strategy_planet_experiences.csv` | `strategy_planet_experiences` | Planetas como experiencias |
| `story_featured_assets.csv` | `story_featured_assets` | Activos narrativos |
| `eda_starship_business_summary.csv` | `eda_starship_business_summary` | Naves por presencia |
| `eda_weapon_business_summary.csv` | `eda_weapon_business_summary` | Armas iconicas |
| `strategy_experience_routes.csv` | `strategy_experience_routes` | Rutas finales por audiencia |
| `story_campaign_lines.csv` | `story_campaign_lines` | Matriz final de campana |
| `eda_survey_bias_visual.csv` | `eda_survey_bias_visual` | Grafico de sesgos |
| `eda_conclusions.csv` | `eda_conclusions` | Cierre ejecutivo |

## Medidas DAX rapidas

### Conexion

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

### Personajes

```DAX
Avg Audience Affinity =
AVERAGE(strategy_character_emotional_map[audience_affinity_score])
```

```DAX
Avg Favorable % =
DIVIDE(AVERAGE(strategy_character_emotional_map[favorable_pct]), 100)
```

```DAX
Avg Unfavorable % =
DIVIDE(AVERAGE(strategy_character_emotional_map[unfavorable_pct]), 100)
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

### Sesgos

```DAX
Max Bias Metric % =
DIVIDE(MAX(eda_survey_bias_visual[bias_metric_pct]), 100)
```

## Montaje por pagina

### Pagina 1 - La senal perdida

| Orden | Visual | Campos |
|---|---|---|
| 1 | Tarjeta | `[Total Respondents]` |
| 2 | Tarjeta | `[Seen Any Star Wars %]` |
| 3 | Tarjeta | `[Star Wars Fan %]` |
| 4 | Tarjeta | `[Avg Movies Seen]` |
| 5 | Barras | Y `eda_fan_by_age[age]`; X `fan_rate_pct` |
| 6 | Barras | Y `eda_fan_by_gender[gender]`; X `fan_rate_pct` |

Texto:

> La conexion existe, pero no esta repartida por igual.

### Pagina 2 - Los clanes de la galaxia

| Orden | Visual | Campos |
|---|---|---|
| 1 | Dona o barras | `audience_type`; valor `respondents` |
| 2 | Barras | `audience_type`; valor `avg_movies_seen` |
| 3 | Matriz | Filas `audience_type`; columnas `age`; valores `respondents` |
| 4 | Tabla | `audience_type`, `strategic_role`, `activation_goal` |

Texto:

> La galaxia tiene clanes. Cada clan necesita una puerta distinta.

### Pagina 3 - El mapa emocional de Star Wars

| Orden | Visual | Campos |
|---|---|---|
| 1 | Dispersion | X `familiarity_score`; Y `audience_affinity_score`; tamano `quote_count`; leyenda `brand_emotion` |
| 2 | Dispersion | X `favorable_pct`; Y `unfavorable_pct`; tamano `opinion_responses`; leyenda `polarization_risk` |
| 3 | Tabla | `character_name`, `brand_emotion`, `emotional_role`, `activation_use` |

Texto:

> Los personajes son emociones de marca.

### Pagina 4 - Las puertas de entrada al universo

| Orden | Visual | Campos |
|---|---|---|
| 1 | Barras | Y `movie_title`; X `movie_campaign_score` |
| 2 | Dispersion | X `view_rate_pct`; Y `preference_score`; tamano `first_place_pct`; leyenda `era` |
| 3 | Dispersion | X `worldwide_box_office_usd`; Y `view_rate_pct`; tamano `roi`; leyenda `era` |
| 4 | Tabla | `film_title`, `worldwide_box_office_usd`, `roi`, `view_rate_pct`, `first_place_pct` |

Texto:

> Cada pelicula abre una conversacion distinta.

### Pagina 5 - Planetas como experiencias

| Orden | Visual | Campos |
|---|---|---|
| 1 | Tarjetas | `planet_name`, `brand_atmosphere`, `experience_concept` |
| 2 | Barras | `eda_planet_business_summary[name]`; valor `film_count` |
| 3 | Barras | `eda_planet_business_summary[name]`; valor `resident_count` |

Texto:

> Los planetas son atmosferas de campana.

### Pagina 6 - Tecnologia, poder y velocidad

| Orden | Visual | Campos |
|---|---|---|
| 1 | Barras | `eda_starship_business_summary[name]`; valor `film_count` |
| 2 | Barras | `universe_starships_clean[starship_class]`; recuento de `name` |
| 3 | Dispersion | X `cost_in_credits`; Y `film_count`; tamano `length`; detalle `name` |
| 4 | Barras | `eda_weapon_business_summary[name]`; valor `film_count` |

Texto:

> El espectaculo vuelve memorable la experiencia.

### Pagina 7 - La estrategia de reactivacion

| Orden | Visual | Campos |
|---|---|---|
| 1 | Matriz | `audience_type`, `entry_gate`, `key_characters`, `world`, `experience_format`, `recommended_action` |
| 2 | Tarjetas | Una por `audience_type` |
| 3 | Tabla | `eda_conclusions[area]`, `finding`, `business_reading` |
| 4 | Barras | `eda_survey_bias_visual[bias_dimension]` por `bias_metric_pct` |

Texto:

> Una marca, varias rutas de conexion.

Nota de lectura:

> La recomendacion es direccional porque 78,92% de la muestra ha visto alguna pelicula y 66,03% se declara fan.

## Checklist final

- [ ] Refrescar datos despues de regenerar CSV o workbook.
- [ ] Confirmar que los 4 segmentos aparecen en orden correcto.
- [ ] Revisar que porcentajes se vean como `%`.
- [ ] Revisar que moneda se vea en USD.
- [ ] Anadir la nota de sesgos en pagina 7: la muestra esta orientada a personas familiarizadas con Star Wars.
- [ ] No presentar Hoth o Dagobah como ranking cuantitativo de planetas.
