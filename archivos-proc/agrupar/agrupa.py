def agrupar(fecha):
    d = {}
    anio, mes, dia = fecha
    f_salidas = open('salidas-{}-{}-{}.csv'.format(anio, mes, dia))
    for linea in f_salidas:
        vuelo, ciudad, hora = linea.strip().split(';')
        if ciudad not in d:
            d[ciudad] = []
        if vuelo[:2] not in d[ciudad]:
            d[ciudad].append(vuelo[:2])
    final = []
    for destino, aerolineas in d.items():
        final.append((len(aerolineas), destino))
    final.sort()
    final.reverse()

    destinos = open('destinos.txt', 'w')
    for num, destino in final:
        destinos.write('{}:{}\n'.format(destino, num))
    destinos.close()
    return len(final)

print(agrupar(('2019', '08', '09')))