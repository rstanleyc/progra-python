def leer_perros(na):
    pe = {}
    a = open(na)
    for l in a:
        _, n, r, p, s = l.strip().split(';')
        if n not in pe:
            pe[n] = []
        pe[n].append(s)
    a.close()
    return pe

print(leer_perros('perros.txt'))

def leer_razas(nombre_archivo):
    d = {}
    archivo = open(nombre_archivo)
    for linea in archivo:
        _, nombre, raza, _, _ = linea.strip().split(';')
        if raza not in d:
            d[raza] = []
        if nombre not in d[raza]:
            d[raza].append(nombre)
    archivo.close()
    return d

print(leer_razas('perros.txt'))

def mestizos(raza1, raza2, nombre_archivo):
    d = {}
    archivo = open(nombre_archivo)
    for linea in archivo:
        _, nombre, raza, _, _ = linea.strip().split(';')
        if nombre not in d:
            d[nombre] = []
        d[nombre].append(raza)
    archivo.close()
    final = []
    for nombre in d:
        if raza1 in d[nombre] and raza2 in d[nombre]:
            final.append(nombre)
    return final

print(mestizos('salchicha', 'san bernardo', 'perros.txt'))
print(mestizos('pequines', 'labrador', 'perros.txt'))
print(mestizos('pequines', 'pastor aleman', 'perros.txt'))

def solucion_mestizos(raza1, raza2, nombre_archivo):
    d = {}
    soluciones = leer_perros(nombre_archivo)
    perros_mestizos = mestizos(raza1, raza2, nombre_archivo)
    for p in perros_mestizos:
        solu = soluciones[p]
        sin_repeticion = []
        for s in solu:
            if s not in d:
                d[s] = 0
            if s not in sin_repeticion:
                d[s] += 1
            sin_repeticion.append(s)
    return d

print(solucion_mestizos('salchicha', 'san bernardo', 'perros.txt'))
print(solucion_mestizos('pequines', 'labrador', 'perros.txt'))
print(solucion_mestizos('pequines', 'pastor aleman', 'perros.txt'))
