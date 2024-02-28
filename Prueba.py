# Menú de la panadería
Menu = {
    "Tradicionales":[
        {"nombre":"Pan de dulce", "Precio": 1000},
        {"nombre": "Pan de Sal", "Precio": 1000},
        {"nombre": "Croasan", "Precio": 1500},
        {"nombre": "Empanadas de pollo", "Precio": 1800},
        {"nombre": "Empanadas de queso", "Precio": 1300},
        {"nombre": "Tamales", "Precio": 1700},
        {"nombre": "Envuelto", "Precio": 1800},
        {"nombre": "Tamal Tolimense", "Precio": 5000},
        {"nombre": "Panuchas", "Precio": 2000},
        {"nombre": "Galletas", "Precio": 2300},
    ],
    "Postres":[
        {"nombre":"Pastel de chocolate", "Precio": 2500},
        {"nombre": "Helado de vainilla", "Precio": 1800},
        {"nombre": "Tarta de fresa", "Precio": 2200},
        {"nombre": "Brownie", "Precio": 2000},
        {"nombre": "Gelatina de frutas", "Precio": 1500},
        {"nombre": "Flan casero", "Precio": 1900},
        {"nombre": "Fresas con Crema", "Precio": 2100},
        {"nombre": "Tiramisú", "Precio": 2600},
        {"nombre": "Mousse de limón", "Precio": 1700},
        {"nombre": "Cheesecake de frutos rojos", "Precio": 2800}
    ]    
}

print("Menú de la Panadería\n")

# Mostrar las categorías disponibles
for categoria in Menu.keys(): 
    print(categoria)

# Pedir al usuario la selección de categoría
categoria_seleccionada = input("Seleccione una categoría: ").capitalize()

# Verificar si la categoría seleccionada existe en el menú
if categoria_seleccionada in Menu:
    productos_categoria = Menu[categoria_seleccionada]

    # Mostrar los productos de la categoría seleccionada
    print(f"\nProductos disponibles en la categoría {categoria_seleccionada}:")
    for indice, producto in enumerate(productos_categoria, start=1):
        print(f"{indice}. {producto['nombre']} : ${producto['Precio']}")

    # Pedir al usuario la selección del producto
    opcion = int(input("Seleccione el producto que desea comprar: "))

    # Verificar si la opción seleccionada es válida
    if 1 <= opcion <= len(productos_categoria):
        producto_seleccionado = productos_categoria[opcion - 1]
        print(f"\nHa seleccionado {producto_seleccionado['nombre']} con un precio de ${producto_seleccionado['Precio']}")

        # Pedir al usuario que ingrese el dinero disponible
        dinero = int(input("Ingrese el valor del dinero disponible: $ "))

        # Calcular el cambio
        cambio = dinero - producto_seleccionado['Precio']

        # Verificar si el dinero es suficiente
        if cambio >= 0:
            print(f"Gracias por su compra. Su cambio es de ${cambio}.")
        else:
            print(f"El dinero depositado no es suficiente. Le falta un total de ${abs(cambio)}.")

    else:
        print("La opción seleccionada no es válida.")
else:
    print("La categoría ingresada no está en el menú.")
