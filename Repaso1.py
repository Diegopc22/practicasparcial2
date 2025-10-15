from tkinter import *  # Importa todos los módulos de tkinter / Imports all tkinter modules
from tkinter import messagebox  # Importa el módulo messagebox / Imports messagebox module
from ValidarRepaso import Validar  # Importa la clase Validar del módulo ValidarRepaso / Imports Validar class from ValidarRepaso module

class Principal():  # Define la clase principal / Defines main class
    def __init__(self):  # Constructor de la clase / Class constructor
        self.ventana = Tk()  # Crea la ventana principal / Creates main window
        self.ventana.geometry("400x200")  # Define el tamaño de la ventana / Defines window size
        self.lista = []  # Lista para almacenar datos / List to store data
        self.valid = Validar()  # Crea instancia de la clase Validar / Creates instance of Validar class
        
    def inicio(self):  # Método para crear la interfaz / Method to create interface
        Label(self.ventana, text="Programa de python con TKInter").place(x=100, y=20)  # Etiqueta título con posición / Title label with position
        Label(self.ventana, text="Escribe un dato").place(x=50, y=50)  # Etiqueta instrucción / Instruction label
        self.dato = Entry(self.ventana)  # Campo de entrada para datos / Entry field for data
        self.dato.place(x=150, y=50, width=150)  # Posición y ancho del campo / Field position and width
        Button(self.ventana, text="Validar", command=self.ValidarDatos).place(x=150, y=90, width=150)  # Botón validar / Validate button
        self.mostrar = Label(self.ventana, text="ejemplo")  # Etiqueta para mostrar lista / Label to show list
        self.mostrar.place(x=20, y=150)  # Posición etiqueta mostrar / Show label position
        self.ventana.mainloop()  # Inicia el bucle principal / Starts main loop

    def ValidarDatos(self):  # Método para validar datos ingresados / Method to validate entered data
        val = self.dato.get()  # Obtiene el texto del campo de entrada / Gets text from entry field
        if val != "":  # Verifica que no esté vacío / Checks if not empty
            self.Revisar(val)  # Llama al método Revisar / Calls Revisar method
            self.lista.append(val)  # Agrega el valor a la lista / Adds value to list
            self.dato.delete(0,END)  # Limpia el campo de entrada / Clears entry field
            self.mostrar.config(text=f'{self.lista}')  # Actualiza la etiqueta con la lista / Updates label with list
            respuesta = self.valid.ValidarConString(val)  # Llama método de validación / Calls validation method
            messagebox.showinfo("Validar Datos", f'El dato es {respuesta}')  # Muestra resultado / Shows result
        else:
            messagebox.showerror("Error","Caja de texto esta vacia")  # Muestra error si está vacío / Shows error if empty

    def Revisar(self, v):  # Método auxiliar para revisar datos / Auxiliary method to check data
        print(v)  # Imprime el valor en consola / Prints value to console

if __name__=='__main__':
    app = Principal()  # Crea instancia de la clase Principal / Creates instance of Principal class
    app.inicio()  # Llama al método inicio / Calls inicio method