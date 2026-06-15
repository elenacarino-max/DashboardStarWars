# Power BI - Visualizacion Choose Your Side

Propuesta visual para el dashboard **Star Wars Rebellion Lab**. Cada pagina responde una pregunta de negocio y termina con una lectura accionable.

## Tablas base

| Tabla | Uso |
|---|---|
| `eda_survey_kpis.csv` | KPIs de conexion |
| `eda_fan_by_age.csv` | Diferencias por edad |
| `eda_fan_by_gender.csv` | Diferencias por genero |
| `strategy_audience_segments.csv` | Segmentos de audiencia |
| `strategy_audience_age_matrix.csv` | Cruce segmento x edad |
| `strategy_character_emotional_map.csv` | Mapa emocional de personajes |
| `eda_movie_opportunities.csv` | Score de puerta de entrada |
| `eda_movie_commercial_audience_summary.csv` | Audiencia + negocio por pelicula |
| `strategy_planet_experiences.csv` | Planetas como conceptos de experiencia |
| `story_featured_assets.csv` | Activos narrativos destacados |
| `eda_starship_business_summary.csv` | Naves iconicas |
| `eda_weapon_business_summary.csv` | Armas iconicas |
| `strategy_experience_routes.csv` | Rutas finales de activacion |
| `story_campaign_lines.csv` | Matriz final de campana |
| `eda_survey_bias_visual.csv` | Sesgos |
| `eda_conclusions.csv` | Cierre ejecutivo |

## Estilo visual recomendado

- Fondo oscuro sobrio, no completamente negro.
- Dorado para decisiones y ruta final.
- Azul para heroes/Jedi y lectura positiva.
- Rojo solo para riesgo, sesgo o Lado Oscuro.
- Cian o verde para tecnologia, exploracion y segmentos casuales.
- Titulos cortos: `La senal perdida`, `Los clanes de la galaxia`, etc.
- Una frase de lectura por pagina.

## Pagina 1 - La senal perdida

Pregunta: **Donde sigue viva la conexion con Star Wars?**

| Visual | Tabla | Campos | Lectura |
|---|---|---|---|
| Tarjeta KPI | `eda_survey_kpis` | `respondents` | 1.186 personas en la muestra |
| Tarjeta KPI | `eda_survey_kpis` | `seen_any_star_wars_pct` | 78,92% ha visto alguna pelicula |
| Tarjeta KPI | `eda_survey_kpis` | `star_wars_fan_pct` | 66,03% se declara fan |
| Tarjeta KPI | `eda_survey_kpis` | `avg_movies_seen` | Media de 3,29 peliculas vistas |
| Barras | `eda_fan_by_age` | Eje `age`; valor `fan_rate_pct` | El grupo 30-44 lidera el fan rate |
| Barras | `eda_fan_by_gender` | Eje `gender`; valor `fan_rate_pct` | Ayuda a explicar diferencias de muestra |

Comentario:

> El reconocimiento existe, pero el vinculo emocional no esta igual de activo en todos los grupos.

## Pagina 2 - Los clanes de la galaxia

Pregunta: **Que tipos de audiencia necesita reactivar la marca?**

| Visual | Tabla | Campos | Lectura |
|---|---|---|---|
| Barras o dona | `strategy_audience_segments` | `audience_type`, `respondents` | Muestra el peso de cada clan |
| Barras | `strategy_audience_segments` | `audience_type`, `avg_movies_seen` | Diferencia profundidad de consumo |
| Matriz | `strategy_audience_age_matrix` | `audience_type`, `age`, `respondents` | Cruza segmento y edad |
| Tabla | `strategy_audience_segments` | `strategic_role`, `activation_goal` | Convierte segmentos en accion |

Comentario:

> El dashboard deja de hablar a "la audiencia" como una masa unica y la convierte en clanes accionables.

## Pagina 3 - El mapa emocional de Star Wars

Pregunta: **Que emocion de marca activa cada personaje?**

| Visual | Tabla | Campos | Lectura |
|---|---|---|---|
| Dispersion | `strategy_character_emotional_map` | X `familiarity_score`; Y `audience_affinity_score`; tamano `quote_count`; color `brand_emotion` | Reconocimiento + conexion emocional |
| Dispersion | `strategy_character_emotional_map` | X `favorable_pct`; Y `unfavorable_pct`; tamano `opinion_responses`; color `polarization_risk` | Identifica personajes seguros y polarizantes |
| Tabla | `strategy_character_emotional_map` | `character_name`, `brand_emotion`, `emotional_role`, `activation_use` | Traduce personaje en estrategia |

