def estafado_por(lista, rut):
    resultado = []
    for rut1, deuda, empresa, fecha in lista:
        if rut == rut1:
            if empresa not in resultado:
                resultado.append(empresa)'

    if len(resultado) == 0:
            return 'Rut no estafado'
    return resultado

def ranking(estafados):
    resultado = {}
    for rut, deuda, empresa, fecha in estafados:
        if empresa not in resultado:
            resultado[empresa] = 0
        resultado[empresa] += deuda
    return resultado


def estafados_por_fecha(estafados, inicial, final):
    resultado = {}
    d, m, a = inicial
    fecha_inicial = (a, m, d)
    d, m, a = final
    fecha_final = (a, m, d)

    for rut, deuda, empresa, fecha in estafados:
        d, m, a = fecha
        fecha_oficial = (a, m, d)
        if fecha_oficial <= fecha_final and fecha_oficial >= fecha_inicial:
            if rut not in resultado:
                resultado[rut] = 0
            resultado[rut] += deuda

    nueva = []
    for rut, deuda in resultado.items():
        nueva.append((deuda, rut))
    nueva.sort()
    nueva.reverse()
    final = []
    for deuda, rut in nueva:
        final.append((rut, deuda))
    return final

