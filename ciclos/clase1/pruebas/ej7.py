n = int(input('n: '))
suma = 0
i = 0
while i < n:
    suma += (-1)**i * 1 / (2*i+1)
    i += 1
print(suma*4)