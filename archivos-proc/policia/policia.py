def filtrar(nombre_archivo, anio):
    dicc = {}
    archivo = open(nombre_archivo, 'r')
    for linea in archivo:
        _, nombre, pais, fecha = linea.strip().split(':')
        anio1 = fecha.split('-')[2]
        if int(anio1) == anio:
            if pais not in dicc:
                dicc[pais] = []
            dicc[pais].append(nombre)
    archivo.close()
    return dicc

print(filtrar('inmigrantes.txt', 2019))

def contar_ingresos(nombre_archivo, anio):
    paises = filtrar(nombre_archivo, anio)
    d = {}
    for p in paises:
        d[p] = len(paises[p])
    return d

print(contar_ingresos('inmigrantes.txt', 2019))
print(contar_ingresos('inmigrantes.txt', 2018))

def escribir_ingresos(nombre_archivo, anio):
    ingresos = contar_ingresos(nombre_archivo, anio)
    lista = []
    for i in ingresos:
        lista.append((ingresos[i], i))
    lista.sort()
    lista.reverse()

    f = open('ingresos{}.txt'.format(anio), 'w')
    c = 1
    suma = 0
    for num, pais in lista:
        f.write('{}-{}:{}\n'.format(c, pais, num))
        suma += int(num)
        c += 1
    f.close()
    return suma

print(escribir_ingresos('inmigrantes.txt', 2019))
print(escribir_ingresos('inmigrantes.txt', 2018))