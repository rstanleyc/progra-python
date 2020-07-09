hora = int(input('Ingrese hora: '))
minutos = int(input('Ingrese minutos: '))

inicio = 6 * 60 + 30
fin = 22 * 60  + 30
inicio_punta1 = 7 * 60 + 30
fin_punta1 = 9 * 60
inicio_punta2 = 18 * 60
fin_punta2 = 19 * 60

actual = hora * 60 + minutos

esta_punta1 = False
esta_punta2 = False
esta_normal1 = False
esta_normal2 = False
esta_normal3 = False

if actual <= inicio or actual >= fin:
    print('Ya no se encuentran trenes en este horario')
else:
    if actual < inicio_punta1:
        esta_normal1 = True
    elif actual <= fin_punta1:
        esta_punta1 = True
    elif actual < inicio_punta2:
        esta_normal2 = True
    elif actual <= fin_punta2:
        esta_punta2 = True
    else:
        esta_normal3 = True

    if esta_normal1 or esta_normal2 or esta_normal3:
        print('Se encuentra en horario normal')
        print('El tren tiene 4 vagones')
        if esta_normal1:
            t = actual - inicio
        if esta_normal2:
            t = actual - fin_punta1
        if esta_normal3:
            t = actual - fin_punta2
        trenes = t // 12
        tiempo_prox_tren = t % 12

    if esta_punta1 or esta_punta2:
        print('Se encuentra en horario punta')
        if esta_punta1:
            t = actual - inicio_punta1
        else:
            t = actual - inicio_punta2
        trenes = t // 6
        tiempo_prox_tren = t % 6
        if trenes % 2 == 0:
            print('El tren tiene 4 vagones')
        else:
            print('El tren tiene 2 vagones')
    if tiempo_prox_tren == 0:
        print('El tren se encuentra en el anden!')
    else:
        print('Debe esperar', tiempo_prox_tren, 'minutos')