import matplotlib.pyplot as plt
import json
import os

# Función para cargar datos desde JSON


def cargar_datos():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(base_dir, '../outputs/resultados.json')
    with open(json_file_path, 'r') as file:
        return json.load(file)

# Funciones para graficar


def graficar_defunciones(datos):
    for day, provinces in datos.items():
        defunciones = [prov['num_def'] for prov in provinces.values()]
        plt.bar(provinces.keys(), defunciones)
        plt.title(f"Defunciones por provincia el {day}")
        plt.xlabel('Provincia')
        plt.ylabel('Defunciones')
        plt.show()
        plt.close()  # Cerrar gráfico automáticamente


def graficar_casos(datos):
    for day, provinces in datos.items():
        casos = [prov['new_cases'] for prov in provinces.values()]
        plt.bar(provinces.keys(), casos)
        plt.title(f"Casos por provincia el {day}")
        plt.xlabel('Provincia')
        plt.ylabel('Casos')
        plt.show()
        plt.close()  # Cerrar gráfico automáticamente


def graficar_hospitalizados(datos):
    for day, provinces in datos.items():
        hospitalizados = [prov['num_hosp'] for prov in provinces.values()]
        plt.bar(provinces.keys(), hospitalizados)
        plt.title(f"Hospitalizados por provincia el {day}")
        plt.xlabel('Provincia')
        plt.ylabel('Hospitalizados')
        plt.show()
        plt.close()  # Cerrar gráfico automáticamente


def graficar_uci(datos):
    for day, provinces in datos.items():
        uci = [prov['num_uci'] for prov in provinces.values()]
        plt.bar(provinces.keys(), uci)
        plt.title(f"Pacientes en UCI por provincia el {day}")
        plt.xlabel('Provincia')
        plt.ylabel('Pacientes en UCI')
        plt.show()
        plt.close()  # Cerrar gráfico automáticamente


# Menú interactivo
datos = cargar_datos()

while True:
    try:
        opcion = int(input("""¿Qué gráfica quieres visualizar?
        1. Defunciones
        2. Casos
        3. Hospitalizados
        4. UCI
        5. Salir
        """))

        if opcion == 1:
            graficar_defunciones(datos)
        elif opcion == 2:
            graficar_casos(datos)
        elif opcion == 3:
            graficar_hospitalizados(datos)
        elif opcion == 4:
            graficar_uci(datos)
        elif opcion == 5:
            break
        else:
            print("Opción no válida, por favor selecciona un número del 1 al 5.")

    except ValueError:
        print("Error: Por favor, ingresa un número válido.")
