def es_cara():
    from random import randint
    return randint(0, 1) == 1

def lanzamiento(monedas):
    i = 0
    suma = 0
    while i < monedas:
        if es_cara():
            suma += 1
        i += 1
    return suma

def maquina(monedas):
    ronda = 0
    while monedas > 0:
        n = lanzamiento(monedas)
        monedas = monedas - n
        ronda += 1
    return ronda

def intentos(monedas, pruebas):
    suma = 0
    i = 0
    while i < pruebas:
        rondas = maquina(monedas)
        suma += rondas
        i += 1
    return suma / pruebas

pruebas = 1000
print('10 monedas:', intentos(10, pruebas), 'intentos promedio')
print('100 monedas:', intentos(100, pruebas), 'intentos promedio')
print('1000 monedas:', intentos(1000, pruebas), 'intentos promedio')
print('10000 monedas:', intentos(10000, pruebas), 'intentos promedio')

# 10 monedas: 4.646 intentos
# 100 monedas: 7.981 intentos
# 1000 monedas: 11.277 intentos
# 10000 monedas: 14.603 intentos