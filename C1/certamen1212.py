#https://youtu.be/u2X_1xXJl9o
def día_de_la_semana(dd,mm,aaaa):
    dd=int(dd)
    mm=int(mm)
    aaaa=int(aaaa)
    x=(14-mm)//12
    y=aaaa-x
    m=mm+(12*x)-2
    d=(dd+y+(y//4)-(y//100)+(y//400)+((31*m)//12))%7
    if d==0:
        return "Domingo"
    if d==1:
        return "Lunes"
    if d==2:
        return "Martes"
    if d==3:
        return "Miércoles"
    if d==4:
        return "Jueves"
    if d==5:
        return "Viernes"
    else:
        return "Sábado"

x="16052000,Sofia;29022000,Silvia;01082000,Andrea;28042000,Paula;04102000,Eduardo;26062001,Pedro;11072001,Federico;03112001,Claudia;20052001,Lucas;24061999,Gabriel;04101999,Camila"
a=""
x=x+";"
print("Fecha de nacimiento")
dia=int(input("Día: "))
mes=int(input("Mes: "))
anno=int(input("Año: "))
df=día_de_la_semana(dia,mes,anno)
print("Naciste un",df)
for i in x:
    if i!=";":
        a+=i
    else:
        dia_=int(a[0:2])
        mes_=int(a[2:4])
        anno_=int(a[4:8])
        day=día_de_la_semana(dia_,mes_,anno_)
        nombre=a[9:]
        if dia==day:
            print(nombre)
    
        
    

