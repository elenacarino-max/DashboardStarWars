# Power BI - Graficos paso a paso

Esta guia convierte el documento de storytelling en instrucciones concretas dentro de Power BI.

## Antes de crear graficos

Comprueba esto en Power BI:

1. Vista `Modelo`: revisa que no haya relaciones raras `*:*`.
2. Vista `Datos`: confirma que los campos monetarios son numero entero o decimal.
3. Vista `Informe`: empieza con pocas paginas y pocos visuales. Es mejor un dashboard claro que muchas paginas llenas.

## Medidas base

Crea una tabla llamada `Medidas` si puedes. Si no, crea las medidas dentro de `films_business_clean` y `survey_respondents`.

### Negocio

```DAX
Worldwide Box Office =
SUM(films_business_clean[worldwide_box_office_usd])
```

```DAX
Total Production Budget =
SUM(films_business_clean[budget_usd])
```

```DAX
Estimated Profit =
SUM(films_business_clean[profit_estimated_usd])
```

```DAX
Average ROI =
AVERAGE(films_business_clean[roi])
```

### Audiencia

```DAX
Total Respondents =
DISTINCTCOUNT(survey_respondents[respondent_id])
```

```DAX
Fans % =
AVERAGE(survey_respondents[is_star_wars_fan_binary])
```

```DAX
Seen Any Film % =
AVERAGE(survey_respondents[has_seen_any_star_wars_film_binary])
```

```DAX
Avg Movies Seen =
AVERAGE(survey_respondents[total_movies_seen])
```

### Universo

```DAX
Universe Assets =
COUNTROWS(universe_assets)
```

```DAX
Avg Merchandising Potential =
AVERAGE(eda_character_merchandising_opportunities[merchandising_potential_index])
```

## Graficos imprescindibles

Si vas justa de tiempo, crea estos primero.

### 1. Taquilla mundial por pelicula

Visual: `Grafico de barras agrupadas`.

Campos:

- Eje Y: `films_business_clean[film_title]`
- Eje X: `films_business_clean[worldwide_box_office_usd]`
- Filtro visual: `films_business_clean[data_status] = final`

Formato:

- Ordenar por `worldwide_box_office_usd`, descendente.
- Titulo: `Peliculas con mayor recaudacion mundial`
- Formato del eje X: moneda USD.

Lectura:

La pelicula con mayor taquilla no tiene por que ser la mas rentable proporcionalmente.

### 2. ROI por pelicula

Visual: `Grafico de barras agrupadas`.

Campos:

- Eje Y: `films_business_clean[film_title]`
- Eje X: `films_business_clean[roi]`
- Filtro visual: `films_business_clean[data_status] = final`

Formato:

- Ordenar por `roi`, descendente.
- Titulo: `Rentabilidad relativa por pelicula`

Lectura:

Las peliculas clasicas pueden destacar en ROI porque sus presupuestos fueron mucho menores.

### 3. Fans vs no fans

Visual: `Grafico de dona`.

Campos:

- Leyenda: `survey_respondents[fan_segment]`
- Valores: `survey_respondents[respondent_id]`

Configuracion:

- En `respondent_id`, usa `Recuento distinto`.
- Titulo: `Distribucion de fans en la muestra`

Lectura:

Este grafico ayuda a explicar si la encuesta puede estar sesgada hacia fans.

### 4. Peliculas mas vistas

Visual: `Grafico de barras agrupadas`.

Campos:

- Eje Y: `eda_movie_views_summary[movie_title]`
- Eje X: `eda_movie_views_summary[view_rate_pct]`

Formato:

- Ordenar por `view_rate_pct`, descendente.
- Titulo: `Peliculas mas vistas por la audiencia`
- Mostrar `view_rate_pct` como porcentaje.

Lectura:

Mide alcance de audiencia, no preferencia.

### 5. Personajes mejor valorados

Visual: `Grafico de barras agrupadas`.

Campos:

- Eje Y: `eda_character_opinion_summary[character_name]`
- Eje X: `eda_character_opinion_summary[favorable_pct]`

Filtros:

- Top N: mostrar solo los 10 primeros por `favorable_pct`.

Formato:

- Titulo: `Personajes con mejor percepcion de audiencia`

Lectura:

Sirve para conectar el analisis con campanas y merchandising.

### 6. Ranking de merchandising

Visual: `Grafico de barras agrupadas`.

Campos:

- Eje Y: `eda_character_merchandising_opportunities[character_name]`
- Eje X: `eda_character_merchandising_opportunities[merchandising_potential_index]`

Filtros:

