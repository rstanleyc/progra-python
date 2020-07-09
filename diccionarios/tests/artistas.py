artistas = {
    # nombre: codigo, origen, duracion en minutos de la presentacion)
    'Marco Antonio': (1, 'Estados Unidos', 74),
    'Louis Michael': (2, 'Puerto Rico', 70),
    'Mariana Hernandez': (3, 'Chile', 40),
    'Los cuatro': (4, 'Chile', 25),
    'Metallico': (5, 'Estados Unidos', 45),
    'Yutu': (6, 'Irlanda', 80),
    'Justino Vivar': (7, 'Canada', 5),
}

artistas_por_dia = {
    # dia, orden de las presentaciones
    "Lunes": (1,4,3,6,2,5),
    "Martes": (2,5,1),
    "Miercoles": (3,6,2,4),
    "Jueves": (2,5),
}


def cantidad_de_artistas(dia):
    return len(artistas_por_dia[dia])

def nombre_primer_artista(dia):
    cod_origen = artistas_por_dia[dia][0]
    for nombre, (cod, origen, duracion) in artistas.items():
        if cod == cod_origen:
            return nombre

def pais_origen_ultimo(dia):
    cod_origen = artistas_por_dia[dia][-1]
    for nombre, (cod, origen, duracion) in artistas.items():
        if cod == cod_origen:
            return origen

def tiempo_total(dia):
    codigos = artistas_por_dia[dia]
    suma = 0
    for i in codigos:
        for nombre, (cod, origen, duracion) in artistas.items():
            if i == cod:
                suma += duracion
    return suma

dia = input('Ingrese dia: ')
print('Ese dia se presentaran', cantidad_de_artistas(dia), 'artistas')
print('El primer artista del dia sera', nombre_primer_artista(dia))
print('El ultimo artista del dia viene de', pais_origen_ultimo(dia))
print('Ese dia el concierto completo durara', tiempo_total(dia),'minutos')