# http://progra.usm.cl/apunte/ejercicios/2/numero-letras.html

n = int(input('Ingrese n: '))
i = 0
mas_corta = float('inf')
mas_larga = -1

while i < n:

    palabra = input('palabra ' + str(i + 1) + ': ')
    letras = 0
    apariciones = ''

    for c in palabra:
        if c not in apariciones:
            letras += 1
            apariciones += c

    if letras < mas_corta:
        mas_corta = letras
        palabra_mas_corta = palabra

    if letras > mas_larga:
        mas_larga = letras
        palabra_mas_larga = palabra

    i += 1

print('La palabra mas larga es:', palabra_mas_larga)
print('La palabra mas corta es:', palabra_mas_corta)