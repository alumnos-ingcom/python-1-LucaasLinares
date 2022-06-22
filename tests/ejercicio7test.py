################
# Lucas Linares - @LucaasLinares Comision 2
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
7. Transformación de un número
Escribir un programa que permita transformar un número solicitado expresado en grados, minutos y segundos a segundos a segundos. Y otra que haga el cambio en el sentido contrario, devolviendo una tuple.

Recuerden que un grado son 60 minutos y un minuto son 60 segundos.

"""
def sexadecimal_a_decimal(grados, minutos, segundos):
    decimal = (grados * 3600) + (minutos * 60) + segundos
    return (decimal)

def decimal_a_sexadecimal(numero):
    decimal = numero
    grados = decimal // 3600
    minutos = (numero - (grados * 3600)) // 60
    segundo = numero - (grados * 3600) - (minutos * 60)
    return (grados,minutos,segundo)


numero = int(input("Ingrese numero decimal para pasarlo a grados, minutos y segundos: "))
grados,minutos,segundos = decimal_a_sexadecimal (numero)
print("",grados,"grados",minutos,"minutos y",segundos,"segundos")

print("Ingrese los datos en grados, minutos y segundos:")
grados = int(input("grados: "))
minutos = int(input("minutos: "))
segundos = int(input("segundos: "))

decimal = sexadecimal_a_decimal(grados, minutos, segundos)
print("son ",decimal,"segundos")