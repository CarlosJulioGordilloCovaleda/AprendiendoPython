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
        {"nombre": "Empanadas de queso", "Precio": 0.6},
        {"nombre": "Tamales", "Precio": 0.6},
        {"nombre": "Embuelto", "Precio": 0.6},
        {"nombre": "Tamal Tolimense", "Precio": 0.6},
        {"nombre": "Panuchas", "Precio": 0.6},
        {"nombre": "Galletas", "Precio": 0.6},
    ]        
}
for i,val in enumerate("nombre"): 
    print(f"""{i}, {val}, ${"precios"[i]} """)

print(Menu)