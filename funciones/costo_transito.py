# ejercicio 3
# http://progra.usm.cl/Archivos/certamenes/2016-2_C1.pdf

def costo_transito(min_comb):
    minutos = min_comb
    if minutos <= 480:
        horas = 0
    else:
        minutos = minutos - 480
        horas = minutos // 60
        if minutos % 60 != 0:
            horas += 1
    return 5000 * horas

def costo_pasajero(hrs_viaje, costo_base, min_comb):
    return hrs_viaje * 30000 + costo_base + costo_transito(min_comb)

costo_menor = float('inf')
mejor_vuelo = ''
flag = True
while flag:
    vuelo = input('Vuelo: ')
    if vuelo == '':
        flag = False
    else:
        horas = int(input('horas: '))
        minutos = int(input('minutos combinacion: '))
        costo_base = int(input('costo base: '))
        costo_p = costo_pasajero(horas, costo_base, minutos)
        if costo_p < costo_menor:
            costo_menor = costo_p
            mejor_vuelo = vuelo
print('Mejor vuelo:', mejor_vuelo)
print('Costo pasajero:', costo_menor)

