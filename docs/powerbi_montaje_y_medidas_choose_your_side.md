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

Para la version final sencilla, uso solo estas 12 hojas del Excel. El resto son tablas de apoyo o detalle y no hacen falta para presentar.

| Hoja en Excel / tabla en Power BI | Uso |
|---|---|
| `survey_kpis` | KPIs de conexion |
| `fan_by_age` | Fan rate por edad |
| `fan_by_gender` | Fan rate por genero |
| `strategy_audience_segments` | Segmentos Choose Your Side |
| `strategy_character_emotional_ma` | Mapa emocional de personajes |
| `movie_opportunities` | Score de puerta de entrada por pelicula |
| `movie_commercial_audience_summa` | Audiencia + negocio por pelicula |
| `strategy_planet_experiences` | Planetas como experiencias |
| `starship_business_summary` | Naves por presencia |
| `weapon_business_summary` | Armas iconicas |
| `strategy_experience_routes` | Rutas finales por audiencia |
| `survey_bias_visual` | Grafico de sesgos |

No uses `README`, `survey_clean_wide`, `u_films`, `u_characters` ni tablas `u_*` para la version de presentacion.

## Relaciones recomendadas

Puedes montar casi todo sin relaciones, usando cada pagina con sus propias tablas. Si quieres crear relaciones, crea solo estas dos:

| De | A | Cardinalidad | Direccion |
|---|---|---|---|
| `movie_commercial_audience_summa[film_key]` | `movie_opportunities[film_key]` | 1 a 1 o 1 a muchos | Simple |
| `strategy_audience_segments[audience_type]` | `strategy_experience_routes[audience_type]` | 1 a 1 | Simple |

No relaciones `starship_business_summary[film_keys]` ni `weapon_business_summary[film_keys]` con `film_key`: son listas de varias peliculas dentro de una celda.

## Medidas DAX rapidas

### Conexion

```DAX
Total Respondents =
MAX(survey_kpis[respondents])
```

```DAX
Seen Any Star Wars % =
DIVIDE(MAX(survey_kpis[seen_any_star_wars_pct]), 100)
```

```DAX
Star Wars Fan % =
DIVIDE(MAX(survey_kpis[star_wars_fan_pct]), 100)
```

```DAX
Avg Movies Seen =
MAX(survey_kpis[avg_movies_seen])
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
AVERAGE(strategy_character_emotional_ma[audience_affinity_score])
```

```DAX
Avg Favorable % =
DIVIDE(AVERAGE(strategy_character_emotional_ma[favorable_pct]), 100)
```

```DAX
Avg Unfavorable % =
DIVIDE(AVERAGE(strategy_character_emotional_ma[unfavorable_pct]), 100)
```

### Peliculas

```DAX
Top Entry Gate Score =
MAX(movie_opportunities[movie_campaign_score])
```

```DAX
Movie View Rate % =
DIVIDE(AVERAGE(movie_commercial_audience_summa[view_rate_pct]), 100)
```

```DAX
Worldwide Box Office =
SUM(movie_commercial_audience_summa[worldwide_box_office_usd])
```

### Sesgos

```DAX
Max Bias Metric % =
DIVIDE(MAX(survey_bias_visual[bias_metric_pct]), 100)
```

## Montaje por pagina

### Pagina 1 - La senal perdida

| Orden | Visual | Campos |
|---|---|---|
| 1 | Tarjeta | `[Total Respondents]` |
| 2 | Tarjeta | `[Seen Any Star Wars %]` |
| 3 | Tarjeta | `[Star Wars Fan %]` |
| 4 | Tarjeta | `[Avg Movies Seen]` |
| 5 | Barras | Y `fan_by_age[age]`; X `fan_rate_pct` |
| 6 | Barras | Y `fan_by_gender[gender]`; X `fan_rate_pct` |

Texto:

> La conexion existe, pero no esta repartida por igual.

### Pagina 2 - Los clanes de la galaxia

| Orden | Visual | Campos |
|---|---|---|
| 1 | Dona o barras | `audience_type`; valor `respondents` |
| 2 | Barras | `audience_type`; valor `avg_movies_seen` |
| 3 | Tabla | `audience_type`, `strategic_role`, `activation_goal` |

Texto:

> La galaxia tiene clanes. Cada clan necesita una puerta distinta.

### Pagina 3 - El mapa emocional de Star Wars

| Orden | Visual | Campos |
|---|---|---|
| 1 | Dispersion | X `familiarity_score`; Y `audience_affinity_score`; leyenda `character_name`; tooltip `brand_emotion`, `emotional_role`, `polarization_risk` |
| 2 | Tabla | `character_name`, `brand_emotion`, `emotional_role`, `activation_use`, `polarization_risk` |

Texto:

> Los personajes son emociones de marca.

### Pagina 4 - Las puertas de entrada al universo

| Orden | Visual | Campos |
|---|---|---|
| 1 | Barras | De `movie_opportunities`: Y `movie_title`; X `movie_campaign_score` |
| 2 | Dispersion | De `movie_commercial_audience_summa`: X `view_rate_pct`; Y `preference_score`; tamano `first_place_pct`; leyenda `era`; detalle/leyenda `movie_title` |
| 3 | Tabla | De `movie_commercial_audience_summa`: `movie_title`, `worldwide_box_office_usd`, `roi`, `view_rate_pct`, `preference_score` |

Texto:

> Cada pelicula abre una conversacion distinta.

### Pagina 5 - Planetas como experiencias

| Orden | Visual | Campos |
|---|---|---|
| 1 | Tarjetas | `planet_name`, `brand_atmosphere`, `experience_concept` |

Texto:

> Los planetas son atmosferas de campana.

### Pagina 6 - Tecnologia, poder y velocidad

| Orden | Visual | Campos |
|---|---|---|
| 1 | Barras | `starship_business_summary[name]`; valor `film_count` |
| 2 | Barras | `weapon_business_summary[name]`; valor `film_count` |

Texto:

> El espectaculo vuelve memorable la experiencia.

### Pagina 7 - La estrategia de reactivacion

| Orden | Visual | Campos |
|---|---|---|
| 1 | Matriz | `audience_type`, `entry_gate`, `key_characters`, `world`, `experience_format`, `recommended_action` |
| 2 | Tarjetas | Una por `audience_type` |
| 3 | Barras | `survey_bias_visual[bias_dimension]` por `bias_metric_pct` |

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
