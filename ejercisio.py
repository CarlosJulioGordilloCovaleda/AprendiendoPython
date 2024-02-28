# hacer un menu y cada menu debe tener una categoria por ejemplo si hago una categoria de postres debe salir postre de limon, roscones,pastel de 3 leches despues de seleccionar los productos
# uno debe seleccionar la cantidad de producto que quiera y al final que compruebe precios ventas y todo lo del anteior ejemplo
# 3 Categorias 10 productos por categorias y 2 promiciones po categoria

# 3 Categorias panaderia basica,postres,gourmet 
Menu = {
    "Tradicionales":[
        {"nombre":"Pan de dulce", "Precio": 1000},
        {"nombre": "Pan de Sal", "Precio": 1000},
        {"nombre": "Croasan", "Precio": 1500},
        {"nombre": "Empanadas de pollo", "Precio": 1800},
        {"nombre": "Empanadas de queso", "Precio": 1300},
        {"nombre": "Tamales", "Precio": 1700},
        {"nombre": "Embuelto", "Precio": 1800},
        {"nombre": "Tamal Tolimense", "Precio": 5000},
        {"nombre": "Panuchas", "Precio": 2000},
        {"nombre": "Galletas", "Precio": 2300},
    ]        
}

print ("                                        Menu                                        ")
for i in Menu.keys(): 
    print(" - ",i)
for indice,producto in enumerate(Menu["Tradicionales"],start=1):
    print(" - {}. {} : $ {}".format(indice, producto["nombre"], producto["Precio"]))

opcion=int(input("Seleccione el producto que desea comprar : "))
producto_seleccionado = Menu["Tradicionales"][opcion - 1]
print(f"El producto que usted escogio es {producto_seleccionado['nombre']} con un valor de  $ {producto_seleccionado['Precio']}")
dinero=int(input("El valor del dinero disponible $ : "))
vueltos=dinero-producto_seleccionado["Precio"]
if dinero>=opcion:
    print(f"Gracias por su compra, su regreso es de $  {vueltos}")
else:
    print(f"El dinero depositado no es suficiente le falta un total de $ {-vueltos}")



