n = int(input('Cuantos valores ingresara?: '))
i = 0
menor = float('inf')
mayor = float('-inf')
while i < n: 
	dato = float(input('Valor ' + str(i+1) + ': '))
	if dato < menor: 
		menor = dato
	if dato > mayor: 
		mayor = dato
	i += 1
print('El rango es', round(mayor - menor, 2))