#Certamen1progra
#Matias Lozano 201960622-0
#link: https://www.youtube.com/watch?v=WD_BDmP2tc0&t=5s
#link2: https://drive.google.com/file/d/16fYFUmQjcmVyabKAfJf-7eRKaTSjMrJE/view?usp=drivesdk

#a)
def día_de_la_semana(dd,mm,aaaa):
    a=(14-mm)/12
    a1=a%1
    a=a-a1
    y=(aaaa-a)
    y1=y%1
    y=y-y1
    m=mm+(12*a)-2
    m1=m%1
    m=m-m1
    q=y/4
    q1=q%1
    q=q-q1
    w=y/100
    w1=w%1
    w=w-w1
    e=y/400
    e1=e%1
    e=e-e1
    r=((31*m)/(12))
    r1=r%1
    r=r-r1
   
    d=(dd+y+(q)-(w)+(e)+(r))%7
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




#b)

datos=input("Datos de amigos:")
lista=" "
lista2=" "
lista3=""
invitados=" "

print("Fecha de nacimiento")

x=int(input("Dia:"))
y=int(input("Mes:"))
z=int(input("Año:"))
diadenacimiento=día_de_la_semana(x,y,z)
print("Naciste un", diadenacimiento)

for d in datos:
    if d==";":
        for d2 in lista:
            
            
            if d2==",":
                hola=lista2[0:12]
                dia=int(hola[3:5])
                mes=int(hola[5:7])
                ano=int(hola[7:11])
                diadenacimiento2=(día_de_la_semana(dia,mes,ano))
                lista2=""
                

                for d3 in lista:
                    lista3+=d3
                    if d3==";":
                        if diadenacimiento2==diadenacimiento:
                            invitado=lista3[12:1000000]
                            invitados+=invitado
                            lista3=""
                            lista=""
            lista2+=d2
          
    lista+=d
print("Amigos a invitar:", invitados)
  





    






       

























              
    
            
                
                

                
        
        


    
    
