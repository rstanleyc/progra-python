def producto_interno(a, b):
    i = 0
    suma = 0
    while i < len(a):
        suma += a[i] * b[i]
        i += 1
    return suma

def son_ortogonales(a, b):
    return producto_interno(a, b) == 0