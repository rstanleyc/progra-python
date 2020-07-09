# ejercicio 2
# http://progra.usm.cl/Archivos/certamenes/2016-1_C1.pdf

peso_total = 0
ingreso_total = 0
num_bultos = 0
mas_pesado = -1
flag = True

while flag:
    bulto = int(input('Ingrese peso bulto: '))
    if bulto > 500:
        print('No debe sobrepasar el limite de 500kg')
    else:
        if bulto <= 25:
            valor = 1000
        elif bulto <= 300:
            valor = 1500
        elif bulto <= 500:
            valor = 2000

        if peso_total + bulto <= 2000:
            peso_total += bulto
            ingreso_total += valor * bulto
            num_bultos += 1
            if bulto > mas_pesado:
                mas_pesado = bulto
        else:
            print('Limite excedido')
            flag = False

print('Numero total de bultos: ', num_bultos)
print('Peso del bulto mas pesado: ', mas_pesado)
print('Peso promedio de los bultos: ', round(peso_total / num_bultos))
print('Ingreso total por carga:', ingreso_total)