# Enlace del vídeo
#https://youtu.be/7eExs0eu8QE 
def dia_de_la_semana(dd,mm,aaaa):
    a=(14-mm)//12
    y=aaaa-a
    m=mm+(12*a)-2
    d=(dd+y+(y//4)-(y//100)+(y//400)+((31*m)//12))%7
    if d==1:
        dia="Lunes"
    if d==2:
        dia="Martes"
    if d==3:
        dia="Miércoles"
    if d==4:
        dia="Jueves"
    if d==5:
        dia="Viernes"
    if d==6:
        dia="Sábado"
    if d==0:
        dia="Domingo"
    return dia


print("Fecha de nacimiento")
dia=int(input("Día: "))
mes=int(input("Mes: "))
amo=int(input("Año: "))
nac=dia_de_la_semana(dia,mes,amo)
print("Naciste un",nac)
a="16052000,Sofia;29022000,Silvia;01082000,Andrea;28042000,Paula;04102000,Eduardo;26062001,Pedro;11072001,Federico;03112001,Claudia;20052001,Lucas;04101999,Camila"
a+=";"
t=""
for p in a:
    if p not in "qwertyuiopñlkjhgfdsazxcvbnmQWERTYUIOPÑLKJHGFDSAZXCVBNM,":
        t+=p
t=t.split(";")        
for m in t:
    d=int(m[0]+m[1])
    n=int(m[2]+m[3])
    ji=int(m[4]+m[5]+m[6]+m[7])
    p=m[0]+m[1]+m[2]+m[3]+m[4]+m[5]+m[6]+m[7]
    na=dia_de_la_semana(d,n,ji)
    if na==nac:
        h=t.index(p)
        n=a[h:]
        print ("Amigos a invitar")
        print(n)
        
        
             
        
    
    
    
       
