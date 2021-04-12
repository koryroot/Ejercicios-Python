#Problema 01: Dado dos números diferentes, devolver el número mayor

""" Análisis: Para la solución de este problema, se requiere que
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

