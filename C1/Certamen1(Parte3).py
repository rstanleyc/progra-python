# https://youtu.be/RKU4Y57J72M

def dia_de_la_semana(dd,mm,aaaa):
    a = (14-mm)//12
    y = aaaa-a
    m = mm + (12*a) - 2
    d = (dd + y + (y//4) - (y//100) + (y//400) + ((31*m)//12)) % 7
    dia=""
    if d==0:
        dia="Domingo"
    elif d==1:
        dia="Lunes"
    elif d==2:
        dia="Martes"
    elif d==3:
        dia="Miércoles"
    elif d==4:
        dia="Jueves"
    elif d==5:
        dia="Viernes"
    elif d==6:
        dia="Sábado"
    return dia

datosdeamigos = input("Datos de amigos: ")
print("Fecha de nacimiento")
dia=int(input("Dia: "))
mes=int(input("Mes: "))
año=int(input("Año: "))
nacimiento=dia_de_la_semana(dia,mes,año)
print("Naciste un",nacimiento)

print("Amigos a invitar:")
datosdeamigos = datosdeamigos + ";"
datos = " "
nombre= " "
numn= " "
mesn= " "
añon= " "
for x in datosdeamigos:
    if x != ";":
        datos+=x
    else:
        nombre=datos[10:]
        numn=int(datos[1:3])
        mesn=int(datos[3:5])
        añon=int(datos[5:9])
        nacdeamigo=dia_de_la_semana(numn,mesn,añon)
        if nacdeamigo==nacimiento:
            print(nombre)
            nombre=" "
            datos=" "
            numn=" "
            mesn=" "
            añon=" "
            nacdeamigo=" "
            datos=" "
        else:
            nombre=" "
            numn=" "
            mesn=" "
            añon=" "
            nacdeamigo=" "
            datos=" "
    
    
    
