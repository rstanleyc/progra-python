# http://progra.usm.cl/Archivos/certamenes/2016-1_C1.pdf
# ejercicio 3

def valida(cadena):
    validos = 'ATCG '
    letras = 0
    for c in cadena:
        if c not in validos:
            return False

        if c != ' ':
            letras += 1
        else:
            if letras != 4:
                return False
            letras = 0
    return True

def cantidad(cadena, base):
    cuenta = 0
    for c in cadena:
        if c == base:
            cuenta += 1
    return cuenta

n = int(input('Cantidad de cadenas de ADN: '))
i = 0
c_animales = 0
c_vegetales = 0
no_validas = 0
while i < n:
    cadena = input('Ingrese cadena ' + str(i + 1) + ': ')
    if not valida(cadena):
        no_validas += 1
    elif cantidad(cadena, 'C') + cantidad(cadena, 'G') > cantidad(cadena, 'A') + cantidad(cadena, 'T'):
        c_vegetales += 1
    else:
        c_animales += 1
    i += 1
print('Cantidad animales:', c_animales)
print('Cantidad vegetales:', c_vegetales)
print('Cantidad no validas:', no_validas)