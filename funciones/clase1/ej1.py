# http://progra.usm.cl/apunte/ejercicios/2/tabla-verdad.html

def predicado(p, q, r):
    return (not p) and (q or r)

def tabla_verdad(predicado):
    p = 1
    while p >= 0:
        q = 1
        while q >= 0:
            r = 1
            while r >= 0:
                print(bool(p), bool(q), bool(r), predicado(bool(p), bool(q), bool(r)))
                r -= 1
            q -= 1
        p -= 1
