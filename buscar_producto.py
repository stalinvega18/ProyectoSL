from tkinter import messagebox
from tkinter import *
import guardar_coordenas
import time

global dibujo
dibujo = 0
lista = []
a = guardar_coordenas.archivo_cor()
ventana = Tk()
articulo=StringVar()

def salir():
    respuesta=messagebox.askyesno("Salir","desea terminaar?")
    if respuesta:
        quit()


def limpiar(dibujo):
    print(dibujo)
    lista.append(dibujo)
    if len(lista) == 1:
        pass
    else:
        #print(lista[len(lista)-2])
        canvas.delete(lista[len(lista)-2])


def mostrar_articulo():

    art = articulo.get()
    if not art:
        messagebox.showinfo("ATENCION", 'Debe ingresar un articulo')
    else:
        dicionario = a.extraer()
        if not a.existencia(dicionario, art):
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
photo=PhotoImage(file='img.png')
canvas.create_image(0,70,image=photo,anchor=NW)
imagenbtn1= PhotoImage(file="lupa.png")
i1=imagenbtn1.subsample(4,4)
btn_buscar=Button(ventana,image=i1,command=mostrar_articulo).place(x=733,y=49)



mainloop()
