    # Nombre: Zuleidy Ochoa Toscano
    # Grupo: 886
    # Programa: Fundamentos de programación
    # Codigo Fuente: Autoría propia

menu = [
    ["Hamburguesa", "Comida rápida", 20000],
    ["Pizza", "Comida rápida", 12000],
    ["Ensalada", "Saludable", 10000],
    ["Jugo Natural", "Bebida", 8000],
    ["Mazorcada", "Comida rápida", 25000],
    ["Gaseosa", "Bebida", 5000]
]

# FUNCIÓN
def calcular_precio_final(producto, categoria_objetivo, umbral):
    nombre, categoria, precio = producto

    # Validación paso a paso
    cumple_categoria = categoria == categoria_objetivo
    cumple_precio = precio > umbral

    # Aplicar lógica
    if cumple_categoria and cumple_precio:
        descuento = precio * 0.15
        precio_final = precio - descuento
    else:
        precio_final = precio

    return precio_final


# PARÁMETROS
categoria_objetivo = "Comida rápida"
umbral = 15000

# SALIDA
print("MENÚ CON PROMOCIÓN\n")

for producto in menu:
    precio_base = producto[2]
    precio_final = calcular_precio_final(producto, categoria_objetivo, umbral)

    print("Producto:", producto[0])
    print("Categoría:", producto[1])
    print("Precio base:", precio_base)
    print("Precio final:", precio_final)
    print("-" * 30)
 