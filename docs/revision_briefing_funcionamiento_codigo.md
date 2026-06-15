# Revision del proyecto, funcionamiento y codigo

Fecha de revision: 2026-06-13

Nuevo enfoque revisado: `C:\Users\elena\Downloads\nuevo_enfoque_proy2.docx`

## Resumen ejecutivo

El proyecto se ha adaptado al nuevo enfoque **Choose Your Side - Star Wars Rebellion Lab**.

La idea anterior estaba centrada en seleccionar oportunidades comerciales y de merchandising. La nueva version es mas estrategica: usa las mismas tablas para decidir que experiencia Star Wars debe recibir cada tipo de audiencia.

El dashboard queda planteado como una herramienta de reactivacion de marca:

> Star Wars no necesita una unica campana. Necesita una galaxia de experiencias, disenada para que cada publico elija su lado.

## Cambio principal de enfoque

Antes:

- Pregunta central: que elementos del universo tienen mayor potencial comercial.
- Cierre: una campana de producto.
- Lectura: personajes, peliculas y activos como oportunidades de merchandising.

Ahora:

- Pregunta central: que experiencia Star Wars reactiva a cada tipo de publico.
- Cierre: estrategia modular por segmentos.
- Lectura: audiencia, personajes, peliculas, planetas, naves y simbolos como rutas de conexion emocional.

## Nuevas tablas generadas

El script `scripts/build_rebellion_lab_outputs.py` crea una capa estrategica en `data/processed`:

| Tabla | Estado | Uso |
|---|---|---|
| `strategy_audience_segments.csv` | Creada | Segmentos Jedi fiel, Rebelde nostalgico, Explorador casual y Territorio neutral |
| `strategy_audience_age_matrix.csv` | Creada | Segmento x edad |
| `strategy_survey_respondents.csv` | Creada | Encuestados con `audience_type` calculado |
| `strategy_character_emotional_map.csv` | Creada | Personajes como emociones de marca |
| `strategy_planet_experiences.csv` | Creada | Planetas como conceptos de experiencia |
| `strategy_experience_routes.csv` | Creada | Rutas finales por tipo de publico |
| `storytelling_powerbi_pages.csv` | Actualizada | Nuevo orden de paginas |
| `story_featured_assets.csv` | Actualizada | Activos narrativos para experiencias |
| `story_campaign_lines.csv` | Actualizada | Matriz final de campana |
| `eda_conclusions.csv` | Actualizada | Conclusiones ejecutivas |

## Nuevo dashboard propuesto

1. **La senal perdida**
   - Mide conexion activa con Star Wars.

2. **Los clanes de la galaxia**
   - Segmenta la audiencia en 4 tipos accionables.

3. **El mapa emocional de Star Wars**
   - Traduce personajes en emociones de marca.

4. **Las puertas de entrada al universo**
   - Analiza que peliculas abren mejor la conversacion.

5. **Planetas como experiencias**
   - Convierte mundos en atmosferas de campana.

6. **Tecnologia, poder y velocidad**
   - Usa naves, vehiculos y armas como activos de espectaculo.

7. **La estrategia de reactivacion**
   - Cierra con rutas por segmento y lectura critica.

## Hallazgos que sostienen la historia

- La muestra tiene 1.186 encuestados.
- 78,92% declara haber visto alguna pelicula.
- 66,03% se declara fan.
- El segmento `Jedi fiel` tiene 443 respuestas.
- El segmento `Territorio neutral` tiene 400 respuestas y consumo muy bajo.
- `Episode V: The Empire Strikes Back` sigue siendo la puerta emocional mas fuerte de la encuesta.
- Han Solo lidera afinidad y representa rebeldia.
- Luke Skywalker representa esperanza.
- Leia Organa representa liderazgo.
- Yoda representa sabiduria.
- Darth Vader representa poder, pero con riesgo de polarizacion.
- Lightsaber, Millennium Falcon y X-wing son activos visuales de reconocimiento rapido.

## Funcionamiento del programa

La tuberia actual queda asi:

