# hacer un menu y cada menu debe tener una categoria por ejemplo si hago una categoria de postres debe salir postre de limon, roscones,pastel de 3 leches despues de seleccionar los productos
# uno debe seleccionar la cantidad de producto que quiera y al final que compruebe precios ventas y todo lo del anteior ejemplo
# 3 Categorias 10 productos por categorias y 2 promiciones po categoria

# 3 Categorias panaderia basica,postres,bebidas
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
    ],
    "Bebidas":[
        {"nombre":"Agua", "Precio": 500},
        {"nombre": "Café", "Precio": 1200},
        {"nombre": "Té", "Precio": 800},
        {"nombre": "Jarra de Jugo de naranja", "Precio": 6000},
        {"nombre": "Refresco", "Precio": 1700},
        {"nombre": "Limonada", "Precio": 1800},
        {"nombre": "Smoothie", "Precio": 2000},
        {"nombre": "Milkshake", "Precio": 2200},
        {"nombre": "Cerveza", "Precio": 2500},
        {"nombre": "Vino", "Precio": 3000}
    ],
     "Superpromos":[
        {"nombre":"Lleve 5 Tamales Tolimnenses por SOLO 22000","Precio": 20000},
        {"nombre":"Lleve un Tamal Tolimnense mas limonada por SOLO 6000","Precio": 6000},
        {"nombre":"lleve 5 empanadas de Pollo + Jarra de jugo de naranja SOLO por 22000","Precio": 13990},
        {"nombre":"Lleve 10 Panuchas por SOLO 9599","Precio": 9599},
        {"nombre":"Lleve Gelatina de frutas + tarta de fresa + Pastel de chocolate por SOLO 5999","Precio": 5999},
        {"nombre":"Lleve 2 embueltos mas cafe por SOLO 4999","Precio": 4999},
    ]    
}

print 
("                                        Menu        Panaderia 1995                                ")

for categoria in Menu.keys(): 
        print(" - ",categoria)

categoria_selec=input("Seleccione una categoria : ").capitalize()
if categoria_selec in Menu:
    productos_categoria=Menu[categoria_selec]
    print(f"\nProductos disponibles en la categoría {categoria_selec}:")

    for indice,producto in enumerate(productos_categoria,start=1):
         print(f"{indice}. {producto['nombre']} : ${producto['Precio']}")
    
    opcion=int(input("Seleccione el producto que desea comprar : "))
  

        
    if 1<=opcion<=len(productos_categoria):
        producto_seleccionado=productos_categoria[opcion-1]
        cantidad=int(input("Que cantidad desea comprar : "))
        cantidad_comprada=cantidad*producto_seleccionado['Precio']
        print(f"El producto que usted escogio es {cantidad} {producto_seleccionado['nombre']} con un valor de  $ {cantidad_comprada}")
        dinero=int(input("ingrese el valor del dinero disponible $ : "))
        vueltos=dinero-producto_seleccionado["Precio"]
        if vueltos>=0:
            print(f"Gracias por su compra, su regreso es de $  {vueltos}")    
        else:
            print(f"El dinero depositado no es suficiente le falta un total de $ {-vueltos}")
    else:
        print("La opcion seleccionada no es validad")
else:    
    print("La categoria ingresada es invalida")