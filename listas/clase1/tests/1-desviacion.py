def desviacion_estandar(datos):
    suma = 0.0
    i=0
    while i < len(datos):
        suma = suma + datos[i]
        i=i+1
    promedio = suma / len(datos)

    suma_dif_cuad = 0.0
    i=0
    while i < len(datos):
        suma_dif_cuad = suma_dif_cuad + (datos[i] - promedio) ** 2
        i=i+1
    desviacion = (suma_dif_cuad / (len(datos) - 1)) ** 0.5
    return desviacion