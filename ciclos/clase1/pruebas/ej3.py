n = int(input('Ingrese un numero: '))
d = 2
es_primo = True

while d < n and es_primo:
    if n % d == 0:
        es_primo = False
    d += 1
    print('iteracion')

if es_primo:
    print('Es primo')
else:
    print('Es compuesto')