def guardar():
    leer = str(input("Ingrese los productos: "))
    ubicacion = str(input("Ingrese la ubicacion: "))
    archivo=open("ingresoinfo.txt","a+")
    archivo.write(leer +",")
    archivo.write(ubicacion +"\n")
    archivo.close()

guardar()
