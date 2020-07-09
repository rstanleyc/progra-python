# Link video:https://drive.google.com/file/d/1Ga_JpmWAP4diE1FjS4qnKl9pd65ee2JV/view?usp=sharing
# Nombre estudiante:Camila Pereira Perez
# Paralelo:103


'''
String de prueba
Si desea probar con los datos de prueba del enunciado, puede copiar y pegar como entrada del programa el siguiente texto:
16052000,Sofia;29022000,Silvia;01082000,Andrea;28042000,Paula;04102000,Eduardo;26062001,Pedro;11072001,Federico;03112001,Claudia;20052001,Lucas;24061999,Gabriel;04101999,Camila
'''
#1
def dia_de_la_semana(dd,mm,aaaa):
    dia = ""
    a = (14 - mm)//12
    y = aaaa - a
    m = mm +(12*a)-2
    d = dd+y+(y//4)-(y//100)+(y//400)+(31*m)//12
    d = d % 7
    if d == 0:
        dia = "Domingo"
    elif d == 1:
        dia = "Lunes"
    elif dia == 2:
        dia = "Martes"
    elif d == 3:
        dia = "Miércoles"
    elif d == 4:
        dia = "Jueves"
    elif d == 5:
        dia = "Viernes"
    elif d ==6:
        dia = "Sábado"
    return dia
#2
datos = input("Datos de amigos:")
print("Fecha de nacimiento")
dd = int(input("Día:"))
mm = int(input("Mes:"))
aaaa = int(input("Año:"))
r = dia_de_la_semana(dd,mm,aaaa)
print("Naciste un", r)
print("Amigos a invitar:")
i = 0
i2 = 0
s = ""
for x in datos:
  while i < len(datos):
    while x != ";":
        s += x
        i2 += 1
    dia = int(s[0:2])
    mes = int(s[2:4])
    año = int(s[4:8])
    nombre = s[8:]
    invitado = dia_de_la_semana(dia,mes,año)
    if invitado == nacio :
        print(nombre)
    i += i2
















