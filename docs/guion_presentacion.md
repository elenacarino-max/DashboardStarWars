# Guion de presentacion oral - 7 minutos

## 0:00 - 1:00 Contexto y problema

Buenos dias. Mi proyecto se llama Star Wars Business Intelligence y consiste en un dashboard interactivo creado en Power BI para analizar el universo Star Wars desde una perspectiva de negocio.

El cliente ficticio es una empresa de entretenimiento, streaming y merchandising que quiere tomar mejores decisiones sobre que personajes, peliculas, planetas o elementos del universo Star Wars pueden tener mas potencial comercial.

El problema principal es que la informacion existe, pero esta dispersa. Por un lado tenemos datos internos del universo Star Wars y por otro lado datos de audiencia. El objetivo es convertir esos datos en una herramienta visual que ayude a decidir que contenidos o campanas priorizar.

## 1:00 - 2:00 Datasets y metodologia

He trabajado con dos datasets.

El primero recoge informacion del universo Star Wars: personajes, especies, planetas, naves y otras variables del contenido.

El segundo recoge informacion de audiencia mediante una encuesta: peliculas vistas, nivel de fan, valoracion de personajes y variables demograficas.

Antes de construir el dashboard hice un EDA en Python. En este analisis revise el tamano de los datasets, los tipos de columnas, los valores nulos, los duplicados, las variables numericas y categoricas, y las primeras relaciones entre variables.

Despues limpie los datos y exporte versiones preparadas para Power BI.

## 2:00 - 4:30 Demo del dashboard

En la primera pagina del dashboard se muestra una vision general con los principales indicadores: numero de personajes, especies, planetas, naves y respuestas de audiencia.

En la segunda pagina analizo la composicion del universo Star Wars. Aqui se pueden ver los personajes agrupados por especie, genero o planeta de origen. Esta parte ayuda a entender que grupos estan mas representados.

En la tercera pagina analizo planetas, naves y otros elementos con potencial narrativo o comercial. Por ejemplo, se pueden identificar planetas con mayor poblacion, naves con mayor coste o elementos que podrian destacar en campanas de merchandising.

En la cuarta pagina se analiza la percepcion de la audiencia. Aqui se observa que peliculas han sido mas vistas, que personajes tienen mejor valoracion y como cambia la opinion segun variables como edad, genero o nivel de fan.

Despues incorporo una pagina de oportunidades de merchandising. En esta parte no solo miro popularidad, sino que combino presencia interna, afinidad de audiencia, potencial visual y calidad del dato para construir un indice de priorizacion. La lectura principal es un cuadrante: los elementos con alta presencia y alta audiencia son prioridades claras; los elementos con baja presencia pero alta audiencia pueden ser oportunidades ocultas.

Los filtros permiten que un usuario no tecnico explore los datos de forma sencilla, sin modificar codigo.

## 4:30 - 5:45 Sesgos y gobernanza

Una parte importante del proyecto es la gobernanza del dato.

He detectado varias limitaciones. En primer lugar, algunos campos del dataset tienen valores desconocidos o incompletos, por ejemplo en variables fisicas de personajes o caracteristicas de planetas y naves.

En segundo lugar, puede existir sesgo de representacion, ya que algunos tipos de personajes, especies o generos aparecen mucho mas que otros.

En tercer lugar, el dataset de encuesta tambien puede tener sesgo de muestra. Si la mayoria de respuestas vienen de personas muy fans de Star Wars, las conclusiones pueden no representar al publico general.

Por eso, el dashboard incluye una seccion de advertencias para recordar que los datos ayudan a decidir, pero no deben interpretarse como una verdad absoluta.

## 5:45 - 6:45 Recomendaciones estrategicas

A partir del analisis, propongo varias recomendaciones.

La primera es priorizar campanas con personajes y peliculas que combinen alta presencia en el universo y buena valoracion por parte de la audiencia.

La segunda es utilizar el Indice de Potencial de Merchandising para seleccionar los elementos que combinan atractivo comercial, traccion de audiencia y fiabilidad del dato.

La tercera es aprovechar planetas, especies o naves con potencial visual para productos de merchandising, videojuegos o experiencias interactivas.

La cuarta es revisar los datos incompletos antes de tomar decisiones automatizadas, porque una mala calidad del dato puede llevar a conclusiones equivocadas.

La quinta es segmentar las campanas segun el perfil de audiencia, porque no todos los grupos valoran igual las mismas peliculas o personajes.

## 6:45 - 7:00 Cierre

En conclusion, este dashboard permite transformar datos dispersos sobre Star Wars en una herramienta de decision clara, visual e interactiva.

El valor principal del proyecto no esta solo en los graficos, sino en convertir los datos en una historia util para negocio: que elementos tienen mas potencial, que prefiere la audiencia y que limitaciones deben tenerse en cuenta antes de decidir.

## Frase de cierre

Este proyecto demuestra que incluso un universo ficticio como Star Wars puede analizarse con criterios reales de inteligencia de negocio: datos, audiencia, sesgos y decisiones estrategicas.
