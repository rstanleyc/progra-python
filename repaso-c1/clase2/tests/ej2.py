# deuman (ej2)
# http://progra.usm.cl/Archivos/certamenes/2019-1_C1.pdf

def mejor(votos):
    vot = str(votos)
    final = 'ABCD'
    mayor = -1
    i = 0
    for v in vot:
        if int(v) > mayor:
            mayor = int(v)
            pos_mayor = i
        i += 1
    if mayor < 4:
        return ''
    return final[pos_mayor]


i = 0
cont_a = cont_b = cont_c = cont_d = 0
mayor = -1
while i < 1000:
    votos = int(input('Voto? '))
    v = mejor(votos)
    if v == 'A':
        cont_a += 1
        if cont_a > mayor:
            mayor = cont_a
            favorita = 'A'
    if v == 'B':
        cont_b += 1
        if cont_b > mayor:
            mayor = cont_b
            favorita = 'B'
    if v == 'C':
        cont_c += 1
        if cont_c > mayor:
            mayor = cont_c
            favorita = 'C'
    if v == 'D':
        cont_d += 1
        if cont_d > mayor:
            mayor = cont_d
            favorita = 'D'
    i += 1

print('La favorita es', favorita, 'con', mayor, 'votos')


