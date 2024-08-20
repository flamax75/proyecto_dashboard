import matplotlib.pyplot as plt

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


def graficar_maximos(maximos):
    categorias = ["Defunciones", "Casos", "Hospitalizados", "UCI"]
    valores = [maximos[key]["valor"] for key in maximos]
    provincias = [maximos[key]["provincia"] for key in maximos]

    for i in range(4):
        plt.pie([valores[i], sum(valores) - valores[i]],
                labels=[provincias[i], 'Otros'], autopct='%1.1f%%')
        plt.title(f'Máximo de {categorias[i]} en {provincias[i]}')
        plt.show()


# Menú interactivo para mostrar las gráficas de máximos
datos = cargar_datos()
maximos = maximo_por_categoria(datos)

while True:
    opcion = int(input("""¿Qué gráfica quieres visualizar?
    1. Provincia con más defunciones
    2. Provincia con más casos
    3. Provincia con más hospitalizados
    4. Provincia con más UCI
    5. Salir
    """))

    if opcion in range(1, 5):
        graficar_maximos(
            {list(maximos.keys())[opcion-1]: maximos[list(maximos.keys())[opcion-1]]})
    elif opcion == 5:
        break
    else:
        print("Opción no válida, por favor selecciona un número del 1 al 5.")
