################
# Lucas Linares - @LucaasLinares Comision 2
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
3. Comparación de números
Escribir una función que utilizando sumas y restas, reciba dos valores y retorne:

Retornar -1 si el primero es menor que el segundo
Retornar 0 si son iguales
Retornar 1 si el primero es mayor que el segundo

"""

def compara(numero, otro_numero):
    if numero == otro_numero :
        retorno = 0
        return (retorno)
    elif numero > otro_numero :
        retorno = 1
        return (retorno)
    else :
        retorno = -1
        return (retorno)
    
## Programa Principal

numero = int(input("Ingrese primer numero: "))
otro_numero = int(input("Ingrese segundo numero: "))

resultado = compara(numero, otro_numero)

if resultado == 0 :
    print("Los numeros ingresados son iguales")
elif resultado == -1 :
    print("El primer numero es menor que el segundo")
else :
    print("El primer numero es mayor al segundo")
