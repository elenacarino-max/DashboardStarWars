# Star Wars Business Intelligence

Dashboard interactivo y storytelling con datos para analizar el universo Star Wars desde una perspectiva de negocio: contenido interno, percepcion de audiencia y oportunidades para campanas de merchandising.

## Objetivo del proyecto

El objetivo es construir una solucion de Business Intelligence en Power BI que ayude a una empresa ficticia de entretenimiento, streaming y merchandising a decidir que elementos del universo Star Wars tienen mayor potencial comercial.

La pregunta estrategica principal es:

> Que elementos del universo Star Wars tienen mayor potencial para campanas de contenido, merchandising, experiencias interactivas o decisiones de entretenimiento?

## Cliente ficticio

Una empresa de entretenimiento y merchandising quiere aprovechar mejor sus datos sobre Star Wars para tomar decisiones de negocio. Actualmente dispone de informacion dispersa sobre personajes, planetas, especies, naves y preferencias de audiencia, pero no cuenta con una herramienta visual que permita detectar oportunidades de forma clara para perfiles directivos no tecnicos.

## Datasets

El proyecto utiliza dos fuentes de datos:

1. **Dataset principal: universo Star Wars**
   - Personajes
   - Especies
   - Planetas
   - Naves
   - Vehiculos u otros elementos internos del universo

2. **Dataset de apoyo: encuesta de audiencia**
   - Nivel de fan
   - Peliculas vistas
   - Ranking o valoracion de peliculas
   - Valoracion de personajes
   - Variables demograficas

La union conceptual de ambos datasets permite comparar dos realidades:

- Lo que existe dentro del universo Star Wars.
- Lo que realmente conecta con la audiencia.

## Herramientas

- **Python / Pandas / NumPy**: exploracion, limpieza y preparacion de datos.
- **Jupyter Notebook**: documentacion del EDA.
- **Power BI**: dashboard ejecutivo final.
- **GitHub**: repositorio y documentacion del proyecto.

## Flujo de trabajo

1. Guardar datasets originales en `data/raw`.
2. Realizar EDA en Python.
3. Documentar nulos, duplicados, tipos de datos y primeras conclusiones.
4. Limpiar y transformar los datos.
5. Exportar CSV limpios a `data/processed`.
6. Importar los datos limpios en Power BI.
7. Crear dashboard con paginas tematicas.
8. Crear un indice de potencial de merchandising.
9. Incluir sesgos, gobernanza y recomendaciones.
10. Preparar presentacion ejecutiva de 7 minutos.

## Estructura del repositorio

```text
proy2mod2/
|-- data/
|   |-- raw/
|   |-- processed/
|-- docs/
|   |-- dashboard_plan.md
|   |-- guion_presentacion.md
|-- images/
|-- notebooks/
|   |-- 01_eda_star_wars.ipynb
|-- powerbi/
|-- src/
|-- .gitignore
|-- README.md
|-- requirements.txt
```

## Paginas previstas del dashboard

1. **Portada ejecutiva**
   - KPIs generales y pregunta de negocio.

2. **Universo Star Wars**
   - Representacion de personajes, especies, genero y planetas.

3. **Planetas, naves y potencial narrativo**
   - Localizaciones, vehiculos y elementos con atractivo comercial.

4. **Percepcion de audiencia**
   - Fans, peliculas vistas, personajes valorados y diferencias por perfil.

5. **Sesgos y gobernanza**
   - Nulos, limitaciones de muestra, representatividad y cautelas.

6. **Recomendaciones estrategicas**
   - Prioridades para campanas de merchandising y contenido.

## KPIs iniciales

- Total de personajes.
- Total de especies.
- Total de planetas.
- Total de naves o vehiculos.
- Total de respuestas de encuesta.
- Porcentaje de fans.
- Peliculas con mayor traccion.
- Personajes mejor valorados.
- Porcentaje de datos incompletos por variable critica.
- Indice de Potencial de Merchandising.

## Indice de Potencial de Merchandising

Para conectar el analisis con una decision de negocio, el proyecto incluira un KPI compuesto llamado **Indice de Potencial de Merchandising**. Este indice no pretende ser una verdad absoluta, sino una herramienta de priorizacion para comparar personajes, peliculas, planetas, especies o naves.

La logica propuesta combina cuatro dimensiones:

- **Presencia interna**: peso del elemento dentro del universo Star Wars.
- **Afinidad de audiencia**: valoracion, ranking, popularidad o recuerdo en la encuesta.
- **Potencial visual/comercial**: capacidad del elemento para convertirse en producto, campana, experiencia o pieza reconocible.
- **Confianza del dato**: penalizacion si el elemento tiene muchos nulos, poca muestra o baja calidad de informacion.

Formula conceptual:

```text
Indice de Potencial =
  Presencia interna
  + Afinidad de audiencia
  + Potencial visual/comercial
  - Penalizacion por baja calidad del dato
```

En Power BI se puede representar como ranking, tarjeta KPI o matriz comparativa.

## Cuadrante estrategico

El dashboard puede incluir un cuadrante para clasificar oportunidades:

- **Alta presencia + alta audiencia**: prioridad clara de campana.
- **Alta presencia + baja audiencia**: revisar narrativa, reposicionamiento o producto.
- **Baja presencia + alta audiencia**: oportunidad oculta o nicho con potencial.
- **Baja presencia + baja audiencia**: baja prioridad comercial.

Este enfoque ayuda a que la presentacion no termine solo con graficos, sino con una recomendacion clara de negocio.

## Sesgos a revisar

- Sesgo de representacion por genero, especie o tipo de personaje.
- Sesgo de datos incompletos en variables fisicas, planetarias o economicas.
- Sesgo de audiencia si la encuesta esta dominada por fans.
- Sesgo generacional, geografico o cultural en las respuestas.
- Sesgo de popularidad hacia personajes mas conocidos.

## Recomendaciones esperadas

El dashboard debe terminar con decisiones concretas, no solo con visualizaciones. Algunos ejemplos:

- Priorizar merchandising de personajes o peliculas con alta valoracion de audiencia.
- Detectar planetas, especies o naves con potencial visual para productos y experiencias.
- Segmentar campanas segun perfil de audiencia.
- No basar decisiones solo en popularidad; combinar presencia, percepcion y calidad del dato.
- Mejorar la calidad del dato antes de automatizar decisiones.

## Repositorio y entrega

La carpeta del proyecto ya funciona como repositorio local de Git. Lo recomendable es trabajar con repositorio desde el principio para guardar avances, documentar decisiones y evitar perder cambios.

GitHub puede crearse cuando el proyecto tenga una primera version estable:

1. Estructura de carpetas lista.
2. README inicial redactado.
3. Notebook de EDA iniciado.
4. Datasets originales ubicados o enlazados.
5. Primer commit preparado.

Si los datasets tienen licencia dudosa o pesan mucho, se documentara el enlace en el README y no se subiran los archivos originales.

## Estado del proyecto

- [ ] Datasets originales guardados en `data/raw`.
- [ ] EDA inicial completado.
- [ ] Limpieza documentada.
- [ ] CSV limpios exportados.
- [ ] Indice de Potencial de Merchandising definido.
- [ ] Cuadrante estrategico presencia/audiencia incluido.
- [ ] Dashboard Power BI creado.
- [ ] Pagina de sesgos incluida.
- [ ] Recomendaciones estrategicas redactadas.
- [ ] Capturas del dashboard anadidas.
- [ ] Presentacion oral ensayada.
- [ ] Validacion con usuario no tecnico documentada.
