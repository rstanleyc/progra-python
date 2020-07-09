# Link video: https://youtu.be/QIae3teRfiw 
# Nombre estudiante: Jeremy Andrew Joy Immediato
# Paralelo: 103
'''
String de prueba
Si desea probar con los datos de prueba del enunciado, puede copiar y pegar como entrada del programa el siguiente texto:
16052000,Sofia;29022000,Silvia;01082000,Andrea;28042000,Paula;04102000,Eduardo;26062001,Pedro;11072001,Federico;03112001,Claudia;20052001,Lucas;24061999,Gabriel;04101999,Camila
'''
#Pregunta 1

def día_de_la_semana(dd,mm,aaaa):
    dia=int(dd)
    mes=int(mm)
    year=int(aaaa)
    a=(14-mes)//12
    y=year-a
    m=mes+(12*a)-2
    d=(dia+y+(y//4)-(y//100)+(y//400)+((31*m)//12))%7
    if d==0:
        return "Domingo"
    elif d==1:
        return "Lunes"
    elif d==2:
        return "Martes"
    elif d==3:
        return "Miércoles"
    elif d==4:
        return "Jueves"
    elif d==5:
        return "Viernes"
    else:
        return "Sábado"

#Pregunta 2

amigos=input("Datos de amigos: ")
amigos+=";"
print("Fecha de nacimiento")
dia=int(input("Día: "))
mes=int(input("Mes: "))
year=int(input("Año: "))
diajuan= día_de_la_semana(dia,mes,year)
print("Naciste un", diajuan)
print("Amigos a invitar:")
fechanombre=""
for x in amigos:
    if x!=";":
        fechanombre+=x
    else:
        nombre=fechanombre[9:len(fechanombre)]
        dia=fechanombre[0:2]
        mes=fechanombre[2:4]
        year=fechanombre[4:8]
        diasemana=día_de_la_semana(dia,mes,year)
        if diasemana==diajuan:
            print(nombre)
        fechanombre=""
        nombre=""
        
#16052000,Sofia
#0123456789






















   
