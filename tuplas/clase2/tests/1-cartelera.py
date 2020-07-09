def pelicula_por_pais(cartelera, pais):
    resultado = []
    for mes, pais1, nombre, anio, salas in cartelera:
        if pais == pais1:
            resultado.append((nombre, anio))
    return resultado

def peliculas_por_sala(cartelera, sala):
    d = {}
    for mes, pais1, nombre, anio, salas in cartelera:
        if sala in salas:
            if mes not in d:
                d[mes] = []
            d[mes].append(nombre)
    return d

def mas_antigua(cartelera):
    anio_menor = 30000
    for mes, pais, nombre, anio, salas in cartelera:
        if anio < anio_menor:
            anio_menor = anio
            resultado = (nombre, pais)
    return resultado
