from tkinter import *  # Importa todos los módulos de tkinter / Imports all tkinter modules
from tkinter import messagebox  # Importa el módulo messagebox / Imports messagebox module
import random  # Importa módulo para números aleatorios / Imports module for random numbers

class Principal():  # Define la clase principal / Defines main class
    def __init__(self):  # Constructor de la clase / Class constructor
        self.ven = Tk()  # Crea la ventana principal / Creates main window
        self.ven.title('Programa 7 con ventanas place')  # Establece el título / Sets the title
        self.ven.geometry('550x250')  # Define el tamaño de la ventana / Defines window size
        self.a = 0  # Variable para primer número / Variable for first number
        self.b = 0  # Variable para segundo número / Variable for second number
        self.lista = []  # Lista para almacenar números / List to store numbers
        self.aux1 = 0  # Variable auxiliar para mayor / Auxiliary variable for maximum
        self.aux2 = 0  # Variable auxiliar para menor / Auxiliary variable for minimum
        self.cont = 0  # Contador para recorrer lista / Counter to traverse list
    
    def Inicio(self):  # Método para crear la interfaz / Method to create interface
        l1 = Label(self.ven,text="Programa 6")  # Etiqueta título / Title label
        l1.place(x=200,y=25)  # Posición absoluta con place / Absolute position with place
        l2 = Label(self.ven,text="Escribe un numero")  # Etiqueta para primer número / Label for first number
        l2.place(x=100,y=50)  # Posición absoluta con place / Absolute position with place
        Label(self.ven,text=" ").place(x=2,y=2)  # Espacio vacío / Empty space
        self.n1 = Entry(self.ven)  # Campo entrada primer número / Entry field first number
        self.n1.place(x=100,y=75)  # Posición absoluta con place / Absolute position with place
        l3 = Label(self.ven,text="Escribe otro numero")  # Etiqueta para segundo número / Label for second number
        l3.place(x=250,y=50)  # Posición absoluta con place / Absolute position with place
        Label(self.ven,text=" ").place(x=4,y=2)  # Espacio vacío / Empty space
        self.n2 = Entry(self.ven)  # Campo entrada segundo número / Entry field second number
        self.n2.place(x=250,y=75)  # Posición absoluta con place / Absolute position with place
        b1 = Button(self.ven,text="Agregar",command=self.agregar)  # Botón agregar números / Add numbers button
        b1.place(x=100,y=110)  # Posición absoluta con place / Absolute position with place
        b2 = Button(self.ven,text="Mayor",command=self.mayor)  # Botón encontrar mayor / Find maximum button
        b2.place(x=180,y=110)  # Posición absoluta con place / Absolute position with place
        b3 = Button(self.ven,text="Menor",command=self.menor)  # Botón encontrar menor / Find minimum button
        b3.place(x=260,y=110)  # Posición absoluta con place / Absolute position with place
        b4 = Button(self.ven,text="Salir",command=self.salir)  # Botón salir / Exit button
        b4.place(x=340,y=110)  # Posición absoluta con place / Absolute position with place
        self.listaElementos = Label(self.ven,text="[]")  # Etiqueta para mostrar lista / Label to show list
        self.listaElementos.place(x=150,y=180)  # Posición absoluta con place / Absolute position with place
        self.lisview = Listbox(self.ven, height=10, width=15, bg='grey', activestyle='dotbox', fg='black')  # Listbox para mostrar elementos / Listbox to show elements
        self.lisview.place(x=410,y=20)  # Posición absoluta con place / Absolute position with place
        self.ven.mainloop()  # Inicia el bucle principal / Starts main loop
    
    def salir(self):  # Método para cerrar la aplicación / Method to close application
        self.ven.destroy()  # Cierra la ventana / Closes window
    
    def agregar(self):  # Método para agregar números aleatorios a la lista / Method to add random numbers to list
        try:
            valor = random.randint(1,100)  # Genera número aleatorio entre 1-100 / Generates random number between 1-100
            self.lista.append(valor)  # Agrega a la lista / Adds to list
            self.lisview.insert(self.lisview.size()+1,valor)  # Inserta en Listbox / Inserts in Listbox
            print(self.lista)  # Imprime lista en consola / Prints list to console
            self.aux2 = self.lista[0]  # Inicializa variable para menor / Initializes variable for minimum
            self.listaElementos.config(text = f'{self.lista}')  # Actualiza etiqueta lista / Updates list label
            
        except ValueError:  # Captura error de conversión / Catches conversion error
            messagebox.showerror("Error","Agrega algun numero")  # Muestra mensaje de error / Shows error message
    
    def mayor(self):  # Método para encontrar el número mayor / Method to find maximum number
        if len(self.lista) > 0:  # Verifica si la lista no está vacía / Checks if list is not empty
            if self.aux1 < self.lista[self.cont]:  # Compara con elemento actual / Compares with current element
                self.aux1 = self.lista[self.cont]  # Actualiza el mayor / Updates maximum
            self.cont += 1  # Incrementa contador / Increments counter
            if len(self.lista)-1 < self.cont:  # Verifica si llegó al final / Checks if reached end
                print(f'El mayor es {self.aux1}')  # Imprime resultado / Prints result
                messagebox.showinfo('El mayor',self.aux1)  # Muestra mensaje informativo / Shows info message
                self.cont = 0  # Reinicia contador / Resets counter
            else:
                return self.mayor()  # Llama recursivamente / Calls recursively
        else:
            messagebox.showerror('Error','La lista esta vacia')  # Muestra error si lista vacía / Shows error if empty list
    
    def menor(self):  # Método para encontrar el número menor / Method to find minimum number
        if len(self.lista) > 0:  # Verifica si la lista no está vacía / Checks if list is not empty
            for i in self.lista:  # Itera sobre cada elemento / Iterates over each element
                if self.aux2 > i:  # Compara con elemento actual / Compares with current element
                    self.aux2 = i  # Actualiza el menor / Updates minimum
            print(f'El menor es {self.aux2}')  # Imprime resultado / Prints result
            messagebox.showinfo('El menor',self.aux2)  # Muestra mensaje informativo / Shows info message
        else:
            messagebox.showerror('Error','La lista esta vacia')  # Muestra error si lista vacía / Shows error if empty list

if __name__ == '__main__':
    app = Principal()  # Crea instancia de la clase / Creates class instance
    app.Inicio()  # Llama al método Inicio / Calls Inicio method