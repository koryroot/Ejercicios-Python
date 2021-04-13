#Problema 01: Dado dos números diferentes, devolver el número mayor
"""
""Análisis: Para la solución de este problema, se requiere que
ingrese dos números por teclado y el sistema realice el proceso
de devolver el número mayor."""
def nMayor(num1,num2):
    print("Este programa es para determinar el mayor de dos numeros")  
    if n1 > n2:
        print(f"El numero mayor es: {n1}")
    else:
        print(f"El numero mayor es: {n2}")
    
n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
nMayor(n1,n2)
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

print("Determinar si un número es positivo, negativo o neutro.")
def Num(n):
    if n1 < 0:
        print("El numero es negativo")
    elif n1 > 0:
        print("El numero es positivo")
    else:
        print("El numero es neutro")

n1 = int(input("Introduce un numero: "))
Num(n1)
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

print("programa para determinar si se ha igresado un numero")
def Idnum(cosa):
    if cosa.isdigit():
        print("El valor ingresado es un numero" )
    else:
        print("Eso no es un numero e.e")

cosas = input("Digita un numero: ")
Idnum(cosas)
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
#3. Problema 03: Dado un carácter determine si es una Vocal o no.

print("Dado un carácter determine si es una Vocal o no.")
def vocal(vocal):
    if vocal in ['a','e','i','o','u','A','E','I','O','U']:
        return "El caracter es una vocal"
    elif vocal in ['y','Y']:
        return "vocal/consonante"
    elif vocal.isdigit():
        print("usted ha introducido un numero")
    elif vocal in ['!','@','#','$','%','^','&','*','(',')','{','}','[',']']:
        print("Usted ha introducciodo un caracter especial")
    else:
        print("Es una consonate")

v = input("Introduce un caracter: ")
vocal(v)
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

print("determina si un numero es par o impar")
def PoI(poi):
    if poi % 2 == 0:
        print("El numero es par") 
    else:
        print("el numero es impar")
iop = int(input("introduce un numero"))
PoI(iop