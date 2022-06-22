################
# Lucas Linares - @LucaasLinares Comision 2
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
1. Conversión de temperaturas
Se quiere transformar temperaturas en grados fahrenheit a grados centígrados y viceversa.

Escribir las funciones para convertir la temperatura en grados centigrados en fahrenheit como un número decimal, utilice esta formula para calcular los grados centígrados y retorne el resultado obtenido. Y viceversa.
"""

# Reemplazar por las funciones a implementar del ejercicio

def convertir_a_fahrenheit(centigrados):
    fahrenheit = (centigrados * 9/5) + 32
    return (fahrenheit)

def convertir_a_centigrados(fahrenheit):
    centigrados = (fahrenheit - 32) * 5/9
    return (centigrados)


#PROGRAMA PRINCIPAL

centigrados = float(input("Ingrese valor en grados centrigrados para realizar la transformacion: "))
fahrenheit = convertir_a_fahrenheit(centigrados)
print("son",fahrenheit," grados fahrenheit")

fahrenheit = float(input("Ingrese valor en grados fahrenheit para realizar la transformacion: "))
centigrados = convertir_a_centigrados(fahrenheit)
print("son",centigrados," grados centigrados")