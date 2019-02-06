class archivo_cor:


    def guardar(self,articulo,x,y,file):
        archivo=open(file,'a')
        archivo.write(str(articulo)+','+str(x)+','+str(y)+'\n')
        archivo.close()


    def extraer(self,file):
        dicio= {}
        archivo = open(file,'r')
        linea = archivo.readline()

        while linea != '':
            div = linea.split(',')
            articulo = div[0].replace("'", '')
            coordX = div[1].replace("'", '')
            coordY = div[2].rstrip('\n')
            dicio[articulo] = [coordX, coordY]

            linea = archivo.readline()

        archivo.close()


        return dicio

    def existencia(self,articulo,file):
        diccionario=self.extraer(file)
        controlador=False
        for key in diccionario:
            if articulo == key:
                controlador=True
                break
        return controlador


    def sobreescribir(self,articulo1,x,y,file):
        archivo = open(file,"r")
        lineas = archivo.readlines()
        archivo.close()
        archivo = open(file,"w")
        for linea in lineas:
            div = linea.split(",")
            articulo= div[0]
            #print(articulo)
            if articulo != articulo1:

                archivo.write(linea)
                #print(linea)

        archivo.close()
        archivo = open(file, 'a')
        archivo.write(str(articulo1) + ',' + str(x) + ',' + str(y) + '\n')
        archivo.close()