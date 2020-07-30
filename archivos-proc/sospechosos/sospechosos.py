# Ejercicio 2 - Sospechosos
# http://progra.usm.cl/Archivos/certamenes/2014-2_C3_CCyCSSJ_VF.pdf

def peligro(personas, publicaciones, claves):
	s = sospechosos(personas, publicaciones)
	palabras_clave = leer_mensajes(personas, publicaciones, claves)
	peligrosos = []
	for rut in s:
		f_personas = open(personas)
		for linea in f_personas:
			rut2, edad, niveles = linea.strip().split(',')
			niveles = list(map(int, niveles.split('-')))
			promedio = sum(niveles) / 3.0
			if rut == rut2:
				if palabras_clave[rut] >= 2 and promedio >= 30:
					peligrosos.append(rut)
		f_personas.close()
	return peligrosos

def leer_mensajes(personas, publicaciones, claves):
	s = sospechosos(personas, publicaciones)
	resultado = {}
	for rut in s:
		resultado[rut] = 0
		f_mensajes = open(rut + '.txt')
		lista = []
		for linea in f_mensajes:
			lista.append(linea.strip())
		texto = ' '.join(lista)
		#texto = ''
		#for linea in f_mensajes:
		#	texto += linea.strip()
		f_mensajes.close()
		for clave in claves:
			if clave in texto:
				resultado[rut] += 1
	return resultado


def sospechosos(personas, publicaciones):
	f_personas = open(personas)
	resultado = set()
	for linea in f_personas:
		rut, edad, niveles = linea.strip().split(',')
		f_publicaciones = open(publicaciones)
		tiene_twitter = False
		for linea2 in f_publicaciones:
			rut2, medio = linea2.strip().split(':')
			if rut == rut2 and int(edad) < 41 and medio != 'twitter':
				resultado.add(rut)
	f_personas.close()
	return resultado
