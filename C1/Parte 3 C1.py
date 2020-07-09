# Link video: https://youtu.be/X8anAAYPnxM
# Nombre estudiante:Ignacio Pacheco Plastic
# Paralelo:103

def día_de_la_semana(dd,mm,aaaa):
    a=int((14-mm)/12)
    y=int(aaaa-a)
    m=int(mm+(12*a)-2)
    d=int(((dd+y+int((y/4))-int((y/100))+int((y/400))+(int(int(31*m))/12)))%7)
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
    elif d==6:
        return "Sábado"

amigos=input("Datos de amigos: ")
print("Fecha de nacimiento")
dia=int(input("Día: "))
mes=int(input("Mes: "))
año=int(input("Año: "))
dia_nac= día_de_la_semana(dia,mes,año)
print("Naciste un ", dia_nac)
print('Amigos a invitar:')
x=0
for i in amigos:
    x+=1
    if i == ',':
        d=amigos[x-9:x-7]
        m=amigos[x-7:x-5]
        a=amigos[x-5:x-1]
        dia_amigo=día_de_la_semana(int(d),int(m),int(a))
        if dia_amigo == dia_nac:
            v=x
            n_amigo=amigos[v]
            a=amigos[v+1]
            while a != ';' or v == len(amigos):
                n_amigo+=a
                v+=1
                a=amigos[v+1]
            print(n_amigo)
            


            






'''
String de prueba
Si desea probar con los datos de prueba del enunciado, puede copiar y pegar como entrada del programa el siguiente texto:
16052000,Sofia;29022000,Silvia;01082000,Andrea;28042000,Paula;04102000,Eduardo;26062001,Pedro;11072001,Federico;03112001,Claudia;20052001,Lucas;24061999,Gabriel;04101999,Camila
'''
