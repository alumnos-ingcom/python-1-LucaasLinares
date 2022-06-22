################
# Lucas Linares - @LucaasLinares Comision 2
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
5. Divisiones
Escribir una función que mediante restas sucesivas, obtenga el valor del cociente y resto de dos números enteros.

"""
#Precondicion : el divisor y dividendo deben ser enteros positivos y el divisor distinto de 0. 

def division_lenta(dividendo, divisor):
    resultado = 0
    div = dividendo
    while divisor <= dividendo  :
        resultado = resultado + 1
        dividendo = dividendo - divisor
    resto = div - (resultado * divisor)
    return (resultado,resto)    
        
dividendo = int(input("Ingrese dividendo: "))        
divisor = int(input("Ingrese divisor: "))

resultado , resto = division_lenta(dividendo, divisor)
print("EL RESULTADO DE LA DIVISION ES: ",resultado,"y su resto es",resto)
