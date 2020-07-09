# http://progra.usm.cl/apunte/ejercicios/2/numeros-palindromos.html

def cantidad_digitos(n):
    num = 0
    while n > 0:
        num += 1
        n //=  10
    return num


def invertir_digitos(n):
    i = cantidad_digitos(n)
    suma = 0
    while n > 0:
        digito = n % 10
        suma += digito * 10 ** (i - 1)
        n //= 10
        i -= 1
    return suma

n = int(input('Ingrese n: '))
if n == invertir_digitos(n):
    print('Es palindromo')
else:
    print('No es palindromo')