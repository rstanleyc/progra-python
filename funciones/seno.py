# http://progra.usm.cl/apunte/ejercicios/2/aprox-seno-coseno.html

def factorial_reciproco(n):
    i = 1
    factorial = 1
    while i <= n:
        factorial *= i
        i += 1
    return 1 / factorial

def signo(n):
    if n % 2 == 0:
        return 1
    return -1

def seno_aprox(x, m):
    i = 0
    suma = 0
    while i < m:
        suma += signo(i) * x ** (2 * i + 1) * factorial_reciproco(2 * i + 1)
        i += 1
    return suma