- Top N: 10 primeros por `merchandising_potential_index`.

Formato:

- Titulo: `Personajes con mayor potencial de merchandising`

Lectura:

Este es el grafico mas conectado con la pregunta principal del proyecto.

## Pagina 1 - Resumen ejecutivo

Objetivo: que una persona no tecnica entienda el proyecto en 30 segundos.

Visuales:

- Tarjeta: `Total Respondents`
- Tarjeta: `Fans %`
- Tarjeta: `Seen Any Film %`
- Tarjeta: `Universe Assets`
- Tarjeta: `Worldwide Box Office`
- Tarjeta: `Avg Merchandising Potential`
- Tabla: `eda_conclusions`

Titulo recomendado:

`Star Wars BI: negocio, audiencia y universo narrativo`

Texto corto:

`El dashboard cruza datos narrativos, percepcion de audiencia y rendimiento comercial para priorizar oportunidades de entretenimiento y merchandising.`

## Pagina 2 - Rendimiento comercial

Visuales:

- Barras: `film_title` por `worldwide_box_office_usd`
- Barras: `film_title` por `roi`
- Dispersion: `budget_usd` en X, `worldwide_box_office_usd` en Y, `film_title` en detalles, `era` en leyenda
- Barras: `era` por `worldwide_box_office_usd`

Segmentadores:

- `era`
- `film_type`
- `data_status`

Recomendacion:

Filtra `data_status = final` si no quieres incluir `The Mandalorian and Grogu` porque tiene datos parciales.

## Pagina 3 - Audiencia y percepcion

Visuales:

- Dona: `fan_segment` por recuento distinto de `respondent_id`
- Barras: `movie_title` por `view_rate_pct`
- Barras: `movie_title` por `avg_rank`, orden ascendente
- Barras: `character_name` por `favorable_pct`

Segmentadores:

- `gender`
- `age`
- `education`
- `location_census_region`

Nota:

En ranking de peliculas, un numero menor en `avg_rank` significa mejor posicion.

## Pagina 4 - Universo narrativo

Visuales:

- Barras: `universe_assets[asset_type]` por recuento de `asset_name`
- Barras: `universe_characters_clean[species]` por recuento de `name`
- Barras: `universe_characters_clean[gender]` por recuento de `name`
- Tabla: `universe_quality_summary`

Segmentadores:

- `asset_type`
- `species`
- `gender`

## Pagina 5 - Planetas, naves y objetos

Visuales:

- Barras: `universe_planets_clean[name]` por `population`
- Barras: `universe_starships_clean[name]` por `cost_in_credits`
- Tabla: `eda_planet_business_summary`
- Tabla: `eda_starship_business_summary`

Segmentadores:

- `climate`
- `terrain`
- `manufacturer`
- `starship_class`

## Pagina 6 - Oportunidades de merchandising

Visuales:

- Barras: `character_name` por `merchandising_potential_index`
- Barras: `character_name` por `audience_affinity_score`
- Matriz con:
  - `character_name`
  - `opportunity_quadrant`
  - `favorable_pct`
  - `data_completeness_pct`
  - `merchandising_potential_index`

Segmentador:

- `opportunity_quadrant`

Mensaje:

Priorizar personajes con alta afinidad, alta familiaridad, presencia narrativa y buena calidad del dato.

## Pagina 7 - Sesgos y gobernanza

Visuales:

- Barras: `eda_governance_missing_top[column]` por `porcentaje`
- Tabla: `eda_survey_sample_bias`
- Tabla: `universe_quality_summary`

Formato:

- Ordenar nulos por `porcentaje`, descendente.
- Titulo: `Variables con mayor falta de datos`

Mensaje:

Los datos orientan decisiones, pero no son una representacion neutral ni completa.

## Pagina 8 - Recomendaciones

Visuales:

- Tabla: `eda_conclusions`
- Tabla o matriz: `eda_character_merchandising_opportunities`
- Tarjetas de texto con 3 decisiones:
  - Priorizar personajes con alta afinidad y alto potencial de merchandising.
  - Usar peliculas con alto rendimiento comercial como ancla de campana.
  - Revisar calidad del dato antes de automatizar decisiones.

## Orden recomendado de construccion

1. Crea primero la pagina `Rendimiento comercial`.
2. Despues crea `Audiencia y percepcion`.
3. Despues crea `Oportunidades de merchandising`.
4. Luego monta `Resumen ejecutivo` reutilizando los KPIs.
5. Al final crea `Gobernanza` y `Recomendaciones`.

Este orden evita bloquearse con paginas complejas antes de tener los graficos principales.
