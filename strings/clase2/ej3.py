# http://progra.usm.cl/Archivos/certamenes/2015-2_C1_CC_v2.pdf
# ejercicio 3

def codigo_palabra(codigo):
    i = 1
    mensaje = ''
    while i <= len(codigo):
        if i % 2 != 0:
            mensaje += codigo[-i]
        i += 1
    return mensaje

def codigo_hora(codigo):
    suma = 0
    for c in codigo:
        if c != ':':
            suma += int(c)
        else:
            hora = suma % 24
            suma = 0
    minutos = suma % 60
    return str(hora) + ':' + str(minutos)

flag = True
mensaje = ''
while flag:
    codigo = input('Ingrese codigo: ')
    if ':' not in codigo:
        des = codigo_palabra(codigo)
        if des == 'acun':
            flag = False
        else:
            mensaje += des + ' '
    else:
        des = codigo_hora(codigo)
        mensaje += des + ' '
print('El mensaje es:', mensaje)