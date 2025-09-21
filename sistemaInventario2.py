
# Creamos cadda producto: diccionario con código, nombre, precio, cantidad
productos = [
    {"codigo": "P001", "nombre": "Lápiz", "precio": 0.5, "stock": 20},
    {"codigo": "P002", "nombre": "Cuaderno", "precio": 1.5, "stock": 3},
    {"codigo": "P003", "nombre": "Borrador", "precio": 0.75, "stock": 10},
]

# Buscamos producto por código o nombre
def buscar_producto(productos, clave):
    for producto in productos:
        if producto["codigo"] == clave or producto["nombre"].lower() == clave.lower():
            return producto
    return None

# Actualizamos inventario tras una venta
def vender_producto(productos, codigo, cantidad):
    producto = buscar_producto(productos, codigo)
    if producto and producto["stock"] >= cantidad:
        producto["stock"] -= cantidad
        return True
    return False

#  generamos el informe de productos con bajo stock (<5)
def productos_bajo_stock(productos):
    return [p for p in productos if p["stock"] < 5]

# Calculamos el valor total del inventario
def valor_inventario(productos):
    return sum(p["precio"] * p["stock"] for p in productos)



# Solicitamos el código o nombre del producto
codigo_input = input("Ingrese el código o nombre del producto que desea comprar: ").strip()

# Solicitamos la cantidad
try:
    cantidad_input = int(input("Ingrese la cantidad que desea comprar: "))
except ValueError:
    print(" Cantidad inválida. Debe ser un número entero.")
    exit()

# Intentar realizar la venta
print(f"\nVenta: {cantidad_input} unidades de '{codigo_input}'")
if vender_producto(productos, codigo_input, cantidad_input):
    print(" Venta exitosa")
else:
    print(" Stock insuficiente o producto no encontrado")

# Mostramps los productos con bajo stock
print("\n Productos con bajo stock :")
bajos = productos_bajo_stock(productos)
if bajos:
    for p in bajos:
        print(f" {p['nombre']} (Stock: {p['stock']})")
else:
    print("Todos los productos tienen suficiente stock.")

# Mostramos el  valor total del inventario
print(f"\n Valor total del inventario: ${valor_inventario(productos):.2f}")

