#Algortimo para generar  la serie de finobacci

serie=int(input("Ingrese la cantidad de terminos que requiere de ls serie de Finobacci: "))

a, b=0, 1 # Declaro las variables a y b que son fijas al inicio
contador =0

if serie<=0:
    print("Ingrese un numero entero positvo ")
elif serie==1:
    print("Serie de Finobacci hasta el termino ", serie, ":", a)
else:
    while contador < serie:
        print(a, end=' ')
    s=a+b
    a=b
    b=s
    contador+=1

