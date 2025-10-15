from tkinter import *  # Importa todos los módulos de tkinter / Imports all tkinter modules
from tkinter import messagebox  # Importa el módulo messagebox / Imports messagebox module

class Principal():  # Define la clase principal / Defines main class
    def __init__(self):  # Constructor de la clase / Class constructor
        self.ven = Tk()  # Crea la ventana principal / Creates main window
        self.ven.title('Programa 6 con ventanas GRID')  # Establece el título / Sets the title
        self.ven.geometry('450x350')  # Define el tamaño de la ventana / Defines window size
        self.a = 0  # Variable para primer número / Variable for first number
        self.b = 0  # Variable para segundo número / Variable for second number
        self.lista = []  # Lista para almacenar números / List to store numbers
        self.aux1 = 0  # Variable auxiliar para mayor / Auxiliary variable for maximum
        self.aux2 = 0  # Variable auxiliar para menor / Auxiliary variable for minimum
        self.cont = 0  # Contador para recorrer lista / Counter to traverse list
    
    def Inicio(self):  # Método para crear la interfaz / Method to create interface
        l1 = Label(self.ven,text="Programa 6")  # Etiqueta título / Title label
        l1.grid(row=1,column=2)  # Posición en grid / Grid position
        l2 = Label(self.ven,text="Escribe un numero")  # Etiqueta para primer número / Label for first number
        l2.grid(row=3,column=1,padx=5,pady=5)  # Posición con padding / Position with padding
        Label(self.ven,text=" ").grid(row=2,column=2)  # Espacio vacío / Empty space
        self.n1 = Entry(self.ven)  # Campo entrada primer número / Entry field first number
        self.n1.grid(row=3,column=2)  # Posición en grid / Grid position
        l3 = Label(self.ven,text="Escribe otro numero")  # Etiqueta para segundo número / Label for second number
        l3.grid(row=5,column=1,padx=5,pady=5)  # Posición con padding / Position with padding
        Label(self.ven,text=" ").grid(row=4,column=2)  # Espacio vacío / Empty space
        self.n2 = Entry(self.ven)  # Campo entrada segundo número / Entry field second number
        self.n2.grid(row=5,column=2)  # Posición en grid / Grid position
        b1 = Button(self.ven,text="Agregar",command=self.agregar)  # Botón agregar números / Add numbers button
        b1.grid(row=6,column=1,padx=10)  # Posición con padding / Position with padding
        b2 = Button(self.ven,text="Mayor",command=self.mayor)  # Botón encontrar mayor / Find maximum button
        b2.grid(row=6,column=2)  # Posición en grid / Grid position
        b3 = Button(self.ven,text="Menor",command=self.menor)  # Botón encontrar menor / Find minimum button
        b3.grid(row=6,column=3,padx=10)  # Posición con padding / Position with padding
        b4 = Button(self.ven,text="Salir",command=self.salir)  # Botón salir / Exit button
        b4.grid(row=6,column=4,padx=25)  # Posición con padding / Position with padding
        self.listaElementos = Label(self.ven,text="[]")  # Etiqueta para mostrar lista / Label to show list
        self.listaElementos.grid(row=8,column=2,padx=25)  # Posición con padding / Position with padding
        self.lisview = Listbox(self.ven, height=10, width=15, bg='grey', activestyle='dotbox', fg='black')  # Listbox para mostrar elementos / Listbox to show elements
        self.lisview.grid(row=2,column=4)  # Posición en grid / Grid position
        self.ven.mainloop()  # Inicia el bucle principal / Starts main loop
    
    def salir(self):  # Método para cerrar la aplicación / Method to close application
        self.ven.destroy()  # Cierra la ventana / Closes window
    
    def agregar(self):  # Método para agregar números a la lista / Method to add numbers to list
        try:
            self.a = int(self.n1.get())  # Obtiene y convierte primer número / Gets and converts first number
            self.lista.append(self.a)  # Agrega a la lista / Adds to list
            self.lisview.insert(self.lisview.size()+1,self.a)  # Inserta en Listbox / Inserts in Listbox
            self.n1.delete(0,END)  # Limpia campo de entrada / Clears entry field
            self.b = int(self.n2.get())  # Obtiene y convierte segundo número / Gets and converts second number
            self.lisview.insert(self.lisview.size()+1,self.b)  # Inserta en Listbox / Inserts in Listbox
            self.lista.append(self.b)  # Agrega a la lista / Adds to list
            self.n2.delete(0,END)  # Limpia campo de entrada / Clears entry field
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