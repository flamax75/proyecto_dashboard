import matplotlib.pyplot as plt
import json
import os

# Función para cargar datos desde JSON


def cargar_datos():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(base_dir, '../outputs/resultados.json')
    with open(json_file_path, 'r') as file:
        return json.load(file)

# Función para encontrar la provincia con el máximo valor en cada categoría


def maximo_por_categoria(datos):
    maximos = {
        "num_def": {"provincia": None, "valor": 0},
        "new_cases": {"provincia": None, "valor": 0},
        "num_hosp": {"provincia": None, "valor": 0},
        "num_uci": {"provincia": None, "valor": 0},
    }

    for day, provinces in datos.items():
        for province, values in provinces.items():
            for key in maximos.keys():
                if values[key] > maximos[key]["valor"]:
                    maximos[key] = {
                        "provincia": province, "valor": values[key]}

    return maximos

# Función para graficar el máximo


def graficar_maximo(categoria, maximos):
    categoria_nombres = {
        "num_def": "Defunciones",
        "new_cases": "Casos",
        "num_hosp": "Hospitalizados",
        "num_uci": "UCI"
    }

    plt.pie([maximos[categoria]["valor"], 1], labels=[
            maximos[categoria]["provincia"], 'Otros'], autopct='%1.1f%%')
    plt.title(f'Máximo de {categoria_nombres[categoria]} en {
              maximos[categoria]["provincia"]}')
    plt.show()
    plt.close()


# Cargar los datos
datos = cargar_datos()
maximos = maximo_por_categoria(datos)

# Menú interactivo
while True:
    try:
        opcion = int(input("""¿Qué gráfica quieres visualizar?
        1. Provincia con más defunciones
        2. Provincia con más casos
        3. Provincia con más hospitalizados
        4. Provincia con más UCI
        5. Salir
        """))

        if opcion == 1:
            graficar_maximo("num_def", maximos)
        elif opcion == 2:
            graficar_maximo("new_cases", maximos)
        elif opcion == 3:
            graficar_maximo("num_hosp", maximos)
        elif opcion == 4:
            graficar_maximo("num_uci", maximos)
        elif opcion == 5:
            break
        else:
            print("Opción no válida, por favor selecciona un número del 1 al 5.")

    except ValueError:
        print("Error: Por favor, ingresa un número válido.")
