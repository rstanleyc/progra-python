# http://progra.usm.cl/apunte/ejercicios/2/supermercado.html

productos = [
    (41419, 'Fideos',        450, 210),
    (70717, 'Cuaderno',      900, 119),
    (78714, 'Jabon',         730, 708),
    (30877, 'Desodorante',  2190,  79),
    (47470, 'Yogur',          99, 832),
    (50809, 'Palta',         500,  55),
    (75466, 'Galletas',      235,   0),
    (33692, 'Bebida',        700,  20),
    (89148, 'Arroz',         900, 121),
    (66194, 'Lapiz',         120, 900),
    (15982, 'Vuvuzela',    12990,  40),
    (41235, 'Chocolate',    3099,  48),
]

clientes = [
    ('11652624-7', 'Perico Los Palotes'),
    ('8830268-0', 'Leonardo Farkas'),
    ('7547896-8', 'Fulanita de Tal'),
]

ventas = [
    (1, (2010,  9, 12),  '8830268-0'),
    (2, (2010,  9, 19), '11652624-7'),
    (3, (2010,  9, 30),  '7547896-8'),
    (4, (2010, 10,  1),  '8830268-0'),
    (5, (2010, 10, 13),  '7547896-8'),
    (6, (2010, 11, 11), '11652624-7'),
]

itemes = [
    (1, 89148,  3),
    (2, 50809,  4),
    (2, 33692,  2),
    (2, 47470,  6),
    (3, 30877,  1),
    (4, 89148,  1),
    (4, 75466,  2),
    (5, 89148,  2),
    (5, 47470, 10),
    (6, 41419,  2),
]

def fecha_ultima_venta_producto(codigo, itemes, ventas):
    mayor = (1900, 1, 1)
    for boleta_i, cod_prod_i, cant_i in itemes:
        if codigo == cod_prod_i:
            for boleta_v, fecha_v, rut_v in ventas:
                if boleta_v == boleta_i:
                    if fecha_v > mayor:
                        mayor = fecha_v
    return mayor

def total_ventas_del_mes(anio, mes, itemes, productos, ventas):
    suma = 0
    for boleta_v, (anio_v, mes_v, dia_v), rut_v in ventas:
        if anio_v == anio and mes_v == mes:
            for boleta_i, cod_i, num_i in itemes:
                if boleta_v == boleta_i:
                    for cod_p, nom_p, precio_p, stock_p in productos:
                        if cod_p == cod_i:
                            suma += precio_p * num_i
    return suma

def cliente_que_mas_pago(itemes, productos, clientes, ventas):
    lista = []
    for rut_c, nombre_c in clientes:
        suma = 0
        for boleta_v, fecha_v, rut_v in ventas:
            if rut_c == rut_v:
                for boleta_i, cod_i, cant_i in itemes:
                    if boleta_i == boleta_v:
                        for cod_p, nombre_p, precio_p, stock_p in productos:
                            if cod_p == cod_i:
                                suma += precio_p * cant_i
        lista.append((suma, nombre_c))
    lista.sort()
    return lista[-1][1]



def producto_con_mas_ingresos(itemes, productos):
    mayor = -1
    for cod_p, nombre_p, precio_p, stock_p in productos:
        suma = 0
        for boleta_i, cod_i, cant_i in itemes:
            if cod_p == cod_i:
                suma += precio_p * cant_i
        if suma > mayor:
            mayor = suma
            nombre_mayor = nombre_p
    return nombre_mayor



def ingreso_total_por_ventas(itemes, productos):
    suma = 0
    for boleta_i, cod_i, cant_i in itemes:
        for cod_p, nombre_p, precio_p, stock_p in productos:
            if cod_p == cod_i:
                suma += precio_p * cant_i
    return suma


def valor_total_bodega2(productos):
    lista = []
    for _, _, precio, cant in productos:
        lista.append(precio * cant)
    return sum(lista)

def valor_total_bodega1(productos):
    suma = 0
    for _, _, precio, cant in productos:
        suma += precio * cant
    return suma


def producto_mas_caro2(productos):
    lista = []
    for cod, nombre, precio, cant in productos:
        lista.append((precio, nombre))
    lista.sort()
    return lista[-1][1]


def producto_mas_caro1(productos):
    mayor = -1
    for cod, nombre, precio, cant in productos:
        if precio > mayor:
            mayor = precio
            nombre_mayor = nombre
    return nombre_mayor

