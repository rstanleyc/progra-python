# ejercicio 2
# http://progra.usm.cl/Archivos/certamenes/2018-1_C1FINAL.pdf

flag = True
pares = 0
impares = 0
c_bytes = 0
while flag: 
	i = 0
	print('Byte', c_bytes+1)
	suma = 0
	while i < 8:
		bit = int(input('Ingrese bit: '))
		suma += bit * (2 ** i)
		i += 1 
	print(suma)
	if suma == 0: 
		flag = False
	else: 
		c_bytes += 1
		if suma % 2 == 0:  
			pares += 1
		else: 
			impares += 1

print('Bytes:', c_bytes)
print('pares:', pares)
print('impares:', impares)