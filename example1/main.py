import funciones as f

def agregar():
    f.abrir()
    nombre = input("Escribe el nombre: ")
    precio = float(input("Escribe el precio: "))
    cantidad = int(input("Escribe la cantidad: "))

    f.agregar(nombre,precio,cantidad)
    f.imprimir()
    f.cerrar()

def abrir_cerrar():
    f.abrir()
    f.imprimir()
    f.cerrar()


if __name__ == '__main__':
    #abrir_cerrar()
    agregar()