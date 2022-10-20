from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox
import tkinter
import random
import time

ventana = Tk()
ventana.geometry("1050x600")
ventana.config(bg="#6F1C0A")
ventana.title("SOPA DE LETRAS")
ventana.iconbitmap("unnamed.png")

alfabeto=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']

ven = Frame(ventana,bg="#6F1C0A", width=20, padx=100)
ven.pack(side="top")

img = tkinter.PhotoImage(file="unnamed.png")# ABRIR CARPETA COMPLETA NO EL ARCHIVO 
portada = tkinter.Label(ventana,image=img,background="#FFFFFF")
portada.pack()

marco = Frame(ventana,padx=8,pady=8,bg="#076403")
cuadro = Frame(ventana, width=50, height=50, padx=8,pady=8,bg="#0B0B0B", bd=5)

fontStyle = tkFont.Font(size=10)

entrada = Entry(cuadro,font=fontStyle,state=DISABLED, bd=6)

def Comparar():
    respuestas = ["JUGAR","COCINAR","HACER","CORRER","VIAJAR","ESTUDIAR","CONSEGUIR","LINDO","FEO","ALTO","OSCURO","ORGULLOSO","MALO"]
    
#                               ///P A L A B R A S\\\
    fila = 0
    for i in respuestas:
        if entrada.get() == i:
            texto = Label(cuadro,text=i,font=fontStyle)
            texto.grid(row=fila,column=0,sticky=(W),padx=5,pady=2)
            fila = fila + 1
        else:
            fila = fila + 1

aceptar = Button(cuadro,text="aceptar",font=fontStyle,padx=2,pady=2,command=Comparar,state=DISABLED)

minute=StringVar()

second=StringVar()

fin=BooleanVar()

fin.set(False)

minute.set("0")

second.set("0")

tiempo = Button(cuadro,text="Tiempo",font=fontStyle,command= lambda : fin.set(True))

minuteEntry= Entry(cuadro,width=3, font=fontStyle,textvariable=minute,state=DISABLED)

secondEntry= Entry(cuadro,width=3, font=fontStyle,textvariable=second,state=DISABLED)

def clock():
    comenzar.config(state=DISABLED)
    tiempo.grid(row=29,column=3,rowspan=32,sticky=(N,S,W,E))
    aceptar.config(state=NORMAL)
    entrada.config(state=NORMAL)

    minute.set("3")# M I N U T O S
    second.set("20")# S E G U N D O S

    temp = int(minute.get()) * 60 + int(second.get())

    while temp > -1:
        mins,secs = divmod(temp,60)

        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))

        minuteEntry.update()
        secondEntry.update()
        time.sleep(1)

        if (temp == 0):
            messagebox.showinfo("","Tiempo")
            entrada.config(state=DISABLED)
            aceptar.config(state=DISABLED)
        elif fin.get() == True:

            messagebox.showinfo("","Tiempo")
            entrada.config(state=DISABLED)
            aceptar.config(state=DISABLED)
            break
         
        temp -= 1


comenzar = Button(cuadro,text="COMENZAR",font=fontStyle,padx=5,pady=5,command=clock)

def Wel():
    portada.pack()

    marco.forget()
    cuadro.forget()

def Palabra(padre,eje,point,p = ""):
    if padre == marco:
        if eje == "y":
            for i,z in enumerate(p):
                btn = Label(padre,text=z,padx=5,pady=5,font=fontStyle,relief="solid",bd=1)
                btn.grid(row=i, column=point, sticky=N+S+E+W)
        elif eje == "x":
            for i,z in enumerate(p):
                btn = Label(padre,text=z,padx=5,pady=5,font=fontStyle,relief="solid",bd=1)
                btn.grid(row=point, column=i, sticky=N+S+E+W)


def Sopa():
    cuadro.pack(side="left",padx=10)
    marco.pack(side="left",padx=10)
    entrada.grid(row=30,column=0,columnspan=2,padx=6,sticky=(N,S,W,E))
    aceptar.grid(row=30,column=2,sticky=(N,S,W,E))
    minuteEntry.grid(row=29,column=0)
    secondEntry.grid(row=29,column=1)
    comenzar.grid(row=29,column=2,sticky=(N,S,W,E))

#                       **** T E M A ****

    Label(cuadro,text="ADJETIVOS Y VERBOS",font=fontStyle).grid(row=31,column=0,columnspan=3,sticky=(W,E),pady=4,padx=6)
    Label(cuadro,text="10 PALABRAS",font=fontStyle).grid(row=32,column=0,columnspan=3,sticky=(W,E),pady=4,padx=6)

#                       **** T E M A ****

    for rows in range(14):

        for cols in range(14):
            boton = Label(marco,text=alfabeto[random.randint(0,25)],font=fontStyle,padx=5,pady=5,relief="solid",bd=1)
            boton.grid(row=rows, column=cols, sticky=N+S+E+W)

#                               **** P A L A B R A S ****
    # EMPUJAMOS PALABRAS AL CENTRO
    Palabra(marco,"y",10,p = "AÑSLSLWDKJUGAR")
    Palabra(marco,"y",7,p = "AÑSLSLWCOCINAR")
    Palabra(marco,"y",13,p = "AÑSCOLMHACER")
    Palabra(marco,"y",11,p = "ESCAMASCCORRER")
    Palabra(marco,"y",5,p = "ASKMDZIVIAJAR")
    Palabra(marco,"y",4,p = "ASIESTUDIAR")
    Palabra(marco,"y",2,p = "ZVAFCONSEGUIR")
    Palabra(marco,"y",12,p = "ÑMAZPLINDO")

    Palabra(marco,"x",0,p = "JVHBRANQUFEO")
    Palabra(marco,"x",2,p = "PEALTO")
    Palabra(marco,"x",12,p = "SMALO")
    
#                               **** P A L A B R A S
    portada.forget()

inicio = Button(ven,text="    INICIAR    ",padx=2,pady=2,font=20, bd= 4, command=Wel).pack(pady=8,fill="x", expand=True)
desafio1 = Button(ven,text="    JUGAR    ",padx=2,pady=2,font=20, bd= 4, command=Sopa).pack(pady=8,fill="x", expand=True)

ventana.mainloop()