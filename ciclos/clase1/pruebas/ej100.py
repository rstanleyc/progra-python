x = float(input('x: '))
p = float(input('p: '))
flag = True
t1 = 0
i = 1
suma = 0
while flag:
    fact = 1
    j = 1
    while j <= i:
        fact = fact * j
        j += 1

    t2 = (-1) ** (i - 1) * x ** i / fact
    dif = t2 - t1
    if dif <= p:
        flag = False
    else:
        suma = suma + t2
        t1 = t2
        i += 1
print(suma)
