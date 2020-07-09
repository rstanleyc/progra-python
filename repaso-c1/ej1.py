mayor = -1
mejor = 0
continuar = True
participante = 1
while continuar:
	# Procesamiento de un participante
	print('PARTICIPANTE', participante)
	# Calificación del primer juez
	puntaje = int(input('Puntaje: '))
	if puntaje>=0:
		# Calificación del resto de los jueces
		suma = puntaje
		i = 1
		while i<3:
			puntaje = int(input('Puntaje: '))
			suma += puntaje
			i += 1
		# Se calcula promedio y se compara con el máximo
		puntaje = round(suma/3)
		print('Promedio:', puntaje)
		if puntaje>mayor:
			mayor = puntaje
			mejor = participante
		participante += 1
	else:
		# Si el primer juez ingresa calificación negativa, termina
		continuar = False
print('Ganador: Participante', mejor, 'con promedio', mayor)
