from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
from tkinter import messagebox
import tkinter as tk
from tkinter import filedialog
import guardar_coordenas
from pathlib import Path
import os.path as path




#VARIABLES
extension=".txt"
global dibujo
ubicacion=""
lista = []
a = guardar_coordenas.archivo_cor()
ventana = Tk()
imagenAnchuraMaxima=ventana.winfo_screenwidth()
imagenAlturaMaxima=ventana.winfo_screenheight()
articulo=StringVar()
btn_terminar=Button

#=============================================

#METODOS
def salir():
    respuesta=messagebox.askyesno("Salir","desea terminaar?")
    if respuesta:
        quit()


def limpiar(dibujo):
    #print(dibujo)
    lista.append(dibujo)
    if len(lista) == 1:
        pass
    else:
        #print(lista[len(lista)-2])
        canvas.delete(lista[len(lista)-2])


def limpiar_agregar(dibujo):
    canvas.delete(dibujo)


def mostrar_articulo():
    art = articulo.get()
    if not art:
        messagebox.showinfo("ATENCION", 'Debe ingresar un articulo')
    else:
        dicionario = a.extraer(ubicacion)
        if not a.existencia(art,ubicacion):
            messagebox.showinfo("ATENCION", 'el articulo no esta disponible')
        else:
            coordX = int(dicionario[art][0])
            coordY = int(dicionario[art][1])
            color = "#FF0000"
            x1, y1 = (coordX - 10), (coordY - 10)
            x2, y2 = (coordX + 10), (coordY + 10)
            dibujo=canvas.create_oval(x1, y1, x2, y2, fill=color)
            limpiar(dibujo)



    articulo.set("")


def selecionar_foto():
    global imagenL
    global ubicacion
    ventana.filename = filedialog.askopenfilename(initialdir="./imagenes")
    ruta = ventana.filename
    path = str(ruta).split('/')
    ub = Path(path[-1]).stem
    ubicacion =ub+extension
    imagen = Image.open(ruta)
    imagen1=imagen.resize((imagenAnchuraMaxima,imagenAlturaMaxima ), Image.ANTIALIAS)
    imagenL = ImageTk.PhotoImage(imagen1)
    canvas.create_image(0, 62, anchor=NW, image=imagenL)



def agregar():

    global i
    global btn_terminar
    imagenbtn = PhotoImage(file="salir.png")
    i = imagenbtn.subsample(45, 45)
    btn_terminar = Button(ventana, image=i, command=salir)
    btn_terminar.place(x=745, y=43)
    btn_buscar.place_forget()
    lb_articulo.configure(text="Agregar")
    setiar()

def buscar():
    btn_buscar.place(x=733,y=49)
    lb_articulo.configure(text="Buscar")
    btn_terminar.place_forget()


#=====================cCOMIENZO GUI=====================

#BARRA DE MENU
menu1 = tk.Menu(ventana)
opciones1 = tk.Menu(menu1)
opciones1.add_command(label="Foto",command=selecionar_foto)
opciones1.add_command(label="Agregar",command=agregar)
opciones1.add_command(label="Buscar",command=buscar)
opciones1.add_command(label="Salir",command=salir)

menu1.add_cascade(label="Archivo", menu=opciones1)
menu1.add_cascade(label="Ayuda")
ventana.config(menu=menu1)

#FRAME
ventana.geometry("{0}x{1}".format(ventana.winfo_screenwidth(), ventana.winfo_screenheight()))
lb_articulo=Label(ventana,text='BUSCAR: ')
lb_articulo.pack( side = TOP )
bx_articulo=Entry(ventana,textvariable=articulo)
bx_articulo.pack(side = TOP )
frame = Frame(ventana,bd=2, relief=SUNKEN)
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)
canvas = Canvas(width=400, height=300)
canvas.pack(expand=YES, fill=BOTH)
messagebox.showinfo("COMENZAR","seleccione el lugar de trabajo en la pestaña Archivo")

#COMIENZO EN BUSQUEDA
imagenbtn1= PhotoImage(file="lupa.png")
i1=imagenbtn1.subsample(4,4)
btn_buscar=Button(ventana,image=i1,command=mostrar_articulo)
btn_buscar.place(x=733,y=49)



#============= METODOS PARA AGREGAR
def insertar(a,x,y):
    respuesta=messagebox.askyesno("AGREGAR","su articulo para insertar es "+a+' en las cordenadas '+str(x)+', '+str(y))
    return respuesta

def printcoords(event):
    x=event.x
    y=event.y
    art=articulo.get()
    if not art:
        messagebox.showinfo("ATENCION",'Debe ingresar un articulo')
    else:
        if path.exists(ubicacion):
            if a.existencia(art,ubicacion):
                confirmacion = messagebox.askyesno("ADVERTENCIA","el articulo ya existe desea modificarlo")
                if confirmacion:
                    a.sobreescribir(art,x,y,ubicacion)
            elif insertar(art,x,y):
                a.guardar(art,x, y,ubicacion)
                messagebox.showinfo('Insertado','nuevo articulo ingresado')
        elif insertar(art, x, y):
            a.guardar(art, x, y, ubicacion)
            messagebox.showinfo('Insertado', 'nuevo articulo ingresado')
    #print (articulo.get(),event.x,event.y)
    articulo.set("")

#evento del raton
def setiar():
    canvas.bind("<Button 1>",printcoords)


mainloop()
