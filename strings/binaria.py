# http://progra.usm.cl/Archivos/certamenes/2018-1_C1FINAL.pdf
# ej3

def caracter_raro(cadena):
    for c in cadena:
        if c != '0' and c != '1':
            return True
    return False

flag = True
total = impares = pares = 0

while flag:
    cadena = input('Ingrese cadena binaria: ')
    if len(cadena) < 4 or len(cadena) > 8 or caracter_raro(cadena):
        flag = False
    else:
        i = len(cadena) - 1
        suma = 0
        for c in cadena:
            if c == '1':
                suma += 2 ** i
            i -= 1
        print(suma)
        if suma % 2 == 0:
            pares += 1
        else:
            impares += 1
        total += 1


print('total', total)
print('pares', pares)
print('impares', impares)