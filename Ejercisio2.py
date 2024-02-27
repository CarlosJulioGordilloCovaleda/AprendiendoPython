#Algoritmo para verificar si un numero es primo
num=int(input("Ingrese un numero : "))

if num<=1:
    print("El numero es primo")
else:
    primo= True
    for i in range(2,num):
        if num %i ==0:
            primo= False
            break
    if primo:
        print(num, "Es primo ")
    else:
        print(num,"No es primo")
