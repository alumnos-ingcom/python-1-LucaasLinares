################
# Lucas Linares - @LucaasLinares Comision 2
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
6. Ordenar 3 valores
Escribir una función que a partir de tres variables de tipo entero retorne una tupla con dichos valores ordenados de menor a mayor. Y Viceversa

"""

def ordenar_mayor_a_menor(uno, dos, tres):
    if uno > dos :
        if uno > tres :
            if dos > tres :
                return (uno,dos,tres)
        else :
            return (dos,uno,tres)   
    elif uno < tres :
        if dos >= tres :
            return (dos,tres,uno)
        else :
            return (tres,dos,uno)

def ordenar_menor_a_mayor(uno, dos, tres):
    if uno > dos :
        if uno > tres :
            if dos > tres :
                return (tres,dos,uno)
        else :
            return (tres,uno,dos)   
    elif uno < tres :
        if dos >= tres :
            return (uno,tres,dos)
        else :
            return (uno,dos,tres)


##def ordenar_menor_a_mayor(uno, dos, tres):

uno = int(input("ingrese primer numero: "))
dos = int(input("ingrese segundo numero: "))
tres = int(input("ingrese tercer numero: "))

a,b,c = ordenar_mayor_a_menor(uno,dos,tres)
print("Numero ordenados de mayor a menor : ",a,b,c)

a,b,c = ordenar_menor_a_mayor(uno,dos,tres)
print("Numero ordenados de menor a mayor : ",a,b,c)

