# http://progra.usm.cl/apunte/ejercicios/2/funciones-numeros-primos.html

def es_divisible(n, d):
    return n % d == 0

def es_primo(n):
    d = 2
    while d < n:
        if es_divisible(n, d):
            return False
        d += 1
    return True

def i_esimo_primo(i):
    candidato = 2
    c = 0
    while c < i:
        if es_primo(candidato):
            primo = candidato
            c += 1
        candidato += 1
    return primo

n = int(input('Cuantos primos de Mersenne: '))
i = 0
j = 1
while i < n:
    candidato = 2 ** i_esimo_primo(j) - 1
    if es_primo(candidato):
        print(candidato)
        i += 1
    j += 1
