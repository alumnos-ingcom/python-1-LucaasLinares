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
        if  numero % 2 == 0 :
            c = c + 1
    if c == 2 :
        return (True)
    else :
        return (False)
