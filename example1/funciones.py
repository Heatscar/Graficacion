import csv
import os

productos = ""
lector = ""

def abrir():
    global productos
    global lector
    productos = open("datos.csv")
    lector = csv.reader(productos)
    #Next sirve para brincarse la primera linea
    next(lector)

def cerrar():
    global productos
    productos.close()

def imprimir():
    for fila in lector:
        #if fila[0].startswith("nombre"):
            #continue
        print("Nombre:", fila[0])
        print("Precio:", fila[1])
        print("Cantidad", fila[2])
    productos.seek(0)
    next(lector)

def agregar(nombre, precio, cantidad):
    cerrar()
    #"a" es para agregar al archivo csv
    productos = open("datos.csv", "a")
    productos.write(nombre + "," + str(precio) + "," + str(cantidad)+"\n")
    productos.close()
    abrir()

def actualizar(nombre, cantidad):
    temporal = open("tmp.csv", "w")
    productos.seek(0)
    for fila in lector:
        if fila[0] == nombre:
            cantidad_final = int(fila[2]) + cantidad
            temporal.write(fila[0] + "," + fila[1] + "," + str(cantidad_final)+"\n")
        else:
            temporal.write(fila[0] + "," + fila[1] + "," + str(fila[2])+"\n")
        
    temporal.close()
    cerrar()
    os.rename("tmp.csv", "datos.csv")
    
    abrir()