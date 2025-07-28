import tkinter
def probar ():
    try:
        usuario = int(entry.get())
        if usuario % 2 == 0:
            lbl.config(text="Par")
        else:
            lbl.config(text="Impar")
    except ValueError:
        lbl.config(text="Por favor, ingresa un número válido.")


def limpiar():
    lbl.config(text="")
    entry.delete(0,'end')


   

    
#####################################
ventana = tkinter.Tk()
ventana.geometry("500x200")
ventana.title("Par o impar")

lbltitle=tkinter.Label(ventana,text="Par o impar", fg="red",font="300")
lbltitle.pack()

entry=tkinter.Entry(ventana)
entry.pack()

lbl=tkinter.Label(ventana,text="", fg="blue",font="300")
lbl.pack()

button=tkinter.Button(ventana,text="Par o impar", command= probar )
button.pack()
button=tkinter.Button(ventana,text="limpiar", command= limpiar )
button.pack()


ventana.mainloop()