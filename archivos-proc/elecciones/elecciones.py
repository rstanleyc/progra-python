def resultados(vot, can):
    d = {}
    validos = 0
    nombres = []
    f_candidatos = open(can)
    for linea in f_candidatos:
        cod, nombre = linea.strip().split(':')
        nombres.append(nombre)
        f_votaciones = open(vot)
        for linea2 in f_votaciones:
            rut, cod2 = linea2.strip().split(':')
            if cod == cod2:
                validos += 1
                if nombre not in d:
                    d[nombre] = 0
                d[nombre] += 1
        f_votaciones.close()
    f_candidatos.close()

    lista = []
    for nombre in nombres:
        if nombre in d:
            lista.append((round(d[nombre] / validos * 100, 1), nombre))
        else:
            lista.append((0.0, nombre))
    lista.sort()
    lista.reverse()

    resultados = open('resultados.txt', 'w')
    resultados.write('Total de votos: {}\n\n'.format(validos))
    for porcentaje, nombre in lista:
        resultados.write('{} {} %\n'.format(nombre, porcentaje))
    resultados.close()

resultados('votaciones.txt', 'candidatos.txt')
