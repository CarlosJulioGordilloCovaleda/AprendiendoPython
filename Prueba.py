# Menú de la panadería
menu = {
    "Pan": {
        "Pan de trigo": 0.5,
        "Pan de centeno": 0.6,
        "Pan integral": 0.7,
        "Bollos de pan": 0.4,
        "Panecillos de leche": 0.8,
        "Pan de avena": 0.7,
        "Panecillos de queso": 0.9,
        "Pan de nueces": 1.0,
        "Rosquillas": 0.6,
        "Panecillos de cebolla": 0.8
    },
    "Repostería": {
        "Croissant": 1.0,
        "Napolitana de chocolate": 1.2,
        "Tarta de manzana": 2.5,
        "Magdalenas": 0.8,
        "Donuts": 1.0,
        "Galletas de mantequilla": 0.6,
        "Palmeras de chocolate": 1.2,
        "Pastelitos de crema": 1.5,
        "Buñuelos de viento": 1.2,
        "Roscón de reyes": 3.0
    },
    "Bebidas": {
        "Café": 1.5,
        "Té": 1.2,
        "Jugo de naranja": 2.0,
        "Refresco de cola": 1.8,
        "Agua mineral": 1.0,
        "Cerveza de barril": 2.5,
        "Vino tinto": 3.0,
        "Batido de frutas": 2.2,
        "Café con leche": 1.8,
        "Limonada": 1.5
    }
}

# Promociones
promociones = {
    "Desayuno Especial": {
        "Café": 1.5,
        "Croissant": 1.0
    },
    "Merienda Feliz": {
        "Magdalenas": 0.8,
        "Jugo de naranja": 2.0
    }
}

# Mostrar menú de la panadería
print("---- Menú de la Panadería ----")
for categoria, productos in menu.items():
    print(categoria + ":")
    for producto, precio in productos.items():
        print("- {} (${:.2f})".format(producto, precio))
    print()

# Mostrar promociones
print("\nPromociones:")
for promocion, items in promociones.items():
    print("- {}:".format(promocion))
    for item, precio in items.items():
        print("  - {} (${:.2f})".format(item, precio))

# Proceso de compra
print("\n¡Bienvenido a la panadería!")
total_cost = 0
while True:
    producto = input("\nIngrese el producto que desea comprar (o escriba 'fin' para terminar la compra): ").capitalize()
    if producto == 'Fin':
        break
    if any(producto in productos for productos in menu.values()):
        cantidad = int(input("Ingrese la cantidad que desea: "))
        if producto in promociones:
            if producto in promociones[producto]:
                total_cost += promociones[producto][producto] * cantidad
            else:
                total_cost += menu[producto] * cantidad
        else:
            total_cost += menu[producto] * cantidad
    else:
        print("El producto ingresado no está en el menú. Por favor, elija otro.")

efectivo = float(input("\nIngrese la cantidad de dinero que posee: $"))
cambio = efectivo - total_cost

if cambio < 0:
    print("Lo siento, no tiene suficiente dinero para realizar la compra.")
else:
    print("\nGracias por su compra. Su cambio es: ${:.2f}".format(cambio))
