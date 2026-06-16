# Plan del dashboard Power BI

## Pregunta ejecutiva

Que tipo de experiencia Star Wars deberiamos crear para reactivar a cada tipo de publico?

## Narrativa

El dashboard cuenta la historia **Choose Your Side - Star Wars Rebellion Lab**.

La galaxia no ha desaparecido del imaginario del publico, pero la conexion no esta igual de activa en todos los segmentos. El objetivo no es elegir un unico producto ni un unico personaje, sino disenar una estrategia modular de marca: varias rutas de entrada para que cada persona encuentre su lugar en la galaxia.

El dashboard debe responder:

1. Donde sigue viva la conexion con Star Wars.
2. Que tipos de audiencia existen.
3. Que emociones activa cada personaje.
4. Que peliculas funcionan como puertas de entrada.
5. Que mundos pueden convertirse en experiencias.
6. Que naves, vehiculos y armas aportan espectaculo.
7. Que estrategia final debe lanzar la empresa.

## Pagina 1: La senal perdida

Objetivo: medir la conexion activa con Star Wars.

Tablas:

- `eda_survey_kpis.csv`
- `eda_fan_by_age.csv`
- `eda_fan_by_gender.csv`
- `survey_respondents.csv`

Graficos:

- Tarjetas KPI: encuestados, `% que ha visto alguna pelicula`, `% fans`, media de peliculas vistas.
- Barras: fan rate por edad.
- Barras: fan rate por genero.
- Segmentador: `fan_segment`.

Mensaje:

> El primer hallazgo no es que pelicula gusta mas, sino donde sigue viva la conexion.

## Pagina 2: Los clanes de la galaxia

Objetivo: convertir la muestra en segmentos accionables.

Tablas:

- `strategy_audience_segments.csv`
- `strategy_audience_age_matrix.csv`
- `strategy_survey_respondents.csv`

Segmentos:

| Segmento | Definicion | Rol estrategico |
|---|---|---|
| Jedi fiel | Fan y 5 o mas peliculas vistas | Profundidad, lore e inmersion |
| Rebelde nostalgico | Fan con menos de 5 peliculas vistas | Nostalgia y recuerdo emocional |
| Explorador casual | No fan con 2 o mas peliculas vistas | Reconocimiento visual y entrada simple |
| Territorio neutral | No fan o consumo casi nulo | Primer contacto digital y sin exceso de lore |

Graficos:

- Barras o donut: distribucion de `audience_type`.
- Barras: media de peliculas vistas por segmento.
- Matriz: `audience_type` x `age`.
- Tabla breve con `strategic_role`, `recommended_message` y `activation_goal`.

Mensaje:

> La galaxia no tiene una audiencia unica. Tiene clanes.

## Pagina 3: El mapa emocional de Star Wars

Objetivo: presentar personajes como emociones de marca.

Tablas:

- `strategy_character_emotional_map.csv`
- `eda_character_merchandising_opportunities.csv`
- `eda_quote_character_summary.csv`

Graficos:

- Dispersion: X `familiarity_score`, Y `audience_affinity_score`, tamano `quote_count`, leyenda `brand_emotion`.
- Dispersion: X `favorable_pct`, Y `unfavorable_pct`, tamano `opinion_responses`, detalle `character_name`.
- Barras: personajes con mas frases o presencia narrativa.
- Tabla: personaje, emocion, rol emocional, uso de activacion y riesgo de polarizacion.

Mensaje:

> Star Wars no conecta por sus datos tecnicos. Conecta por emociones.

## Pagina 4: Las puertas de entrada al universo

Objetivo: decidir que pelicula abre mejor la conversacion con cada publico.

Tablas:

- `eda_movie_opportunities.csv`
- `eda_movie_commercial_audience_summary.csv`
- `films_business_clean.csv`

Graficos:

- Barras: `movie_title` por `movie_campaign_score`.
- Dispersion: X `view_rate_pct`, Y `preference_score`, tamano `first_place_pct`.
- Dispersion: X `worldwide_box_office_usd`, Y `view_rate_pct`, tamano `roi`, leyenda `era`.
- Tabla: pelicula, taquilla, ROI, visionado, preferencia y estado del dato.

Mensaje:

> La pregunta no es cual es la mejor pelicula. La pregunta es que pelicula abre mejor la conversacion con cada publico.

## Pagina 5: Planetas como experiencias

Objetivo: transformar mundos en atmosferas de campana.

Tablas:

- `strategy_planet_experiences.csv`
- `story_featured_assets.csv`
- `eda_planet_business_summary.csv`
- `universe_planets_clean.csv`

Graficos:

- Tarjetas: planeta, atmosfera de marca y concepto de experiencia.
- Barras: planetas por `film_count`.
- Barras: planetas por `resident_count`.
- Dispersion opcional: X `film_count`, Y `resident_count`, tamano `population`, leyenda `climate`.

Mensaje:

> Los planetas no son fondos decorativos. Son atmosferas de campana.

## Pagina 6: Tecnologia, poder y velocidad

Objetivo: agrupar naves, vehiculos y armas como activos de adrenalina.

Tablas:

- `eda_starship_business_summary.csv`
- `eda_weapon_business_summary.csv`
- `universe_starships_clean.csv`
- `universe_vehicles_clean.csv`
- `universe_weapons_clean.csv`

Graficos:

- Barras: naves por `film_count`.
- Barras: naves por `starship_class`.
- Dispersion: X `cost_in_credits`, Y `film_count`, tamano `length`, detalle `name`.
- Barras: armas por `film_count`.

Mensaje:

> Si los personajes generan emocion, las naves y armas generan espectaculo.

## Pagina 7: La estrategia de reactivacion

Objetivo: cerrar con una recomendacion accionable de marca.

Tablas:

- `strategy_experience_routes.csv`
- `story_campaign_lines.csv`
- `eda_conclusions.csv`
- `eda_survey_bias_visual.csv`

Graficos:

- Matriz: `audience_type`, `entry_gate`, `key_characters`, `world`, `experience_format`, `recommended_action`.
- Tarjetas: una ruta por segmento.
- Tabla: conclusiones ejecutivas.
- Barras pequenas: sesgos principales desde `eda_survey_bias_visual.csv`.

Mensaje:

> Star Wars no necesita una campana unica. Necesita una galaxia de experiencias, disenada para que cada publico elija su lado.

Lectura obligatoria:

> La recomendacion es accionable, pero direccional: la muestra esta muy familiarizada con Star Wars y no representa por si sola al mercado general.

## Sesgos y lectura critica

La lectura de sesgos puede aparecer como bloque final de la pagina 7 o como pagina anexa si el dashboard necesita mas detalle.

Puntos obligatorios:

- 78,92% de la muestra ha visto alguna pelicula.
- 66,03% se declara fan.
- La muestra no representa de forma neutral al publico general.
- Hoth y Dagobah son activos narrativos de experiencia, no ganadores cuantitativos del ranking de planetas.
- Los costes de naves y armas tienen nulos relevantes, asi que se interpretan como contexto, no como KPI principal.

## Entrega recomendada

La version principal debe ser de 7 paginas. Si el tiempo de presentacion es corto, se puede mostrar la pagina de sesgos integrada en el cierre y dejar graficos de calidad del dato como anexo.
