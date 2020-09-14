import csv 

productos = ""
lector = ""

def abrir():
    global productos
    global lector
    productos = open("datos.csv")
    lector = csv.reader(productos)


def cerrar():
    global productos
    productos.close()

def imprimir():
    for fila in lector:
        print("Nombre:", fila[0])
        print("Precio:", fila[1])
        print("Cantidad", fila[2])
    productos.seek(0)