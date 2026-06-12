# Plan del dashboard Power BI

## Pregunta ejecutiva

Que elementos del universo Star Wars tienen mayor potencial para campanas de merchandising, contenido y experiencias interactivas?

## Narrativa

El dashboard debe contar una historia sencilla:

1. Que activos tiene el universo Star Wars.
2. Que elementos parecen tener mas peso narrativo o comercial.
3. Que opina la audiencia.
4. Que rendimiento comercial han tenido las peliculas.
5. Que oportunidades aparecen al cruzar presencia interna, traccion de audiencia y negocio.
6. Que sesgos limitan la lectura.
7. Que decisiones deberia tomar la empresa.

## Pagina 1: Portada ejecutiva

Objetivo: situar rapidamente al publico.

Elementos:

- Titulo del proyecto.
- Cliente ficticio.
- Pregunta estrategica.
- KPIs generales.

KPIs posibles:

- Total de personajes.
- Total de especies.
- Total de planetas.
- Total de naves o vehiculos.
- Total de respuestas de encuesta.
- Porcentaje de fans.
- Taquilla mundial total.
- ROI medio.
- Indice de Potencial de Merchandising.

## Pagina 2: Universo Star Wars

Objetivo: entender la composicion interna del universo.

Graficos sugeridos:

- Personajes por especie.
- Personajes por genero.
- Personajes por planeta de origen.
- Distribucion de altura o masa.

Filtros:

- Genero.
- Especie.
- Planeta de origen.

Pregunta de negocio:

> Que grupos y personajes dominan la representacion del universo Star Wars?

## Pagina 3: Planetas, naves y oportunidades narrativas

Objetivo: identificar elementos con potencial visual, narrativo o comercial.

Graficos sugeridos:

- Top planetas por poblacion.
- Planetas por clima o terreno.
- Naves por coste.
- Naves por capacidad, velocidad o fabricante.

Filtros:

- Clima.
- Terreno.
- Fabricante.
- Clase de nave.

Pregunta de negocio:

> Que localizaciones y vehiculos tienen mayor potencial para campanas, productos o experiencias interactivas?

## Pagina 4: Percepcion de audiencia

Objetivo: medir que conecta con el publico.

Graficos sugeridos:

- Porcentaje de personas que se consideran fans.
- Peliculas mas vistas.
- Ranking de peliculas.
- Personajes mejor valorados.
- Diferencias por edad, genero o nivel educativo.

Filtros:

- Fan / no fan.
- Edad.
- Genero.
- Educacion.
- Ingresos.
- Region.

Pregunta de negocio:

> Que contenido conecta mejor con la audiencia?

## Pagina 5: Rendimiento comercial de la franquicia

Objetivo: incorporar una lectura claramente de negocio.

Tabla principal:

- `films_business_clean.csv`

Graficos sugeridos:

- Taquilla mundial por pelicula.
- Presupuesto frente a taquilla mundial.
- ROI por pelicula.
- Taquilla mundial por era.
- Comparativa entre peliculas clasicas, precuelas, secuelas, spin-offs y nuevas.

Advertencia:

- `The Mandalorian and Grogu` se marca como `partial_current_release`, porque sus datos de taquilla son recientes y pueden cambiar.

Pregunta de negocio:

> Que peliculas han generado mas valor economico y como se relaciona eso con la percepcion de audiencia?

## Pagina 6: Oportunidades de merchandising

Objetivo: convertir el analisis en una herramienta de priorizacion comercial.

Elemento central:

- Indice de Potencial de Merchandising.

Logica del indice:

- Presencia interna del elemento en el universo.
- Afinidad o valoracion de audiencia.
- Potencial visual/comercial para merchandising, campanas o experiencias.
- Penalizacion por baja calidad del dato o muestra insuficiente.

Graficos sugeridos:

- Ranking de elementos con mayor potencial.
- Cuadrante de presencia interna frente a afinidad de audiencia.
- Tabla de oportunidades con explicacion ejecutiva.

Lectura del cuadrante:

- Alta presencia + alta audiencia: prioridad clara de campana.
- Alta presencia + baja audiencia: reposicionamiento o revision narrativa.
- Baja presencia + alta audiencia: oportunidad oculta.
- Baja presencia + baja audiencia: baja prioridad comercial.

Pregunta de negocio:

> Que elementos deberian priorizarse en una campana de merchandising?

## Pagina 7: Sesgos y gobernanza

Objetivo: demostrar lectura critica de los datos.

Elementos:

- Tabla o matriz de porcentaje de nulos.
- Variables con mayor incompletitud.
- Advertencias de representatividad.
- Riesgos si la empresa toma decisiones sin revisar los sesgos.

Sesgos a revisar:

- Representacion desigual de generos, especies o personajes.
- Datos incompletos en variables como masa, altura, poblacion o coste.
- Encuesta dominada por fans.
- Posible sesgo generacional, geografico o cultural.
- Popularidad concentrada en personajes principales.

Mensaje clave:

> Los datos orientan decisiones, pero no son una representacion neutral ni completa de la realidad.

## Pagina 8: Recomendaciones estrategicas

Objetivo: cerrar con decisiones accionables.

Recomendaciones posibles:

- Priorizar personajes y peliculas con alta valoracion de audiencia.
- Usar planetas, especies y naves de alto potencial visual en campanas.
- Activar primero los elementos situados en el cuadrante de alta presencia y alta audiencia.
- Explorar oportunidades ocultas con baja presencia pero alta afinidad.
- Crear campanas diferenciadas para audiencias fan y no fan.
- Revisar la calidad del dato antes de automatizar decisiones.
- Combinar presencia interna, percepcion externa y fiabilidad del dato.
