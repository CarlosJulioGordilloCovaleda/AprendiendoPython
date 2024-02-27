# Algortimo para calcular el area de un triangulo
import math
print("Tenga en cuenta que todas las unidades ingresadas deben ser en la misma unidad de medida ( cm,m,ft,in)")

opcion=input("Si desea realizar el calulo con el radio digite(r) y si lo desea con el diametro digite (d) : ")

if opcion.lower()=='r':
    radio =float(input("Ingrese el radio del circulo : "))
    Area=math.pi * radio**2
    print("El area del cirulo es : ", Area)
elif opcion.lower()=='d':
    diametro=float(input("Ingrese el diametro del circulo : "))
    Area=( math.pi * diametro**2 ) / 4
    print("El area del circulo es : ", Area)
else:
    print("Opcion no valida por favor ingrese  (r)para radio o (d)diametro")