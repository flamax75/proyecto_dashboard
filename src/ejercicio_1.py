
import csv
import json
from collections import defaultdict
from datetime import datetime
import os

# Crear una estructura de datos para almacenar los resultados
results = defaultdict(lambda: defaultdict(lambda: {
    "num_def": 0,
    "new_cases": 0,
    "num_hosp": 0,
    "num_uci": 0
}))

# Ruta al archivo CSV
csv_file_path = 'C:/Users/Usuario/Documents/proyecto_dashboard/data/data.csv'
json_file_path = 'C:/Users/Usuario/Documents/proyecto_dashboard/outputs/resultados.json'

# Verificar si el archivo CSV está vacío
if os.stat(csv_file_path).st_size == 0:
    print("El archivo CSV está vacío. Por favor, agrega datos antes de continuar.")
else:
    # Leer el archivo CSV con codificación adecuada
    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        # Mostrar los encabezados
        print("Encabezados encontrados en el archivo CSV:")
        print(reader.fieldnames)

        # Mostrar cada fila del CSV
        print("\nDatos del archivo CSV:")
        for row in reader:
            print(row)  # Imprime cada fila tal como está en el CSV

            # Convertir la fecha y extraer el día de la semana
            # Cambiar 'fecha' por 'date'
            date = datetime.strptime(row['date'], '%Y-%m-%d')
            day_of_week = date.strftime('%A')
            province = row['province']  # Cambiar 'provincia' por 'province'

            # Sumarizar los datos por día de la semana y provincia
            results[day_of_week][province]['num_def'] += int(row['num_def'])
            results[day_of_week][province]['new_cases'] += int(
                row['new_cases'])
            results[day_of_week][province]['num_hosp'] += int(row['num_hosp'])
            results[day_of_week][province]['num_uci'] += int(row['num_uci'])

    # Guardar los resultados en un archivo JSON
    with open(json_file_path, 'w') as json_file:
        json.dump(results, json_file, indent=4)

    print(f"\nDatos almacenados exitosamente en {json_file_path}")
