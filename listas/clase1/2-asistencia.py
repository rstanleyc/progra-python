# http://progra.usm.cl/apunte/ejercicios/2/asistencia.html
alumnos = ['Pepito', 'Yayita', 'Fulanita', 'Panchito']
asistencia = [
    [True, True, True, False, False, False, False],
    [True, True, True, False, True, False, True],
    [True, True, True, True, True, True, True],
    [True, True, True, False, True, True, True]
]

def alumno_estrella(asistencia):
    lista = total_por_alumno2(asistencia)
    return alumnos[lista.index(max(lista))]

def total_por_clase(tabla):
    resultado = []
    for j in range(len(tabla[0])):
        suma = 0
        for i in range(len(tabla)):
            if tabla[i][j]:
                suma += 1
        resultado.append(suma)
    return resultado



def total_por_alumno2(tabla):
    resultado = []
    for elemento in tabla:
        resultado.append(elemento.count(True))
    return resultado

def total_por_alumno1(tabla):
    resultado = []
    for elemento in tabla:
        suma = 0
        for e in elemento:
            if e == True:
                suma += 1
        resultado.append(suma)
    return resultado