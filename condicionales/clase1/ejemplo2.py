# Ejemplo 2
# Considerar la siguiente tabla que muestra la tasa de impuesto a pagar por una persona según su sueldo.

#           Sueldo	                Tasa de impuesto
#       menos de 1000	                0%
#       1000 ≤ sueldo < 2000	        5%
#       2000 ≤ sueldo < 4000	        10%
#       4000 o más	                    12%


sueldo = int(input('Ingrese su sueldo: '))

if sueldo < 1000:
    tasa = 0.0

if sueldo >= 1000 and sueldo < 2000:
    tasa = 0.05

if sueldo >= 2000 and sueldo < 4000:
    tasa = 0.10

if sueldo >= 4000:
    tasa = 0.12

print('Usted pagara', tasa * sueldo, 'de impuesto')


'''
if sueldo < 1000:
    tasa = 0
elif sueldo < 2000:
    tasa = 0.05
elif sueldo < 4000:
    tasa = 0.1
else:
    tasa = 0.12
print('Usted pagara', tasa * sueldo, 'de impuesto')
'''