tipo = input('Tipo de vehiculo: ')
dia = input('Dia: ')
hora = int(input('Hora: '))
minutos = int(input('Minutos: '))
if tipo == 'auto':
    pasajeros = int(input('Cantidad Pasajeros: '))

final = hora * 60 + minutos

if dia == 'lunes' or dia == 'martes' or dia == 'miercoles' or dia == 'jueves' or dia == 'viernes':
    if final >= 450 and final <= 570 or final >= 1050 and final <= 1200:
        if tipo == 'auto':
            if pasajeros >= 3:
                pago = 0
            else:
                pago = 2400
        else:
            pago = 3500
    else:
        if tipo == 'auto':
            pago = 2000 - 100 * pasajeros
        else:
            pago = 2500
else:
    if final >= 510 and final <= 660 or final >= 1065 and final <= 1350:
        if tipo == 'auto':
            pago = 4500 - 300 * pasajeros
        else:
            pago = 4500
    else:
        if tipo == 'auto':
            pago = 2800
        else:
            pago = 3800
print('Total a pagar:', pago)
