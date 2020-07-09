def eliminar(texto, palabra):
	acum = ''
	final = ''
	for c in texto:
		print(c)
		if c != ' ':
			acum += c
		else:
			print(acum)
			if acum != palabra:
				final += acum + ' '
			acum = ''
	return final[:-1]