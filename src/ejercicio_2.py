import matplotlib.pyplot as plt
import json

# Función para cargar datos desde JSON


def cargar_datos():
    with open('resultados.json', 'r') as file:
        return json.load(file)

# Funciones para graficar


def graficar_defunciones(datos):
    for day, provinces in datos.items():
        defunciones = [prov['num_def'] for prov in provinces.values()]
        plt.bar(provinces.keys(), defunciones)
        plt.title(f"Defunciones por provincia el {day}")
        plt.show()


def graficar_casos(datos):
    for day, provinces in datos.items():
        casos = [prov['new_cases'] for prov in provinces.values()]
        plt.bar(provinces.keys(), casos)
        plt.title(f"Nuevos casos por provincia el {day}")
        plt.show()


def graficar_hospitalizados(datos):
    for day, provinces in datos.items():
        hospitalizados = [prov['num_hosp'] for prov in provinces.values()]
        plt.bar(provinces.keys(), hospitalizados)
        plt.title(f"Hospitalizados por provincia el {day}")
        plt.show()


def graficar_uci(datos):
    for day, provinces in datos.items():
        uci = [prov['num_uci'] for prov in provinces.values()]
        plt.bar(provinces.keys(), uci)
        plt.title(f"Pacientes en UCI por provincia el {day}")
        plt.show()


# Menú interactivo
datos = cargar_datos()

while True:
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
