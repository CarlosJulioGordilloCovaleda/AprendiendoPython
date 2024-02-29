# Primero intento para hacer una plataforma que tome pedidos de una empresa de alimentos, esta plataforma es para un vendedor
# Cuando realiza ventas la plataforma le da el valor del pedido puede seleccionar cliente y los productos que este solicita
# Da un % de descuento si cliente sobrepasa un monto y tambien voy a tratar de dar un porcentaje al vendedor sobre la venta que lo calcule
# Productos : Platanitos Salados,Maiz Molido,Frijo lima,Mantequilla de Mani,Mani salado

clientes=("Mas o menos","HipermercadosExito","Supermercados Metro","Agromercados de la montaña")
Productos=[
            {"nombre":"Platanitos verdes","precio":1200},
            {"nombre":"Platanitos verdes","precio":1200},
            {"nombre":"Platanitos verdes","precio":1200},
            {"nombre":"Platanitos verdes","precio":1200},
            {"nombre":"Platanitos verdes","precio":1200},
            {"nombre":"Platanitos verdes","precio":1200}
]
print("----- Clientes -----")

for i,val in enumerate(clientes,start=1):
    print(i,val)
Clienteelegido=int(input("Ingrese el codigo del cliente"))


print(Productos)
print(clientes)