Comentario:

> Han Solo activa rebeldia, Luke esperanza, Leia liderazgo, Yoda sabiduria y Vader poder con riesgo de polarizacion.

## Pagina 4 - Las puertas de entrada al universo

Pregunta: **Que pelicula abre mejor la conversacion con cada publico?**

| Visual | Tabla | Campos | Lectura |
|---|---|---|---|
| Barras | `eda_movie_opportunities` | `movie_title`, `movie_campaign_score` | `Episode V` lidera la oportunidad |
| Dispersion | `eda_movie_commercial_audience_summary` | X `view_rate_pct`; Y `preference_score`; tamano `first_place_pct`; color `era` | Popularidad frente a preferencia |
| Dispersion | `eda_movie_commercial_audience_summary` | X `worldwide_box_office_usd`; Y `view_rate_pct`; tamano `roi`; color `era` | Negocio frente a conexion |
| Tabla | `eda_movie_commercial_audience_summary` | `film_title`, `worldwide_box_office_usd`, `roi`, `view_rate_pct`, `first_place_pct` | Defensa ejecutiva |

Comentario:

> La mejor puerta de entrada no tiene que ser la mayor taquilla; tiene que abrir una conversacion emocional clara.

## Pagina 5 - Planetas como experiencias

Pregunta: **Que atmosfera debe vivir cada publico?**

| Visual | Tabla | Campos | Lectura |
|---|---|---|---|
| Tarjetas | `strategy_planet_experiences` | `planet_name`, `brand_atmosphere`, `experience_concept` | Convierte mundos en conceptos |
| Barras | `eda_planet_business_summary` | `name`, `film_count` | Presencia narrativa cuantitativa |
| Barras | `eda_planet_business_summary` | `name`, `resident_count` | Relacion con personajes |

Comentario:

> Tatooine puede ser origen y nostalgia; Hoth accion; Dagobah entrenamiento; Coruscant tecnologia; Naboo lifestyle; Endor aventura familiar.

Nota:

Hoth y Dagobah son activos narrativos en `story_featured_assets.csv`. No deben presentarse como ganadores cuantitativos de `eda_planet_business_summary.csv`.

## Pagina 6 - Tecnologia, poder y velocidad

Pregunta: **Que activos generan impacto visual y accion?**

| Visual | Tabla | Campos | Lectura |
|---|---|---|---|
| Barras | `eda_starship_business_summary` | `name`, `film_count` | Millennium Falcon y X-wing como siluetas reconocibles |
| Barras | `universe_starships_clean` | `starship_class`, recuento de `name` | Tipos de nave |
| Dispersion | `eda_starship_business_summary` | X `cost_in_credits`; Y `film_count`; tamano `length` | Coste como contexto, no KPI central |
| Barras | `eda_weapon_business_summary` | `name`, `film_count` | Lightsaber como simbolo transversal |

Comentario:

> Si los personajes generan apego, las naves y armas generan espectaculo.

## Pagina 7 - La estrategia de reactivacion

Pregunta: **Como convertir los datos en rutas de experiencia?**

| Visual | Tabla | Campos | Lectura |
|---|---|---|---|
| Matriz | `strategy_experience_routes` | `audience_type`, `entry_gate`, `key_characters`, `world`, `experience_format`, `recommended_action` | Recomendacion final por segmento |
| Tarjetas | `strategy_experience_routes` | Una tarjeta por `audience_type` | Facilita el cierre oral |
| Tabla | `eda_conclusions` | `area`, `finding`, `business_reading` | Cierre ejecutivo |
| Barras | `eda_survey_bias_visual` | `bias_dimension`, `bias_metric_pct`, color `risk_level` | Lectura critica |

Comentario:

> Star Wars no necesita una unica campana. Necesita una galaxia de experiencias, disenada para que cada publico elija su lado.

## Hitos para anotar en Power BI

1. 78,92% ha visto alguna pelicula y 66,03% se declara fan.
2. `Jedi fiel` tiene 443 respuestas y una media de 5,93 peliculas vistas.
3. `Territorio neutral` tiene 400 respuestas y necesita entrada simple.
4. `Episode V: The Empire Strikes Back` lidera la conexion emocional dentro de la encuesta.
5. Han Solo activa rebeldia y lidera afinidad total.
6. Luke Skywalker activa esperanza y tiene la favorabilidad mas alta.
7. Darth Vader activa poder, pero tiene riesgo de polarizacion.
8. Millennium Falcon, X-wing y Lightsaber son activos visuales transversales.
9. Los sesgos no invalidan el dashboard, pero limitan la lectura como mercado general.
