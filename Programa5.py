from tkinter import *  # Importa todos los módulos de tkinter / Imports all tkinter modules
from tkinter import messagebox  # Importa el módulo messagebox / Imports messagebox module

class Principal():  # Define la clase principal / Defines main class
    def __init__(self):  # Constructor de la clase / Class constructor
        self.ven = Tk()  # Crea la ventana principal / Creates main window
        self.ven.title('Programa 5 con ventanas')  # Establece el título / Sets the title
        self.ven.geometry('450x250')  # Define el tamaño de la ventana / Defines window size
        self.lista = []  # Inicializa lista vacía para almacenar promedios / Initializes empty list to store averages
        self.inicio()  # Llama al método inicio / Calls inicio method
    
    def sumar(self):  # Método para sumar elementos de la lista / Method to sum list elements
        s = 0  # Inicializa contador de suma / Initializes sum counter
        for i in self.lista:  # Itera sobre cada elemento de la lista / Iterates over each list element
            s += i  # Suma el elemento actual al total / Adds current element to total
        return s  # Retorna la suma total / Returns total sum
    
    def promediar(self):  # Método para calcular promedio / Method to calculate average
        try:
            a = float(self.n1.get())  # Obtiene y convierte primer número / Gets and converts first number
            b = float(self.n2.get())  # Obtiene y convierte segundo número / Gets and converts second number
            c = float(self.n3.get())  # Obtiene y convierte tercer número / Gets and converts third number
            d = float(self.n4.get())  # Obtiene y convierte cuarto número / Gets and converts fourth number
            promedio = (a+b+c+d) / 4  # Calcula el promedio / Calculates average
            self.l6.config(text = str(promedio))  # Actualiza etiqueta con promedio / Updates label with average
            self.lista.append(promedio)  # Agrega promedio a la lista / Adds average to list
            self.l7.config(text = str(self.lista))  # Actualiza etiqueta con lista / Updates label with list
            self.n1.delete(0,END)  # Limpia campo de entrada 1 / Clears entry field 1
            self.n2.delete(0,END)  # Limpia campo de entrada 2 / Clears entry field 2
            self.n3.delete(0,END)  # Limpia campo de entrada 3 / Clears entry field 3
            self.n4.delete(0,END)  # Limpia campo de entrada 4 / Clears entry field 4
            suma = self.sumar()  # Calcula suma total de promedios / Calculates total sum of averages
            p = suma / len(self.lista)  # Calcula promedio general / Calculates general average
            self.l8.config(text = f'Promedio general: {str(p)}')  # Actualiza promedio general / Updates general average
        except ValueError:  # Captura error de conversión / Catches conversion error
            messagebox.showerror('Error', 'Algun dato no es un numero')  # Muestra mensaje de error / Shows error message
            self.n1.delete(0,END)  # Limpia campo de entrada 1 / Clears entry field 1
            self.n2.delete(0,END)  # Limpia campo de entrada 2 / Clears entry field 2
            self.n3.delete(0,END)  # Limpia campo de entrada 3 / Clears entry field 3
            self.n4.delete(0,END)  # Limpia campo de entrada 4 / Clears entry field 4
    
    def salir(self):  # Método para cerrar la aplicación / Method to close application
        self.ven.destroy()  # Cierra la ventana / Closes window
    
    def inicio(self):  # Método para crear la interfaz / Method to create interface
        l1 = Label(self.ven,text='Escribe un numero').place(y=10,x=20)  # Etiqueta y posición / Label and position
        l2 = Label(self.ven,text='Escribe un numero').place(y=50,x=20)  # Etiqueta y posición / Label and position
        self.n1 = Entry(self.ven)  # Campo de entrada para número 1 / Entry field for number 1
        self.n1.place(y=10,x=130)  # Posición del campo 1 / Position of field 1
        self.n2 = Entry(self.ven)  # Campo de entrada para número 2 / Entry field for number 2
        self.n2.place(y=50,x=130)  # Posición del campo 2 / Position of field 2
        l3 = Label(self.ven,text='Escribe un numero').place(y=90,x=20)  # Etiqueta y posición / Label and position
        l4 = Label(self.ven,text='Escribe un numero').place(y=130,x=20)  # Etiqueta y posición / Label and position
        self.n3 = Entry(self.ven)  # Campo de entrada para número 3 / Entry field for number 3
        self.n3.place(y=90,x=130)  # Posición del campo 3 / Position of field 3
        self.n4 = Entry(self.ven)  # Campo de entrada para número 4 / Entry field for number 4
        self.n4.place(y=130,x=130)  # Posición del campo 4 / Position of field 4
        l5 = Label(self.ven,text='Promedio').place(y=150,x=130)  # Etiqueta promedio / Average label
        self.l6 = Label(self.ven,text='0.0')  # Etiqueta para mostrar promedio actual / Label to show current average
        self.l6.place(y=150,x=200)  # Posición etiqueta promedio / Average label position
        b1 = Button(self.ven,text='Promedio',command=self.promediar).place(y=50,x=300)  # Botón calcular promedio / Calculate average button
        b2 = Button(self.ven,text='Salir',command=self.salir).place(y=90,x=300)  # Botón salir / Exit button
        self.l7 = Label(self.ven,text='[]')  # Etiqueta para mostrar lista de promedios / Label to show averages list
        self.l7.place(y=170,x=200)  # Posición etiqueta lista / List label position
        self.l8 = Label(self.ven,text='Promedio general: 0.0')  # Etiqueta promedio general / General average label
        self.l8.place(y=190,x=130)  # Posición promedio general / General average position
        self.ven.mainloop()  # Inicia el bucle principal / Starts main loop

if __name__ == '__main__':
    app = Principal()  # Crea instancia de la clase Principal / Creates instance of Principal class