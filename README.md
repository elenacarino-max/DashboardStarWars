# Choose Your Side - Star Wars Rebellion Lab

Dashboard interactivo en Power BI para analizar como reactivar la conexion emocional entre Star Wars y distintos tipos de audiencia. El proyecto ya no se plantea como una simple decision de merchandising, sino como una estrategia de marca basada en datos:

> Que tipo de experiencia Star Wars deberiamos crear para reconquistar a cada tipo de publico?

La idea central es **Choose Your Side**: una misma marca, varias rutas de conexion. El fan fiel busca profundidad, el nostalgico busca emocion, el casual busca reconocimiento y el publico neutral necesita una entrada simple.

## Vista del dashboard

<img width="1372" height="805" alt="estrategia de activacion" src="https://github.com/user-attachments/assets/fff81fd2-7d65-4b04-8ab1-29efb566b85b" />


## Cliente ficticio

Una empresa de entretenimiento quiere relanzar Star Wars con una estrategia mas original que una campana unica de productos. Necesita entender que segmentos de audiencia siguen conectados con la saga, que peliculas funcionan como puertas de entrada, que personajes activan emociones de marca y que mundos, naves o simbolos pueden convertirse en experiencias memorables.

## Datasets

El proyecto mantiene las mismas fuentes del enfoque anterior:

1. **Universo Star Wars**
   - Personajes, peliculas, planetas, especies, naves, vehiculos, armas, droides y frases.

2. **Encuesta de audiencia**
   - Nivel de fan, peliculas vistas, ranking de peliculas, valoracion de personajes y variables demograficas.

3. **Rendimiento comercial de peliculas**
   - Presupuesto estimado, taquilla domestica, taquilla mundial, beneficio estimado, ROI, era y tipo de pelicula.

La tabla comercial se guarda como `data/raw/films_business.csv` y usa como referencia principal The Numbers:

```text
https://www.the-numbers.com/movies/franchise/Star-Wars
```

## Herramientas

- **Python / Pandas / NumPy**: limpieza, EDA y generacion de tablas estrategicas.
- **Jupyter Notebook**: documentacion del proceso analitico.
- **Power BI**: dashboard ejecutivo final.
- **Excel de importacion**: workbook con todos los CSV procesados para facilitar la carga.
- **GitHub**: repositorio y documentacion del proyecto.

## Flujo de trabajo

1. Guardar datasets originales en `data/raw`.
2. Ejecutar `notebooks/01_limpieza_star_wars.ipynb`.
3. Exportar CSV limpios a `data/processed`.
4. Ejecutar `notebooks/02_eda_storytelling_star_wars.ipynb`.
5. Ejecutar `scripts/build_rebellion_lab_outputs.py`.
6. Regenerar `powerbi/starwars_powerbi_import.xlsx` con `scripts/build_powerbi_import_workbook.mjs`.
7. Importar en Power BI las tablas indicadas en `docs/powerbi_montaje_y_medidas_choose_your_side.md`.
8. Montar las 7 paginas de `Choose Your Side`.
9. Revisar sesgos, calidad del dato y lectura critica.
10. Preparar la presentacion ejecutiva de 7 minutos.

Comando recomendado si `python` no esta instalado en Windows:

```powershell
.\scripts\run_rebellion_lab_pipeline.ps1
```

Este runner busca primero Python local y, si no existe, usa el runtime empaquetado de Codex. Tambien regenera el workbook de Power BI.

## Como reproducir el proyecto

El proyecto ya incluye los CSV procesados, el workbook de importacion y el archivo `.pbix`. Si solo quieres revisar el resultado final, abre `powerbi/graficos_PBI.pbix` en Power BI Desktop y refresca los datos desde `powerbi/starwars_powerbi_import.xlsx`.

Para regenerar la parte analitica desde cero en Windows:

```powershell
python -m pip install -r requirements.txt
.\scripts\run_rebellion_lab_pipeline.ps1
```

Ese comando:

1. Regenera las tablas estrategicas en `data/processed`.
2. Actualiza las tablas `strategy_*.csv` y `story_*.csv`.
3. Regenera `powerbi/starwars_powerbi_import.xlsx` cuando hay Node.js disponible.

Si no tienes Node.js o no estas trabajando desde Codex, puedes regenerar solo la parte Python:

```powershell
.\scripts\run_rebellion_lab_pipeline.ps1 -SkipWorkbook
```

Despues de ejecutar el pipeline, el ultimo paso sigue siendo manual: abrir `powerbi/graficos_PBI.pbix`, refrescar datos y revisar visualmente las paginas del dashboard.

## Tablas nuevas del enfoque Rebellion Lab

Estas tablas se generan desde los CSV ya existentes y son la capa principal para la nueva narrativa:

| Tabla | Uso |
|---|---|
| `strategy_audience_segments.csv` | Segmentos de audiencia: Jedi fiel, Rebelde nostalgico, Explorador casual y Territorio neutral. |
| `strategy_audience_age_matrix.csv` | Cruce de tipo de audiencia con edad. |
| `strategy_survey_respondents.csv` | Encuestados con columna `audience_type` ya calculada. |
| `strategy_character_emotional_map.csv` | Personajes como emociones de marca: esperanza, liderazgo, rebeldia, sabiduria, poder, humor, etc. |
| `strategy_planet_experiences.csv` | Planetas convertidos en conceptos de experiencia. |
| `strategy_experience_routes.csv` | Rutas finales de activacion por tipo de publico. |

