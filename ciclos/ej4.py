'''
Un viajero desea saber cuánto tiempo tomó un viaje que realizó. Él tiene la duración en
minutos de cada uno de los tramos del viaje.
Desarrolle un programa que permita ingresar los tiempos de viaje de los tramos y entregue
como resultado el tiempo total de viaje en formato horas:minutos.

El programa deja de pedir tiempos de viaje cuando se ingresa un 0.

Duracion tramo: 15
Duracion tramo: 30
Duracion tramo: 87
Duracion tramo: 0
Tiempo total de viaje: 2:12 horas

Duracion tramo: 51
Duracion tramo: 17
Duracion tramo: 0
Tiempo total de viaje: 1:08 horas
'''

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

print('Tiempo total de viaje:', horas,':',minutos,'horas')