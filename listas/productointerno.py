# http://progra.usm.cl/apunte/ejercicios/2/producto-interno.html

def producto_interno(a, b):
    i = 0
    suma = 0
    if len(a) != len(b):
        return False
    while i < len(a):
        suma += a[i] * b[i]
        i += 1
    return suma

def son_ortogonales(a, b):
    return producto_interno(a, b) == 0