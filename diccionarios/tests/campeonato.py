resultados = {
	('Honduras', 'Chile'): (0, 1), 
	('Espana', 'Suiza'): (0, 1), 
	('Suiza', 'Chile'): (0 ,1), 
	('Espana', 'Honduras'): (3, 0), 
	('Suiza', 'Honduras'): (0, 0), 
	('Espana', 'Chile'): (2, 1)
}

def obtener_lista_equipos(resultados): 
	c = set()
	for i in resultados: 
		eq1, eq2 = i
		c.add(eq1)
		c.add(eq2)
	return list(c)
	
def obtener_lista_equipo_v2(resultados): 
	l = []
	for eq1, eq2 in resultados.keys(): 
		if eq1 not in l: 
			l.append(eq1)
		if eq2 not in l: 
			l.append(eq2)
	return l

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
	favor = contra = 0
	for (eq1, eq2), (g1, g2) in resultados.items(): 
		if equipo == eq1: 
			favor += g1
			contra += g2
		if equipo == eq2: 
			favor += g2
			contra += g1
	return favor - contra
	
def calcular_diferencia_de_goles_v2(equipo, resultados): 
	diferencia = 0
	for (eq1, eq2), (g1, g2) in resultados.items(): 
		if equipo == eq1: 
			diferencia += g1 - g2
		if equipo == eq2: 
			diferencia += g2 - g1
	return diferencia

def goles_anotados(equipo, resultados):
	suma = 0
	for (eq1, eq2), (g1, g2) in resultados.items(): 
		if equipo == eq1: 
			suma += g1
		if equipo == eq2: 
			suma += g2
	return suma

def posiciones(resultados):
	ordenado = []
	mayor = -1
	equipos = obtener_lista_equipos(resultados)
	for e in equipos:
		p = calcular_puntos(e, resultados)
		dif_goles = calcular_diferencia_de_goles(e, resultados)
		goles = goles_anotados(e, resultados)
		ordenado.append((p, dif_goles, goles, e))
	ordenado.sort()
	ordenado.reverse()
	final = []
	for c in ordenado:
		final.append(c[-1])
	return final