

def volumen(t):
	a, b, c = t
	return a * b * c
def distancia(t): 
	x, y = t
	return (x ** 2 + y ** 2) ** 0.5

def viajes_a_realizar(encomiendas, destinos): 
	lista = []
	final = []
	for cod, tupla_vol in encomiendas.items(): 
		for cod1, tupla_dis in destinos: 
			if cod == cod1: 
				d = distancia(tupla_dis)
				ingreso = 0.1 * volumen(tupla_vol) * d
				lista.append((ingreso, cod, d))
	lista.sort()
	lista.reverse()
	for i, c, d in lista: 
		if d <= 30: 
			final.append(c)
	return final[:10]