```text
data/raw
   -> notebooks/01_limpieza_star_wars.ipynb
   -> data/processed/*_clean.csv
   -> notebooks/02_eda_storytelling_star_wars.ipynb
   -> data/processed/eda_*.csv
   -> scripts/build_rebellion_lab_outputs.py
   -> data/processed/strategy_*.csv + story_*.csv
   -> scripts/build_powerbi_import_workbook.mjs
   -> powerbi/starwars_powerbi_import.xlsx
   -> Power BI
```

## Comandos de regeneracion

En un entorno con Python y dependencias instaladas:

```powershell
python scripts\build_rebellion_lab_outputs.py
```

Para regenerar el workbook de importacion con el runtime empaquetado de Codex:

```powershell
$env:NODE_PATH = 'C:\Users\elena\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\node_modules'
& 'C:\Users\elena\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin\node.exe' 'scripts\build_powerbi_import_workbook.mjs'
```

Comando recomendado actual:

```powershell
.\scripts\run_rebellion_lab_pipeline.ps1
```

Este comando usa Python local si existe. Si Windows no tiene `python` o `py`, usa el Python empaquetado de Codex y despues regenera el workbook de Power BI.

## Revision de codigo

### P2 - Los entornos Python locales estaban rotos

Se intento ejecutar:

```powershell
python scripts\build_rebellion_lab_outputs.py
```

pero `python` no esta en el PATH. Tambien se probaron:

```powershell
.venv\Scripts\python.exe
venv\Scripts\python.exe
```

Ambos entornos apuntan a rutas antiguas de Python que ya no existen despues del reinstalado/formateo.

Impacto:

- El proyecto funciona con el runtime empaquetado de Codex.
- Se ha anadido `scripts/run_rebellion_lab_pipeline.ps1` para ejecutar la capa estrategica aunque no exista Python de sistema.
- Para uso normal fuera de Codex, sigue siendo recomendable recrear el entorno virtual.

Recomendacion:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Si `py` tampoco esta instalado, instalar Python y recrear `.venv`.

### P2 - El generador de Excel depende del runtime de Codex

Archivo: `scripts/build_powerbi_import_workbook.mjs`.

El script usa `@oai/artifact-tool` desde `NODE_PATH`. Funciona con el runtime empaquetado de Codex, pero no con un Node generico sin esa dependencia.

Impacto:

- El `.xlsx` se puede regenerar en esta sesion.
- Otra persona necesitara importar CSV individuales o tener documentado el comando con `NODE_PATH`.

Recomendacion:

- Mantener el Excel ya generado para la entrega.
- Documentar el comando exacto.
- Si el proyecto debe ejecutarse fuera de Codex, crear una alternativa Python con `openpyxl` o importar CSV individuales en Power BI.

### P3 - `notebooks/prueba.py` sigue siendo exploratorio

El archivo no forma parte de la tuberia final documentada.

Recomendacion:

- Dejarlo fuera de la presentacion.
- Renombrarlo como utilidad de diagnostico o eliminarlo en una limpieza posterior.

## Validaciones realizadas

- Se leyo el nuevo briefing `nuevo_enfoque_proy2.docx`.
- Se genero la nueva capa `strategy_*.csv`.
- Se actualizaron las tablas narrativas `story_*.csv`.
- Se actualizaron README y documentacion principal.
- Se dejo una guia de montaje, visualizacion, modelo y graficos coherente con `Choose Your Side`.
- Se detecto el problema de entornos Python locales rotos.

## Riesgo residual

No se puede validar visualmente el archivo `.pbix` desde aqui sin Power BI Desktop. La revision final debe hacerse abriendo `powerbi/graficos_PBI.pbix`, refrescando datos y comprobando que las paginas usan las tablas nuevas.

## Checklist antes de entregar

1. Abrir `powerbi/graficos_PBI.pbix`.
2. Refrescar datos desde `powerbi/starwars_powerbi_import.xlsx` o desde los CSV.
3. Cambiar paginas antiguas por las 7 paginas nuevas.
4. Revisar que aparecen los cuatro segmentos.
5. Anadir la nota de sesgos: 78,92% ha visto alguna pelicula y 66,03% se declara fan.
6. Confirmar que Hoth y Dagobah se muestran como activos narrativos, no como ranking cuantitativo.
7. Exportar capturas a `images/` si la entrega las pide.
