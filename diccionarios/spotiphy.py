# spotiphy (ejercicio 2)
# http://progra.usm.cl/Archivos/certamenes/2018_2_C2_CC_CSSJ_VF.pdf
# https://drive.google.com/file/d/1RjzsneVs_ESMrna2OV5uRUZIYDHiY1qJ/view?usp=sharing

evaluaciones = [
   ('Phypocrita', 'Hasta abajo', ['Pynuel'], (2018, 6, 30), 4),
   ('Sin Phyjama', 'Nuevo Estilo', ['Becky T', 'Turize'], (2018, 4, 14), 3),
   ('Vaina Crazy', 'del Weno', ['Ozune', 'Turize'], (2018, 7, 18), 5),
   ('Phypocrita', 'Hasta abajo', ['Pynuel'], (2018, 8, 20), 5),
   ('Quiero Beber Agua', 'Hasta abajo', ['Pynuel'], (2018, 2, 25), 5),
]

'''
Pregunta (a)
Retornar diccionario donde la llave es el nombre del artista y el valor es una
lista de enteros con las evaluaciones de canciones en las que ha participado.
'''
def notas_por_artista(lista):
   d = {}
   for cancion, album, artistas, fecha, nota in lista:
      for artista in artistas:
         if artista not in d:
            d[artista] = []
         d[artista].append(nota)
   return d

print(notas_por_artista(evaluaciones))
# Salida esperada (no necesariamente en el mismo orden):
# {'Ozune': [5], 'Pynuel': [4, 5, 5], 'Becky T': [3], 'Turize': [3, 5]}

'''
Pregunta (b)
Retornar lista con los 3 artistas que con mayor probabilidad producen hits,
ordenada de forma descendente según la probabilidad.
La probabilidad se obtiene al dividir la cantidad de evaluaciones del artista
con nota 4 o 5 entre la cantidad total de evaluaciones del artista
En ambos considerar las evaluaciones hasta la fecha consultada, inclusive.
Si hay menos de 3 artistas con evaluaciones anteriores a la fecha,
entregue una lista con todos los artistas posibles.
Tenga en consideracion que los 3 mejores artistas seleccionados deben tener
probabilidad ≥ a todo el resto de los artistas en SpotiPhy.
'''
def artistas_hit(lista, fecha):
   d = {}
   for cancion, album, artistas, fecha_eval, nota in lista:
      if fecha_eval <= fecha:
         for artista in artistas:
            if artista not in d:
               d[artista] = []
            d[artista].append(nota)
   lista = []
   for artista in d:
      n = 0
      for nota in d[artista]:
         if nota >= 4:
            n += 1
      lista.append((n/len(d[artista]),artista))
   lista.sort()
   lista.reverse()
   resultado = []
   for i in range(min(3,len(lista))):
      resultado.append(lista[i][1])
   return resultado

print(artistas_hit(evaluaciones,(2018,8,30)))
# Salida esperada: ['Pynuel', 'Ozune', 'Turize']

print(artistas_hit(evaluaciones,(2018,2,28)))
# Salida esperada: ['Pynuel']
