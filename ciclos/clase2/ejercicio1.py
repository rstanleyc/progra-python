# ejercicio 3
# http://progra.usm.cl/Archivos/certamenes/2011-1_C1.pdf

n = int(input('Cuantos valores ingresara?: '))
menor = float('inf')
mayor = float('-inf')

i = 0
while i < n:
    dato = float(input('Valor ' + str(i+1) + ': '))
    if dato < menor:
        menor = dato
    if dato > mayor:
        mayor = dato
    i += 1
print('El rango es', round(mayor - menor, 2))