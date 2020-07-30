# Ejercicio 2 - Pythonia
# http://progra.usm.cl/Archivos/certamenes/2015-2_C3_CS.pdf

def datos_por_sector(archivo_mensajes, archivo_ips):
	f_mensajes = open(archivo_mensajes)
	d = {}
	for linea1 in f_mensajes:
		m, ip = linea1.strip().split('@@')
		f_ips = open(archivo_ips)
		for linea2 in f_ips:
			ip2, sec2 = linea2.strip().split(',')
			if ip == ip2:
				sector, desplazamiento = sec2.split('=')
				if sector not in d:
					d[sector] = []
				d[sector].append(descifrar_mensaje(m, int(desplazamiento)))
		f_ips.close()
	f_mensajes.close()
	return d


def descifrar_mensaje(mensaje_cifrado, desplazamiento):
    abecedario = 'abcdefghijklmnopqrstuvwxyz'
    mensaje = []
    mensaje_cifrado = mensaje_cifrado.lower()
    for i in mensaje_cifrado:
        if i not in abecedario:
            mensaje.append(i)
        else:
            mensaje.append(abecedario[list(abecedario).index(i) - desplazamiento])
    return ''.join(mensaje)
