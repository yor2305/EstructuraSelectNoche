# Definir Constantes
PRECIO_SENCILLA = 20000
PRECIO_DOBLE = 25000
PRECIO_TRIPLE = 28000
IMPUESTO_TARJETA = 0.07

# Funcion para calcular el precio
def calcular_precio(tipo_hambuerguesa, medio_pago, cantidad):
    # definir el tipo de hambuerguesa
    if tipo_hambuerguesa == 1:
        precio = PRECIO_SENCILLA
        descripcion = "Sencilla"
    elif tipo_hambuerguesa == 2:
        precio = PRECIO_DOBLE
        descripcion = "Doble"
    elif tipo_hambuerguesa == 3:
        precio = PRECIO_TRIPLE
        descripcion = "Triple"
    else:
        return None  # Tipo de hambuerguesa
    # Calcular el total sin cargos
    total_sin_cargo = precio * cantidad

# Aplicar impuesto si el medio de pago es tarjeta
    if medio_pago == 1:
        impuesto = round(total_sin_cargo * IMPUESTO_TARJETA)
    else:
        impuesto = 0
    total = round(total_sin_cargo + impuesto)

    # Retoranar datos relevantes
    return descripcion, precio, cantidad, impuesto, total


# Funcion para generar mensaje
def generar_mensaje(descripcion, precio, cantidad, impuesto, total):
    return (f"Tipo de hambuerguesa: {descripcion}\n"
            f"Precio: ${precio}\n"
            f"Cantidad: {cantidad}\n"
            f"Impuesto: ${impuesto}\n"
            f"Total: ${total}")


# funcion para validar los datos
def validar_datos(tipo_hambuerguesa, medio_pago, cantidad):
    if 1 <= tipo_hambuerguesa <= 3 and 1 <= medio_pago <= 2 and cantidad > 0:
        resultado = calcular_precio(tipo_hambuerguesa, medio_pago, cantidad)
        # print("Resultado: ",resultado)
        descripcion, precio, cantidad, impuesto, total = resultado
        mensaje = generar_mensaje(descripcion, precio, cantidad, impuesto, total)
        print("------------------------\n" + mensaje)
    else:
        print("Verifique las opciones ingresadas")
# entradas
tipo_hambuerguesa = int(input("Ingres el tipo de hambuerguesa \n1. Sencilla \n2. Doble \n3. Triple \n"))
medio_pago = int(input("Ingrese el medio de pago \n1. Tarjeta \n2. Otro \n"))
cantidad = int(input("Ingrese la cantidad: "))

#saidas
validar_datos(tipo_hambuerguesa,medio_pago, cantidad)
