# Ejemplo 0
# Escriba un programa que pida al usuario dos palabras, y que
# indique cuál de ellas es la más larga y por cuántas letras lo es.

palabra1 = input('Ingrese palabra 1: ')
palabra2 = input('Ingrese palabra 2: ')

if len(palabra1) == len(palabra2):
    print('Ambas palabras tienen mismo largo')
elif len(palabra2) > len(palabra1):
    print('Palabra 2 es mayor que palabra 1 en', len(palabra2) - len(palabra1))
else:
    print('Palabra 1 es mayor que palabra 2 en', len(palabra1) - len(palabra2))
