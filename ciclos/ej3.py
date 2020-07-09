'''
Escriba un programa que determine si un número es primo o compuesto.
'''

n = int(input('Ingrese numero: '))
d = 2
es_primo = True

while d < n and es_primo:
    if n % d == 0:
        es_primo = False
    d += 1


if es_primo:
    print('Es primo')
else:
    print('Es compuesto')