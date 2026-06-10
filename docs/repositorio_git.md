# Como trabajar el repositorio

## Recomendacion

No hace falta esperar al final para crear el repositorio. Lo mejor es usar Git desde el principio y subir a GitHub cuando haya una primera version presentable.

Esta carpeta ya tiene Git local inicializado, asi que el repositorio local ya existe. Lo que faltaria mas adelante es crear el repositorio remoto en GitHub y conectarlo.

## Fases recomendadas

### Fase 1: ahora

- Crear estructura de carpetas.
- Redactar README inicial.
- Preparar notebook de EDA.
- Guardar el guion y el plan del dashboard.
- Hacer el primer commit.

### Fase 2: cuando esten los datasets

- Poner los CSV en `data/raw`.
- Revisar licencias y peso de archivos.
- Si se pueden publicar, subirlos.
- Si no se pueden publicar, dejar solo enlace y descripcion en README.

### Fase 3: despues del EDA

- Exportar CSV limpios a `data/processed`.
- Documentar limpieza y decisiones.
- Actualizar README con hallazgos reales.
- Hacer otro commit.

### Fase 4: despues de Power BI

- Guardar `.pbix` en `powerbi`.
- Anadir capturas en `images`.
- Documentar paginas, medidas y filtros.
- Preparar entrega final.

## Que no conviene subir

- Archivos con datos privados.
- Datasets con licencia dudosa.
- Archivos temporales de Power BI.
- Entornos virtuales de Python.
- Archivos muy pesados si GitHub no los acepta bien.

## Primer commit sugerido

Mensaje:

```text
Initial Star Wars BI project structure
```
