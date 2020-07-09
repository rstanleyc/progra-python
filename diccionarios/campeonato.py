# http://progra.usm.cl/apunte/ejercicios/2/campeonato.html
# Campeonato de Futbol

resultados = {
	('Honduras', 'Chile'): (0, 1),
	('Espana', 'Suiza'): (0, 1),
	('Suiza', 'Chile'): (0 ,1),
	('Espana', 'Honduras'): (3, 0),
	('Suiza', 'Honduras'): (0, 0),
	('Espana', 'Chile'): (2, 1)
}

def obtener_lista_equipos(resultados):
	lista = []
	for eq1, eq2 in resultados:
		if eq1 not in lista:
			lista.append(eq1)
		if eq2 not in lista:
			lista.append(eq2)
	return lista


def calcular_puntos(equipo, resultados):
	puntos = 0
	for (eq1, eq2), (g1, g2) in resultados.items():
		if equipo == eq1:
			if g1 > g2:
				puntos += 3
			if g1 == g2:
				puntos += 1
		if equipo == eq2:
			if g2 > g1:
				puntos += 3
			if g2 == g1:
				puntos += 1
	return puntos

def calcular_diferencia_de_goles(equipo, resultados):
	favor = 0
	contra = 0
	for (eq1, eq2), (g1, g2) in resultados.items():
		if equipo == eq1:
			favor += g1
			contra += g2
		if equipo == eq2:
			favor += g2
			contra += g1
	return favor - contra


def goles_anotados(equipo, resultados):
	suma = 0
	for (eq1, eq2), (g1, g2) in resultados.items():
		if equipo == eq1:
			suma += g1
		if equipo == eq2:
			suma += g2
	return suma


def posiciones(resultados):
	lista = []
	equipos = obtener_lista_equipos(resultados)
	for e in equipos:
		p = calcular_puntos(e, resultados)
		dif_goles = calcular_diferencia_de_goles(e, resultados)
		goles = goles_anotados(e, resultados)
		lista.append((p, dif_goles, goles, e))
	lista.sort()
	lista.reverse()
	final = []
	for c in lista:
		final.append(c[-1])
	return final
