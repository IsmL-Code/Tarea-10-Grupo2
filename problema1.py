import numpy as np

# Función para ingresar las temperaturas de las ciudades


def ingresar_temperaturas(n_ciudades=5, n_meses=12):
    """
    Solicita al usuario ingresar las temperaturas mensuales de cada ciudad.

    Parámetros:
        n_ciudades (int): Número de ciudades.
        n_meses (int): Número de meses.

    Retorna:
        numpy.ndarray: Matriz de temperaturas (ciudades x meses)
    """
    temperaturas = []
    for i in range(n_ciudades):
        ciudad = []
        print(f"\nIngresando temperaturas para la ciudad {i+1}:")
        for j in range(n_meses):
            temp = float(input(f"Mes {j+1}: "))
            ciudad.append(temp)
        temperaturas.append(ciudad)
    return np.array(temperaturas)


# Función para calcular el promedio anual por ciudad
def promedio_anual(temperaturas):
    """
    Calcula el promedio anual de temperatura de cada ciudad.

    Parámetros:
        temperaturas (numpy.ndarray): Matriz de temperaturas (ciudades x meses)

    Retorna:
        numpy.ndarray: Vector con promedios anuales por ciudad
    """
    return np.mean(temperaturas, axis=1)


# Función para identificar el mes más caluroso y más frío por ciudad
def extremos_por_ciudad(temperaturas):
    """
    Encuentra el mes más caluroso y más frío para cada ciudad.

    Parámetros:
        temperaturas (numpy.ndarray): Matriz de temperaturas (ciudades x meses)

    Retorna:
        list: Lista de tuplas (mes_frio, mes_caluroso) para cada ciudad
    """
    extremos = []
    for ciudad in temperaturas:
        mes_frio = np.argmin(ciudad) + 1
        mes_caluroso = np.argmax(ciudad) + 1
        extremos.append((mes_frio, mes_caluroso))
    return extremos


# Función para determinar la ciudad con mayor variación de temperatura
def ciudad_mayor_variacion(temperaturas):
    """
    Determina qué ciudad tuvo la mayor diferencia entre la temperatura más alta y más baja.

    Parámetros:
        temperaturas (numpy.ndarray): Matriz de temperaturas (ciudades x meses)

    Retorna:
        int: Índice de la ciudad con mayor variación
        float: Valor de la variación
    """
    variaciones = np.ptp(temperaturas, axis=1)  # ptp = peak-to-peak
    ciudad_max = np.argmax(variaciones)
    return ciudad_max, variaciones[ciudad_max]


# Función principal para ejecutar el análisis
def ejecutar_problema1():
    print("=== Problema 1: Análisis de Temperaturas Mensuales ===")

    # Ingreso de datos
    temperaturas = ingresar_temperaturas()

    # Promedio anual
    promedios = promedio_anual(temperaturas)
    print("\nPromedio anual por ciudad:")
    for i, prom in enumerate(promedios, start=1):
        print(f"Ciudad {i}: {prom:.2f}°C")

    # Meses extremos
    extremos = extremos_por_ciudad(temperaturas)
    print("\nMes más frío y más caluroso por ciudad:")
    for i, (frio, caluroso) in enumerate(extremos, start=1):
        print(
            f"Ciudad {i}: Mes más frío = {frio}, Mes más caluroso = {caluroso}")

    # Ciudad con mayor variación
    ciudad_var, variacion = ciudad_mayor_variacion(temperaturas)
    print(
        f"\nCiudad con mayor variación de temperatura: Ciudad {ciudad_var+1} ({variacion:.2f}°C)")


# Ejecutar el programa
if __name__ == "__main__":
    ejecutar_problema1()