Tambien se actualizan las tablas narrativas:

- `storytelling_powerbi_pages.csv`
- `story_featured_assets.csv`
- `story_campaign_lines.csv`
- `eda_conclusions.csv`

## Paginas del dashboard

1. **La senal perdida**
   - Mide si existe conexion activa con Star Wars y donde sigue viva.

2. **Los clanes de la galaxia**
   - Segmenta la audiencia en Jedi fiel, Rebelde nostalgico, Explorador casual y Territorio neutral.

3. **El mapa emocional de Star Wars**
   - Convierte personajes en territorios emocionales de marca.

4. **Las puertas de entrada al universo**
   - Analiza que peliculas abren mejor la conversacion con cada publico.

5. **Planetas como experiencias**
   - Traduce mundos como Tatooine, Hoth, Dagobah, Coruscant, Naboo o Endor en atmosferas de campana.

6. **Tecnologia, poder y velocidad**
   - Agrupa naves, vehiculos y armas como activos de accion e impacto visual.

7. **La estrategia de reactivacion**
   - Recomienda una campana modular: una marca, varias rutas de conexion.

## Hallazgos principales

- La muestra tiene 1.186 encuestados.
- 78,92% declara haber visto alguna pelicula de Star Wars.
- 66,03% se declara fan.
- `Jedi fiel` es el segmento mas grande de la nueva clasificacion: 443 respuestas.
- `Territorio neutral` tambien es relevante: 400 respuestas y consumo casi nulo, por lo que necesita una entrada simple.
- `Episode V: The Empire Strikes Back` sigue siendo la puerta emocional mas fuerte dentro de la encuesta.
- Han Solo lidera la afinidad total y se interpreta como territorio de **rebeldia**.
- Luke Skywalker activa **esperanza**, Leia **liderazgo**, Yoda **sabiduria** y Darth Vader **poder** con riesgo de polarizacion.
- Lightsaber, Millennium Falcon y X-wing funcionan como simbolos transversales de reconocimiento rapido.

## Sesgos a revisar

Las recomendaciones son direccionales, no una prediccion exacta del publico general.

- La encuesta esta inclinada hacia personas que ya conocen Star Wars.
- 78,92% ha visto al menos una pelicula y 66,03% se declara fan.
- El fan de universo expandido tiene muchos nulos, asi que no conviene extraer conclusiones fuertes sobre series o videojuegos.
- Costes de naves y armas tienen incompletitud relevante, por lo que deben usarse como contexto secundario.
- Hoth y Dagobah son activos narrativos en `story_featured_assets.csv`; no deben presentarse como ganadores cuantitativos del ranking de planetas.

En Power BI, esta lectura debe aparecer en la pagina 7 como bloque visual de sesgos desde `eda_survey_bias_visual.csv` y como conclusion ejecutiva en `eda_conclusions.csv`.

## Estructura del repositorio

```text
DashboardStarWars/
|-- data/
|   |-- raw/
|   |-- processed/
|-- docs/
|   |-- dashboard_plan.md
|   |-- guion_presentacion.md
|   |-- powerbi_montaje_y_medidas_choose_your_side.md
|-- images/
|   |-- capturas finales del dashboard, si la entrega las pide
|-- notebooks/
|   |-- 01_limpieza_star_wars.ipynb
|   |-- 02_eda_storytelling_star_wars.ipynb
|-- powerbi/
|   |-- graficos_PBI.pbix
|   |-- starwars_powerbi_import.xlsx
|-- scripts/
|   |-- build_rebellion_lab_outputs.py
|   |-- build_powerbi_import_workbook.mjs
|   |-- run_rebellion_lab_pipeline.ps1
|-- README.md
|-- requirements.txt
```

## Archivos locales no versionados

- `docx/` queda reservado para borradores o entregables Word locales y esta ignorado en `.gitignore` de momento.
- `images/` se mantiene versionada como carpeta preparada para capturas finales del dashboard.

## Estado del proyecto

- [x] Datasets originales guardados en `data/raw`.
- [x] Limpieza y normalizacion documentadas.
- [x] CSV limpios exportados a `data/processed`.
- [x] EDA orientado a storytelling creado.
- [x] Tabla comercial `films_business.csv` anadida.
- [x] Segmentos de audiencia `Choose Your Side` generados.
- [x] Mapa emocional de personajes generado.
- [x] Rutas de experiencia por audiencia generadas.
- [x] Paginas Power BI redefinidas para Rebellion Lab.
- [x] Tabla de sesgos incluida.
- [x] Sesgo integrado en el cierre ejecutivo y en la pagina final.
- [x] Recomendaciones estrategicas redactadas.
- [x] Workbook de importacion para Power BI generado.
- [x] Runner PowerShell creado para usar Python local o Python empaquetado de Codex.
- [x] Revisar visualmente `powerbi/graficos_PBI.pbix` en Power BI Desktop tras refrescar datos.
- [x] Anadir capturas finales del dashboard en `images/` si la entrega las pide.

## Mas documentacion

La carpeta `docx/` contiene los documentos finales de apoyo del proyecto.
