from tkinter import ttk
from tkinter import *
import math
import datetime

class Gonz:

    def __init__(self, screen):


        ancho = 400

        alto = 200 

    self.scr = screen

#Dimensiones de la ventana     
self.scr.geometry(str(ancho)+'x'+str(alto))

#titulo de la ventana
self.scr.title("Examen Final")

etiqueta = Label(self.scr, text= "BIENVENIDO", font="30")
etiqueta.grid(row=0, columnspan=7, sticky=W+E)

#entradas
#Nombre
Label(scr, text="Nombre:").grid(row=1, column=1, columnspan=2)
self.Name = Entry(scr)
self.focus()
self.Name.grid(row=1, column=3, columnspan=3, sticky=W+E)

#Apellido
Label(scr, text="Apellido:").grid(row=2, column=1, columnspan=2)
self.Apellid = Entry(scr)
self.Apellid.grid(row=2, column=3, columnspan=3, sticky=W+E)

#Dia
Label(scr, text="Día:").grid(row=3, column=1, columnspan=2)
self.Dia = Entry(scr)
self.Dia.grid(row=3, column=3, columnspan=3, sticky=W+E)

#Mes
Label(scr, text="Mes:").grid(row=4, column=1, columnspan=2)
self.Mes = Entry(scr)
self.Mes.grid(row=4, column=3, columnspan=3, sticky=W+E)
#Año
Año = Label(text="Año:").grid(row=5, column=1, columnspan=2)
self.Año = Entry(scr)
self.Año.grid(row=5, column=3, columnspan=3, sticky=W+E)

#Botones
Button(scr, text="Función 1", command = self.dec2bin).grid(row=6, column=1)
Button(scr, text="Función 2", command = self.living).grid(row=6, column=2)
Button(scr, text="Función 3", command = self.NumLetras).grid(row=6, column=3)
Button(scr, text="Función 4", command = self.VocCon).grid(row=6, column=4)
Button(scr, text="Función 5", command = self.turn).grid(row=6, column=5)

#Resultado
self.answer = Label(scr,text = '', fg = 'blue')
self.answer.grid(row=7,column=2, columnspan=3, sticky = W+E)

#Funcion 1
def dec2bin(self):
    dia=int(self.Dia.get())
    mes=int(self.Mes.get())
    año=int(self.Año.get())
    diabin=format(dia, '0b')
    mesbin=format(mes, '0b')
    añobin=format(año, '0b')

    self.answer['text'] = '{}/{}/{} en binario es {}/{}/{}'. format(dia,mes,año,diabin,mesbin,añobin)

#Funcion 2
def living(self):
    dia=int(self.Dia.get())
    mes=int(self.Mes.get())
    año=iny(self.Año.get())
    birthdate = datetime.datetime(dia, mes, año)
    today = datetime.datetime.now()
    diferencia = today - birthdate
    DiasVividos = diferencia.days

    self.answer['text'] = 'Usted nacio el {}/{}/{} y ha vivido {} dias'.format(dia,mes, año,DiasVividos)

#Funcion #3
def NumLetras(self):
    name=str(self.Name.get())
    apellid=str(self.Apellid.get())
    NumName=int(len(nombre))
    NumApellid=int(len(apellido))
    if NumName%2==0 and NumApellid %2==0:
        self.answer['text'] = '{}{} su nombre es par al igual que su apellido'.format(name, apellid)

    elif NumName%2==0 and NumApellid%2==1:
        self.answer['text']= '{}{} su nombre es par pero su apellido es impar'.format(name, apellid)

    elif NumName%2==1 and NumApellid%2==0:
        self.answer['text']= '{}{} su nombre es impar pero su apellido es par'.format(name, apellid)

    elif NumName%2==1 and NumApellid%2==1:
        self.answer['text']= '{}{} su nombre es impar al igual que su apellido'.format(name, apellid)

#funcion 4
def VocCon(self):
    name=str(self.Name.get())
    apellid=str(self.Apellid.get())
    count = 0

    for num in name:
        if num =='a' or num == 'e' or num == 'i' or num == 'o' or num == 'u' or num =='A' or num == 'E' or num == 'I' or num == 'O' or num == 'U':
            count += 1
    for num in apellid:
        if num =='a' or num == 'e' or num == 'i' or num == 'o' or num == 'u' or num =='A' or num == 'E' or num == 'I' or num == 'O' or num == 'U':        
            count += 1

    coun1=len(name)
    coun2=len(apellid)
    cons= coun1+coun2-count

    self.answer['texto']= '{}{} tiene {} vocales y {} consonantes'. format(Name,Apellid,count, cons)

#funcion 5
def turn(self):
    name=str(self.Name.get())
    apellid=str(self.Apellid.get())
    cadena_invertida =""
    cadena_invertida1=""
    for letter in name:
            cadena_invertida = letter + cadena_invertida
    for letter1 in apellid:
            cadena_invertida1 = letter1 + cadena_invertida1
        self.answer['text'] = '{} {} al revez {} {}'.format(name,apellid, cadena_invertida,cadena_invertida1)

#validacion
if __name__ == '__main__':
    
    #asignamos la propiedad de tkinter a la variable screen
    screen = Tk()
    
    #en la variable app guardamos la clase Desk y le enviamos como parametro la ventana 
    app = Gonz(screen)

screen.mainloop()