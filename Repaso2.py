from tkinter import *
from tkinter import messagebox
from ValidacionRepaso2 import Validacion

class Ventana():
    def __init__(self):
        self.ven = Tk()
        self.ven.title('Repaso 2')
        self.ven.geometry('600x250')
        self.valida = Validacion()
        self.lista = []
        self.b1 = False

    def Inicio(self):
        Label(self.ven, text='Minusculas').place(x=10, y=10)
        self.c1 = Entry(self.ven)
        self.c1.place(x=10, y=35)

        Label(self.ven, text='Mayusculas').place(x=150, y=10)
        self.c2 = Entry(self.ven)
        self.c2.place(x=150, y=35)

        Label(self.ven, text='Numeros').place(x=290, y=10)
        self.c3 = Entry(self.ven)
        self.c3.place(x=290, y=35)

        Label(self.ven,text='Datos ingresados en la lista').place(x=140,y=100)
        self.lis = Label(self.ven,text=f'{len(self.lista)}')
        self.lis.place(x=200,y=130)

        Button(self.ven, text='Validacion', command=self.validacion).place(x=110, y=70)
        Button(self.ven, text='Agregar', command=self.agregar).place(x=255, y=70)

        self.lisview = Listbox(self.ven, height=10, width=15, bg='grey', activestyle='dotbox', fg='black')#Hace de forma visual la lista
        self.lisview.place(x=450,y=35)

        self.ven.mainloop()
    
    def validacion(self):
        val1 = self.c1.get()
        val2 = self.c2.get()
        val3 = self.c3.get()

        if val1 != "" and val2 != "" and val3 != "":
            if self.valida.ValidarMinus(val1):
                if self.valida.ValidarMayus(val2):
                    if self.valida.ValidarNumeros(val3):
                        messagebox.showinfo("Validación", "Todas las cajas son correctas")
                        self.c1.delete(0, END)
                        self.c2.delete(0, END)
                        self.c3.delete(0, END)
                        self.cadena = val1+val2+val3
                        print(self.cadena)
                        self.b1 = True
                    else:
                        messagebox.showerror("Error", "Casilla 3 debe tener solo números")
                        self.c3.delete(0, END)
                else:
                    messagebox.showerror("Error", "Casilla 2 debe tener solo mayúsculas")
                    self.c2.delete(0, END)
            else:
                messagebox.showerror("Error", "Casilla 1 debe tener solo minúsculas")
                self.c1.delete(0, END)
        else:
            messagebox.showerror("Error", "Todas las cajas deben estar llenas")

    def agregar(self):
        if self.b1:
            self.lista.append(self.cadena)
            self.lisview.insert(self.lisview.size()+1,self.cadena) #Agrega el elemento a la lista
            self.lis.config(text=f'{len(self.lista)}') #Esto actualiza el contador de la lista 
            self.b1 = False


if __name__ == '__main__':
    app = Ventana()
    app.Inicio()
