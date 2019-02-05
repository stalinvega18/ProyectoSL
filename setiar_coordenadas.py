from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
from tkinter import messagebox
import guardar_coordenas

a = guardar_coordenas.archivo_cor()
def salir():
    respuesta=messagebox.askyesno("Salir","desea terminaar?")
    if respuesta:
        quit()


ventana = Tk()
articulo=StringVar()


ventana.geometry("{0}x{1}".format(ventana.winfo_screenwidth(), ventana.winfo_screenheight()))
ventana.attributes("-toolwindow",-1)
lb_articulo=Label(ventana,text='Articulo: ')
lb_articulo.pack( side = TOP )
bx_articulo=Entry(ventana,textvariable=articulo)
bx_articulo.pack(side = TOP )
frame = Frame(ventana,bd=2, relief=SUNKEN)
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)
canvas = Canvas(width=400, height=300)
canvas.pack(expand=YES, fill=BOTH)
photo=PhotoImage(file='img.png')
canvas.create_image(0,70,image=photo,anchor=NW)
#colocamos la imagen
imagenbtn= PhotoImage(file="salir.png")
i=imagenbtn.subsample(45,45)
btn_terminar=Button(ventana,image=i,command=salir).place(x=745,y=43)


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

        dicionario=a.extraer()
        if a.existencia(dicionario,art):
            confirmacion = messagebox.askyesno("ADVERTENCIA","el articulo ya existe desea modificarlo")
            if confirmacion:
                a.sobreescribir(art,x,y)
        elif insertar(art,x,y):
            a.guardar(art,x, y)
            messagebox.showinfo('Insertado','nuevo articulo ingresado')
    #print (articulo.get(),event.x,event.y)
    articulo.set("")



#evento del raton
canvas.bind("<Button 1>",printcoords)
mainloop()
