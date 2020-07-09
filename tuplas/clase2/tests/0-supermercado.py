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
    for boleta_i, cod_prod_i, _ in itemes:
        if codigo == cod_prod_i:
            for boleta_v, fecha, _ in ventas:
                if boleta_i == boleta_v:
                    if fecha > mayor:
                        mayor = fecha
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


def cliente_que_mas_pago(itemes, productos, clientes):
    lista = []
    for rut_c, nombre in clientes:
        suma = 0
        for boleta, fecha, rut_v in ventas:
            if rut_c == rut_v:
                for boleta_i, prod, cant_i in itemes:
                    for cod_p, nombre_p, precio, cant_p in productos:
                        if prod == cod_p:
                            suma += precio * cant_i
                            print
                            nombre
        lista.append((rut_c, suma))
    return lista


def producto_con_mas_ingresos(itemes, productos):
    mayor = 0
    for cod1, nombre1, precio1, cant1 in productos:
        suma = 0
        for boleta2, cod2, cant2 in itemes:
            if cod1 == cod2:
                suma += precio1 * cant2
        if suma > mayor:
            mayor = suma
            nombre_mayor = nombre1
    return nombre_mayor


def ingreso_total_por_ventas(itemes, productos):
    suma = 0
    for boleta1, cod1, cant1 in itemes:
        for cod2, nombre2, precio2, cant2 in productos:
            if cod1 == cod2:
                suma += precio2 * cant1
    return suma


def valor_total_bodega(productos):
    lista = []
    for cod, nombre, precio, cant in productos:
        lista.append(precio * cant)
    return sum(lista)


def valor_total_bodega(productos):
    suma = 0
    for cod, nombre, precio, cant in productos:
        suma += precio * cant
    return suma


def producto_mas_caro_v1(productos):
    lista = []
    for cod, nombre, precio, cant in productos:
        lista.append((precio, nombre))
    lista.sort()
    lista.reverse()
    return lista[0][1]


def producto_mas_caro_v2(productos):
    mayor = -1
    for cod, nombre, precio, cant in productos:
        if precio > mayor:
            mayor = precio
            nombre_mayor = nombre
    return nombre_mayoras_del_mes(2010, 10, itemes, productos, ventas))