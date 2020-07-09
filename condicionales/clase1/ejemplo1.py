# Ejemplo 1
# El riesgo de que una persona sufra enfermedades coronarias depende
# de su edad y su índice de masa corporal:

#               edad < 45	 edad ≥ 45
# IMC < 22.0	  bajo	      medio
# IMC ≥ 22.0	  medio	      alto

#Escriba un programa que reciba como entrada la estatura, el peso y la edad de una persona, y le
# entregue su condición de riesgo.


estatura = float(input('Ingrese estatura: '))
peso = float(input('Ingrese peso: '))
edad = int(input('Ingrese edad: '))

IMC = peso / estatura ** 2

print('Su IMC es', round(IMC, 2))


if IMC < 22 and edad < 45:
    print('Su nivel de riesgo es bajo')
elif IMC < 22 and edad >= 45:
    print('Su nivel de riesgo es medio')
else:
    if edad < 45:
        print('Su nivel de riesgo es medio')
    else:
        print('Su nivel de riesgo es alto')


'''
if edad < 45:
    if IMC < 22.0:
        print('Su nivel de riesgo es bajo')
    else:
        print('Su nivel de riesgo es medio')
else:
    if IMC < 22.0:
        print('Su nivel de riesgo es medio')
    else:
        print('Su nivel de riesgo es alto')
'''

