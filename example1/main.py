import funciones as f

def agregar():
    f.abrir()
    nombre = input("Escribe el nombre: ")
    precio = float(input("Escribe el precio: "))
    cantidad = int(input("Escribe la cantidad: "))

    f.agregar(nombre,precio,cantidad)
    f.imprimir()
    f.cerrar()

def cambiar_cantidad():
    f.abrir()
    nombre = input("Escribe el nombre: ")
    cantidad = int(input("Escribe la cantidad: "))

    f.actualizar(nombre,cantidad)
    f.imprimir()
    f.cerrar()

def vender_producto():
    f.abrir()
    nombre = input("Escribe el nombre: ")
    cantidad = int(input("Escribe la cantidad: "))

    f.vender(nombre,cantidad)
    f.imprimir()
    f.cerrar()

def abrir_cerrar():
    f.abrir()
    f.imprimir()
    f.cerrar()


if __name__ == '__main__':
    #agregar()
    #cambiar_cantidad()
    vender_producto()
    #abrir_cerrar()