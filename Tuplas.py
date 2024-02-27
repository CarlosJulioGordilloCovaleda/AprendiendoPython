productos = tuple((
    "Coca-Cola", 
    "Pepsi", 
    "Sprite", 
    "Fanta", 
    "7UP", 
    "Mountain Dew", 
    "Dr Pepper", 
    "Schweppes", 
    "Miranda", 
    "Lift"))
precios = tuple((
    4500, 
    3750, 
    3000, 
    3600, 
    5250, 
    6000, 
    5400, 
    3900, 
    4200, 
    4800))


for i,val in enumerate(productos): #Recorre la tupla y saca su valor y su indice
    print(f"""{i}, {val}, ${precios[i]} """)
   
opcion=int(input())
print(f"Usuario usted selecciono el proucto {productos[opcion]} con un valor de ${precios[opcion]}" )
dinero=int(input(" Ingrese la cantidad de dinero disponible : "))
vueltos=dinero-precios[opcion]
if dinero >= precios[opcion]:
    print(f"Usuario si usted compro el producto {productos[opcion]} con un valor de ${precios[opcion]}, sus vueltos son ${vueltos}")
else:
    print(f"Usuario el producto que desea comprar {productos[opcion]} con un valor de ${precios[opcion]}, le falta un total de $ {-vueltos}")

