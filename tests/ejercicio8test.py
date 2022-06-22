################
# Lucas Linares - @LucaasLinares Comision 2
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
8. Números primos
Escribir una función que indique con True si un numero indicado es Primo.

"""


def es_primo(numero):
    x = 1 
    c = 0
    while x <= numero :
        if  numero % x == 0 :
            c = c + 1
        x = x + 1
    if c == 2 :
        return (True)
    else :
        return (False)

## Programa principal

numero = int(input("Ingrese numero para verificar si es primo: "))
esprimo = es_primo(numero)
if esprimo == True :
    print("es primo")
elif esprimo == False :
    print("no es primo")