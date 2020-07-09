'''
Escriba un programa que entregue todos los divisores del número entero ingresado:

Ingrese numero: 200
1 2 4 5 8 10 20 25 40 50 100 200
'''
n = int(input('Ingrese numero: '))
i = 1
while i <= n:
    if n % i == 0:
        print(i, end=' ')
    i += 1