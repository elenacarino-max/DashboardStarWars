# Power BI - Graficos paso a paso

Guia practica para montar **Choose Your Side - Star Wars Rebellion Lab** en Power BI.

## Antes de crear graficos

Comprueba esto en Power BI:

1. Importa `powerbi/starwars_powerbi_import.xlsx` o los CSV de `data/processed`.
2. Revisa que los campos porcentuales sean numeros decimales.
3. Ordena `strategy_audience_segments[audience_type]` por `audience_type_order`.
4. Ordena `storytelling_powerbi_pages[page_name]` por `page_order`.
5. No fuerces relaciones entre tablas resumen si no son necesarias para un visual.

## Medidas base

Crea una tabla llamada `Medidas`.

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

```DAX
Audience Segment Share % =
DIVIDE(SUM(strategy_audience_segments[share_pct]), 100)
```

```DAX
Movie View Rate % =
DIVIDE(AVERAGE(eda_movie_commercial_audience_summary[view_rate_pct]), 100)
```

```DAX
Avg Favorable % =
DIVIDE(AVERAGE(strategy_character_emotional_map[favorable_pct]), 100)
```

```DAX
Avg Unfavorable % =
DIVIDE(AVERAGE(strategy_character_emotional_map[unfavorable_pct]), 100)
```

```DAX
Worldwide Box Office =
SUM(eda_movie_commercial_audience_summary[worldwide_box_office_usd])
```

## Graficos imprescindibles

Si vas justa de tiempo, monta estos primero.

### 1. KPIs de conexion

Visual: tarjetas.

Campos:

- `[Total Respondents]`
- `[Seen Any Star Wars %]`
- `[Star Wars Fan %]`
- `[Avg Movies Seen]`

Lectura:

La muestra ya conoce Star Wars: 78,92% ha visto alguna pelicula y 66,03% se declara fan.

### 2. Segmentos Choose Your Side

Visual: barras horizontales o dona.

Campos:

- Leyenda/eje: `strategy_audience_segments[audience_type]`
- Valores: `strategy_audience_segments[respondents]`
- Tooltip: `strategic_role`, `activation_goal`

Orden:

- Ordenar por `audience_type_order`, ascendente.

Lectura:

La audiencia se divide en clanes accionables: Jedi fiel, Rebelde nostalgico, Explorador casual y Territorio neutral.

### 3. Media de peliculas vistas por segmento

Visual: columnas.

Campos:

- Eje: `audience_type`
- Valor: `avg_movies_seen`

Lectura:

Sirve para distinguir profundidad real de vinculo. El Jedi fiel consume casi toda la saga; Territorio neutral apenas entra en ella.

### 4. Mapa emocional de personajes

Visual: dispersion.

Campos:

- X: `strategy_character_emotional_map[familiarity_score]`
- Y: `strategy_character_emotional_map[audience_affinity_score]`
- Tamano: `quote_count`
- Leyenda: `brand_emotion`
- Detalles: `character_name`

Lectura:

El eje X mide reconocimiento, el eje Y mide conexion emocional y el tamano muestra presencia narrativa.

### 5. Amor vs rechazo

Visual: dispersion.

Campos:

- X: `favorable_pct`
- Y: `unfavorable_pct`
- Tamano: `opinion_responses`
- Leyenda: `polarization_risk`
- Detalles: `character_name`

Lectura:

Detecta personajes seguros y personajes polarizantes. Darth Vader puede ser potente para una experiencia premium, pero no debe leerse como personaje de afecto masivo.

### 6. Puertas de entrada por pelicula

Visual: barras horizontales.

Campos:

- Eje Y: `eda_movie_opportunities[movie_title]`
- Eje X: `eda_movie_opportunities[movie_campaign_score]`

Formato:

- Ordenar descendente por `movie_campaign_score`.
- Titulo: `Puertas de entrada al universo`.

Lectura:

`Episode V: The Empire Strikes Back` lidera como puerta emocional de la encuesta.

### 7. Popularidad vs preferencia

Visual: dispersion.

Campos:

- X: `view_rate_pct`
- Y: `preference_score`
- Tamano: `first_place_pct`
- Leyenda: `era`
- Detalles: `movie_title`

Lectura:

