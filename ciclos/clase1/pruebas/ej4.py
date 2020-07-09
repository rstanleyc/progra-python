suma = 0
flag = True
while flag:
    tiempo = int(input('Duracion tramo: '))
    if tiempo == 0:
        flag = False
    else:
        suma += tiempo

horas = suma // 60
minutos = suma % 60

if minutos <= 9:
    minutos = '0' + str(minutos)
else:
    minutos = str(minutos)

print('Tiempo total de viaje:', str(suma//60) + ':'+minutos,'horas')
