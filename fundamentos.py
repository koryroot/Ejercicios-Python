#Problema 01: Dado dos números diferentes, devolver el número mayor
"""
""Análisis: Para la solución de este problema, se requiere que
ingrese dos números por teclado y el sistema realice el proceso
de devolver el número mayor."""

print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
print("Este programa es para determinar el mayor de dos numeros")  
n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))

if n1 > n2:
    print(f"El numero mayor es: {n1}")
else:
    print(f"El numero mayor es: {n2}")

print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

print("Determinar si un número es positivo, negativo o neutro.")
"""Para la solución de este problema, se requiere que
ingrese un número entero por teclado y el sistema verifique si
es positivo, neutro o negativo."""

n1 = int(input("Introduce un numero: "))
if n1 < 0:
    print("El numero es negativo")
elif n1 > 0:
    print("El numero es positivo")
else:
    print("El numero es neutro")
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

#programa para determinar si se ha igresado un numero

cosa = input("Digita un numero: ")
if cosa.isdigit():
    print("El valor ingresado es un numero" )
else:
    print("Eso no es un numero e.e")

#3. Problema 03: Dado un carácter determine si es una Vocal o no.
"""Análisis: Para la solución de este problema, se requiere que
usuario ingrese un carácter y el sistema verifique si es un
vocal o no."""
