### Problema 1: Análisis de Temperaturas Mensuales

Este proyecto implementa un programa en Python que analiza las temperaturas promedio mensuales de varias ciudades. El objetivo es calcular promedios anuales, identificar meses extremos (más frío y más caluroso) y determinar la ciudad con mayor variación de temperatura durante el año.

---

## Estructura de Datos

Para almacenar las temperaturas se utiliza un **arreglo bidimensional (matriz)** mediante `numpy.ndarray`, donde:

- **Filas:** Representan cada ciudad (5 ciudades por defecto).
- **Columnas:** Representan cada mes del año (12 meses).

Ejemplo de matriz:

| Ciudad/Mes | Ene | Feb | Mar | ... | Dic |
|------------|-----|-----|-----|-----|-----|
| Ciudad 1   | 23  | 25  | 22  | ... | 20  |
| Ciudad 2   | 18  | 19  | 21  | ... | 17  |
| ...        | ... | ... | ... | ... | ... |
| Ciudad 5   | 24  | 23  | 25  | ... | 22  |

El uso de `numpy` permite operaciones **vectorizadas**, evitando bucles explícitos para cálculos de promedio y variación, lo que mejora la eficiencia.

---

## Funciones Implementadas

### 1. `ingresar_temperaturas(n_ciudades=5, n_meses=12)`

- **Descripción:** Solicita al usuario ingresar las temperaturas mensuales de cada ciudad.
- **Entrada:** 
  - `n_ciudades` (int): Número de ciudades.
  - `n_meses` (int): Número de meses.
- **Salida:** `numpy.ndarray` con dimensiones `(n_ciudades x n_meses)`.
- **Ventaja:** Centraliza la captura de datos y devuelve un arreglo listo para cálculos posteriores.

---

### 2. `promedio_anual(temperaturas)`

- **Descripción:** Calcula el promedio anual de temperatura de cada ciudad.
- **Entrada:** Matriz de temperaturas `(ciudades x meses)`.
- **Salida:** Vector con promedios anuales por ciudad.
- **Implementación eficiente:** Se utiliza `np.mean(temperaturas, axis=1)` para calcular todos los promedios de manera vectorizada.

---

### 3. `extremos_por_ciudad(temperaturas)`

- **Descripción:** Determina el mes más frío y más caluroso por ciudad.
- **Entrada:** Matriz de temperaturas.
- **Salida:** Lista de tuplas `(mes_frio, mes_caluroso)` para cada ciudad.
- **Ventaja:** `np.argmin` y `np.argmax` permiten identificar los extremos sin recorrer manualmente cada elemento.

---

### 4. `ciudad_mayor_variacion(temperaturas)`

- **Descripción:** Encuentra la ciudad con mayor diferencia entre la temperatura máxima y mínima.
- **Entrada:** Matriz de temperaturas.
- **Salida:** Índice de la ciudad y valor de la variación.
- **Implementación eficiente:** `np.ptp(temperaturas, axis=1)` calcula directamente la diferencia máxima-mínima por ciudad.

---

### 5. `ejecutar_problema1()`

- **Descripción:** Función principal que coordina la ejecución del análisis.
- **Funciones llamadas:**
  - `ingresar_temperaturas`
  - `promedio_anual`
  - `extremos_por_ciudad`
  - `ciudad_mayor_variacion`
- **Salida:** Muestra por consola:
  - Promedio anual por ciudad.
  - Mes más frío y más caluroso por ciudad.
  - Ciudad con mayor variación de temperatura.

---

## Ventajas y Eficiencia de la Solución

1. **Modularidad:** Cada tarea tiene su función, siguiendo el **principio de responsabilidad única**, lo que facilita mantenimiento y pruebas unitarias.
2. **Uso de NumPy:** Permite operaciones vectorizadas sobre matrices, evitando bucles anidados y reduciendo el tiempo de ejecución.
3. **Escalabilidad:** Se puede ampliar fácilmente a más ciudades o meses sin cambiar la lógica.
4. **Legibilidad y mantenibilidad:** Nombres descriptivos y docstrings claros mejoran la comprensión del código.
5. **Rendimiento:** Las funciones vectorizadas (`np.mean`, `np.argmax`, `np.ptp`) optimizan cálculos de promedio y variación, comparado con iteraciones manuales en Python puro.

---




----------------------------------------------------------------------
### Problema 2: Sistema de Gestión de Inventario

###Objetivo

Simular un sistema de inventario para una tienda con:

Almacenamiento de hasta 50 productos (código, nombre, precio, stock).

Búsqueda por código o nombre.

Actualización de stock tras una venta.

Reporte de productos con bajo stock (<5 unidades).

Cálculo del valor total del inventario.

### Estructura de Datos

Se utiliza una lista de diccionarios:

producto = {
    "codigo": "P001",
    "nombre": "Lápiz",
    "precio": 0.5,
    "stock": 20
}

### Funciones Implementadas

buscar_producto(productos, clave)

vender_producto(productos, codigo, cantidad)

productos_bajo_stock(productos)

valor_inventario(productos)

Cada función se encarga de una operación del sistema, permitiendo una implementación limpia y eficiente.

### Ventajas

Estructura flexible y adaptable.

Módulos reutilizables.

Fácil de integrar con interfaces gráficas o bases de datos.

### Rendimiento

Tiempo: O(n), donde n = número de productos.

Escalable y fácil de optimizar con estructuras como diccionarios hash.
--------------------------------------------------------------------
### Problema 3: Analisis de ventas
Este proyecto implementa un programa en Python que permite registrar y analizar las **ventas de varias sucursales** durante un número determinado de días.  

El programa está diseñado para ejecutarse desde la consola y solicitar al usuario los datos de ventas, mostrando luego un informe con estadísticas, patrones y un pronóstico para el mes siguiente.

---

 Funcionalidades

El sistema realiza los siguientes cálculos:

1. Ingreso de ventas
   - Permite capturar las ventas diarias de cada sucursal.  
   - Valida que los valores ingresados sean numéricos.  

2. Totales por sucursal  
   - Suma las ventas de cada sucursal en todo el período registrado.  

3. Totales por día  
   - Calcula el total de ventas sumando todas las sucursales por día.  

4. Mejor sucursal  
   - Identifica qué sucursal tuvo el mayor volumen de ventas acumulado.  

5. Patrones de ventas por día de la semana  
   - Analiza los datos agrupados por día de la semana.  
   - Determina el **mejor día** (mayores ventas promedio) y el **peor día**.  

6. Pronóstico de ventas  
   - Calcula un promedio diario por sucursal.  
   - Estima las ventas para un mes de **30 días**.  

## Requisitos

- Python 3.x
- Biblioteca NumPy (`pip install numpy`)

---

## Ejecución

```bash
python problema1.py.py
