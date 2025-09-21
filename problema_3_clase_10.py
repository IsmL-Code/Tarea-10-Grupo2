# =============================
# Análisis de Datos de Ventas
# =============================

# 1. Ingresar datos de ventas
def ingresar_ventas(num_sucursales=2, dias=2):
    ventas = []
    for i in range(num_sucursales):
        print(f"\n--- Sucursal {i+1} ---")
        sucursal_ventas = []
        for j in range(dias):
            while True:
                try:
                    valor = float(input(f"Ventas del día {j+1}: "))
                    break
                except ValueError:
                    print("❌ Entrada inválida, ingresa un número.")
            sucursal_ventas.append(valor)
        ventas.append(sucursal_ventas)
    return ventas

# 2. Calcular totales por sucursal
def total_por_sucursal(ventas):
    return [sum(sucursal) for sucursal in ventas]

# 3. Calcular totales por día
def total_por_dia(ventas):
    if not ventas:
        return []
    dias = max(len(s) for s in ventas)
    return [sum(s[d] if d < len(s) else 0 for s in ventas) for d in range(dias)]

# 4. Mejor sucursal
def mejor_sucursal(ventas):
    if not ventas:
        return None, 0.0
    totales = total_por_sucursal(ventas)
    mejor = max(totales)
    indice = totales.index(mejor) + 1
    return indice, mejor

# 5. Detectar patrones
def patrones_ventas(ventas):
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    totales_dia = total_por_dia(ventas)
    if not totales_dia:
        return None, None, [0.0]*7

    promedios_semana = [0.0] * 7
    cuentas = [0] * 7

    # Agrupamos ventas por día de la semana y contamos cuántas veces aparece cada día
    for d, venta in enumerate(totales_dia):
        idx = d % 7
        promedios_semana[idx] += venta
        cuentas[idx] += 1

    # Evitar división por cero
    for i in range(7):
        if cuentas[i] > 0:
            promedios_semana[i] /= cuentas[i]

    mejor_dia = dias_semana[promedios_semana.index(max(promedios_semana))]
    peor_dia = dias_semana[promedios_semana.index(min(promedios_semana))]

    return mejor_dia, peor_dia, promedios_semana

# 6. Pronóstico para el siguiente mes
def pronostico(ventas):
    return [sum(suc) / len(suc) if len(suc) > 0 else 0.0 for suc in ventas]

# =============================
# Programa principal
# =============================
def main():
    print("=== Análisis de Datos de Ventas ===")
    ventas = ingresar_ventas()

    # Totales por sucursal
    tot_suc = total_por_sucursal(ventas)
    print("\nTotal de ventas por sucursal:")
    for i, total in enumerate(tot_suc, 1):
        print(f"Sucursal {i}: {total:.2f}")

    # Totales por día
    tot_dia = total_por_dia(ventas)
    print("\nTotal de ventas por día:")
    for d, total in enumerate(tot_dia, 1):
        print(f"Día {d}: {total:.2f}")

    # Mejor sucursal
    mejor_idx, mejor_val = mejor_sucursal(ventas)
    if mejor_idx:
        print(f"\nLa mejor sucursal fue la {mejor_idx} con ventas de {mejor_val:.2f}")
    else:
        print("\n⚠️ No hay datos de sucursales.")

    # Patrones
    mejor_dia, peor_dia, promedios = patrones_ventas(ventas)
    if mejor_dia:
        print("\nPatrones detectados:")
        print(f"📈 Mejor día de la semana: {mejor_dia}")
        print(f"📉 Peor día de la semana: {peor_dia}")
        print("Promedios por día de la semana:")
        for i, p in enumerate(promedios):
            print(f"{['Lunes','Martes','Miércoles','Jueves','Viernes','Sábado','Domingo'][i]}: {p:.2f}")
    else:
        print("\n⚠️ No hay datos suficientes para detectar patrones.")

    # Pronóstico
    pron = pronostico(ventas)
    print("\nPronóstico de ventas para el próximo mes (estimado en 30 días):")
    for i, p in enumerate(pron, 1):
        print(f"Sucursal {i}: {p * 30:.2f}")

# Ejecutar
if __name__ == "__main__":
    main()
