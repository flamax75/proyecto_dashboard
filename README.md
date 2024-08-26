

# Proyecto Dashboard Científico de COVID-19

Este proyecto consiste en la creación de un dashboard científico que permite visualizar y analizar datos relacionados con el COVID-19. El proyecto está compuesto por tres ejercicios que incluyen el procesamiento de datos, la visualización de gráficos interactivos y el análisis de resultados.

## Estructura del Proyecto

La estructura del proyecto es la siguiente:

```
proyecto_dashboard/
├── data/
│   └── data.csv                       # Archivo CSV con los datos de entrada
├── outputs/
│   └── resultados.json                # Archivo JSON generado por el ejercicio 1
└── src/
    ├── ejercicio_1.py                 # Script que procesa los datos y genera resultados.json
    ├── ejercicio_2.py                 # Script que genera gráficos interactivos
    └── ejercicio_3.py                 # Script que genera gráficos de máximos por categoría
```

## Ejercicio 1: Procesamiento de Datos

Este ejercicio toma los datos de un archivo CSV (`data.csv`), los agrupa por día de la semana y por provincia, y calcula los acumulados de defunciones, nuevos casos, hospitalizados y UCI. Los resultados se almacenan en un archivo JSON (`resultados.json`).

### Ejecución

```bash
python src/ejercicio_1.py
```

Este comando leerá el archivo `data.csv`, procesará los datos y generará el archivo `resultados.json` en la carpeta `outputs/`.

## Ejercicio 2: Visualización Interactiva de Datos

Este ejercicio proporciona un menú interactivo para visualizar gráficos basados en los datos procesados en el ejercicio 1. Las opciones incluyen gráficos de defunciones, casos, hospitalizados y UCI por provincia.

### Ejecución

```bash
python src/ejercicio_2.py
```

Después de ejecutar este comando, se te presentará un menú en la consola donde podrás elegir qué gráfica visualizar. Los gráficos se cerrarán automáticamente después de mostrarse.

### Opciones del Menú

1. Defunciones
2. Casos
3. Hospitalizados
4. UCI
5. Salir

## Ejercicio 3: Análisis de Máximos

Este ejercicio analiza los datos para identificar la provincia con el máximo valor en cada categoría (defunciones, casos, hospitalizados, UCI) y genera gráficos de pastel para cada uno.

### Ejecución

```bash
python src/ejercicio_3.py
```

Después de ejecutar este comando, se te presentará un menú interactivo similar al del ejercicio 2. Selecciona una categoría para ver la gráfica de pastel que muestra la provincia con el máximo valor.

### Opciones del Menú

1. Provincia con más defunciones
2. Provincia con más casos
3. Provincia con más hospitalizados
4. Provincia con más UCI
5. Salir

## Requisitos

Antes de ejecutar los scripts, asegúrate de tener instaladas las dependencias necesarias:

```bash
pip install -r requirements.txt
```

**Nota:** El archivo `requirements.txt` debe incluir `matplotlib` y cualquier otra dependencia que se necesite.

## Notas Finales

- Asegúrate de que el archivo `data.csv` esté en la carpeta `data/` antes de ejecutar el ejercicio 1.
- Los gráficos generados se cerrarán automáticamente después de mostrarse, lo que permite una interacción fluida con el menú.
- Si encuentras algún problema, asegúrate de que todos los archivos estén en las ubicaciones correctas y de que los nombres de las columnas en `data.csv` coincidan con los utilizados en los scripts.
