# http://progra.usm.cl/apunte/ejercicios/2/numeros-palindromos.html

def num_digitos(n):
    i = 0
    while n > 0:
        n //= 10
        i += 1
    return i

def invertir_digitos(n):
    i = num_digitos(n)
    suma = 0
    while n > 0:
        digito = n % 10
        n //= 10
        suma += digito * 10 ** (i - 1)
        i -= 1
    return suma

n = int(input('Ingrese n: '))
if n == invertir_digitos(n):
    print('Es palindromo')
else:
    print('No es palindromo')