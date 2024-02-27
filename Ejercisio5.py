# Algortimo para verficiar si un numero es par o impar

num=int(input("Ingrese un numero : "))

if num % 2 ==0: # Utilizo el % significa si la division del num / 2 el residuo es igual a  0 entonces sera par
    print("El numero es Par")

else:
    print("El numero no es par")