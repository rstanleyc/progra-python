# http://progra.usm.cl/apunte/ejercicios/2/tabla-verdad.html

def predicado(p, q, r):
    return (not p) and (q or r)

def tabla_de_verdad(predicado):
    print('p\t\tq\t\tr\t\tpredicado')
    print('=====\t=====\t=====\t=========')
    i = 1
    while i >= 0:
        j = 1
        while j >= 0:
            k = 1
            while k >= 0:
                print(bool(i),'\t', bool(j), '\t', bool(k), '\t', predicado(bool(i), bool(j), bool(k)))
                k -= 1
            j -= 1
        i -= 1

tabla_de_verdad(predicado)