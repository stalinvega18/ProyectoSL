class Archivo:
    def __init__(self):
        print("Super!")

    def guardar(self):
        leer = str(input("Ingrese los productos: "))
        ubicacion = str(input("Ingrese la ubicacion: "))
        archivo=open("productos.txt","a+")
        archivo.write(leer +",")
        archivo.write(ubicacion +"\n")
        archivo.close()

    def imprimir(self):
        arch = self.guardar()
        print(archivo)

archivo = Archivo()
archivo.imprimir()