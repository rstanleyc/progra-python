alumnos = ['Pepito', 'Yayita', 'Fulanita', 'Panchito']
asistencia = [
    [True, True, True, False, False, False, False],
    [True, True, True, False, True, False, True],
    [True, True, True, True, True, True, True],
    [True, True, True, False, True, True, True]
]


def total_por_alumno(asistencia):
    resultado = []
    for elemento in asistencia:
        suma = 0
        for i in elemento:
            if i == True:
                suma += 1
        resultado.append(suma)
    return resultado


def total_por_clase(asistencia):
    resultado = []
    for j in range(len(asistencia[0])):
        suma = 0
        for i in range(len(asistencia)):
            if asistencia[i][j] == True:
                suma += 1
        resultado.append(suma)
    return resultado


def alumno_estrella(asistencia):
    lista = total_por_alumno(asistencia)
    return alumnos[lista.index(max(lista))]