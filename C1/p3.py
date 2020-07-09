# Link video: https://youtu.be/EaRIR0EgpKI
# Nombre estudiante: Pablo Ignacio Esparza Contreras
# Paralelo: 103


'''
String de prueba
Si desea probar con los datos de prueba del enunciado, puede copiar y pegar como entrada del programa el siguiente texto:
16052000,Sofia;29022000,Silvia;01082000,Andrea;28042000,Paula;04102000,Eduardo;26062001,Pedro;11072001,Federico;03112001,Claudia;20052001,Lucas;24061999,Gabriel;04101999,Camila
'''

def dia_de_la_semana(dd,mm,aaaa):
    dia=''
    a=int((14-mm)/12)
    y=(aaaa)-a
    m=(mm)+(12*a)-2
    d=int((dd+y+int(y/4)-int(y/100)+int(y/400)+((31*m)/12))%7)
    if d==0:
        dia='Domingo'
    if d==1:
        dia='Lunes'
    if d==2:
        dia='Martes'
    if d==3:
        dia='Miércoles'
    if d==4:
        dia='Jueves'
    if d==5:
        dia='Viernes'
    if d==6:
        dia='Sabado'
    return dia
i=0
m=0
d=0
a=0

datos=input('Datos de amigos: ')+';'
print('Fecha de nacimiento')
dd=int(input('Día: '))
mm=int(input('Mes: '))
aaaa=int(input('Año: '))
x= dia_de_la_semana(dd,mm,aaaa)
print('Naciste un ',x)
print('Amigos a invitar:')
while i<len(datos)-10:
    nombre=''
    d=int(datos[i]+datos[i+1])
    m=int(datos[i+2]+datos[i+3])
    a=int(datos[i+4]+datos[i+5]+datos[i+6]+datos[i+7])
    i+=9
    while datos[i]!=';':
        nombre+=str(datos[i])
        i+=1
    if dia_de_la_semana(d,m,a)==x:
        print(nombre)
    d=0
    m=0
    a=0
    i+=1


        
        
    
