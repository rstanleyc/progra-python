# http://progra.usm.cl/apunte/ejercicios/2/desviacion-estandar.html

def desviacion_estandar(valores):
    suma = 0
    promedio = sum(valores) / len(valores)
    for v in valores:
        suma += (v - promedio) ** 2
    desviacion = (suma / (len(valores) - 1)) ** 0.5
    return desviacion