Permite explicar que alcance y preferencia no son la misma cosa.

### 8. Planetas como experiencias

Visual: tarjetas o tabla.

Campos:

- `strategy_planet_experiences[planet_name]`
- `brand_atmosphere`
- `experience_concept`

Lectura:

Los planetas se usan como atmosferas de campana: Tatooine es nostalgia, Hoth accion, Dagobah misterio, Coruscant tecnologia, Naboo lifestyle y Endor aventura familiar.

### 9. Naves y armas iconicas

Visuales:

- Barras: `eda_starship_business_summary[name]` por `film_count`.
- Barras: `eda_weapon_business_summary[name]` por `film_count`.

Lectura:

Millennium Falcon, X-wing y Lightsaber son activos de reconocimiento rapido.

### 10. Rutas finales de activacion

Visual: matriz.

Campos:

- Filas: `strategy_experience_routes[audience_type]`
- Valores o detalle: `entry_gate`, `key_characters`, `world`, `experience_format`, `recommended_action`

Lectura:

La campana final no es una unica pieza. Es una estrategia modular por tipo de audiencia.

## Pagina 1 - La senal perdida

Visuales:

- 4 tarjetas KPI.
- Barras de fan rate por edad.
- Barras de fan rate por genero.

Texto recomendado:

> Star Wars sigue siendo reconocible, pero la conexion activa cambia segun el publico.

## Pagina 2 - Los clanes de la galaxia

Visuales:

- Dona o barras de segmentos.
- Barras de peliculas vistas por segmento.
- Matriz de segmento por edad.
- Tabla de rol estrategico.

Texto recomendado:

> No hay una sola audiencia Star Wars. Hay clanes con puertas de entrada distintas.

## Pagina 3 - El mapa emocional de Star Wars

Visuales:

- Dispersion afinidad/familiaridad.
- Dispersion amor/rechazo.
- Tabla de emociones y usos de activacion.

Texto recomendado:

> Cada personaje activa una emocion distinta: esperanza, liderazgo, rebeldia, sabiduria, poder o humor.

## Pagina 4 - Las puertas de entrada al universo

Visuales:

- Ranking por `movie_campaign_score`.
- Dispersion `view_rate_pct` vs `preference_score`.
- Dispersion negocio vs audiencia.
- Tabla de detalle por pelicula.

Texto recomendado:

> La mejor puerta no es siempre la mayor taquilla. Es la que combina alcance y conexion emocional.

## Pagina 5 - Planetas como experiencias

Visuales:

- Tarjetas de experiencias.
- Barras por `film_count`.
- Barras por `resident_count`.

Texto recomendado:

> Elegir un planeta es elegir que sensacion vivira el publico.

## Pagina 6 - Tecnologia, poder y velocidad

Visuales:

- Naves por presencia.
- Naves por clase.
- Coste vs presencia.
- Armas iconicas.

Texto recomendado:

> Los personajes crean apego; las naves y armas crean espectaculo.

## Pagina 7 - La estrategia de reactivacion

Visuales:

- Matriz final de rutas.
- Tarjetas por segmento.
- Tabla de conclusiones.
- Bloque breve de sesgos.

Texto recomendado:

> Star Wars no necesita una campana unica. Necesita una galaxia de experiencias.

## Formato recomendado

- Fondo oscuro discreto.
- Dorado para oportunidad o decision final.
- Azul para Jedi, heroes y lectura positiva.
- Rojo solo para riesgo, sesgo o Lado Oscuro.
- Verde o cian para tecnologia y rutas casuales.
- Una frase de lectura por pagina.
- Maximo 3 o 4 visuales principales por pagina.

## Checklist final de Power BI

- [ ] Importar las tablas actualizadas.
- [ ] Ordenar segmentos por `audience_type_order`.
- [ ] Crear medidas base.
- [ ] Revisar porcentajes como `%`.
- [ ] Revisar moneda como USD.
- [ ] Confirmar que `strategy_*` aparece en el modelo.
- [ ] Refrescar el `.pbix` tras regenerar CSV o Excel.
- [ ] Validar que la pagina final muestra las 4 rutas de audiencia.
- [ ] Incluir sesgos: 78,92% ha visto alguna pelicula y 66,03% se declara fan.
