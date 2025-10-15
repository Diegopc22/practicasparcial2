from tkinter import *  # Importa todos los módulos de tkinter / Imports all tkinter modules
from tkinter import messagebox  # Importa el módulo messagebox / Imports messagebox module

class Ventana():  # Define la clase Ventana / Defines Ventana class
    def __init__(self):  # Constructor de la clase / Class constructor
        self.ven = Tk()  # Crea la ventana principal / Creates main window
        self.ven.title('Organizador de 3 calificaiones')  # Establece el título / Sets the title
        self.ven.geometry('600x300')  # Define el tamaño de la ventana / Defines window size
        self.inicio()  # Llama al método inicio / Calls inicio method
    
    def inicio(self):  # Método para crear la interfaz / Method to create interface
        self.lis = []  # Inicializa lista para datos del estudiante / Initializes list for student data
        labeln = Label(self.ven, text='Cual es tu nombre').pack()  # Etiqueta nombre y empaqueta / Name label and packs
        self.nom = Entry(self.ven)  # Campo entrada nombre / Name entry field
        self.nom.pack(pady=4)  # Empaqueta con espacio / Packs with spacing
        label1 = Label(self.ven, text='Ingresa una calificacion').pack()  # Etiqueta calificación 1 / Grade 1 label
        self.c1 = Entry(self.ven)  # Campo entrada calificación 1 / Grade 1 entry field
        self.c1.pack(pady=4)  # Empaqueta con espacio / Packs with spacing
        label2 = Label(self.ven,text='Ingresa otra calificacion').pack(pady=4)  # Etiqueta calificación 2 / Grade 2 label
        self.c2 = Entry(self.ven)  # Campo entrada calificación 2 / Grade 2 entry field
        self.c2.pack(pady=4)  # Empaqueta con espacio / Packs with spacing
        label3 = Label(self.ven,text='Ingresa otra calificacion').pack(pady=4)  # Etiqueta calificación 3 / Grade 3 label
        self.c3 = Entry(self.ven)  # Campo entrada calificación 3 / Grade 3 entry field
        self.c3.pack(pady=4)  # Empaqueta con espacio / Packs with spacing
        boton = Button(self.ven,text='Ordenar',command=self.ordenar).pack(pady=4)  # Botón ordenar / Sort button
        self.ven.mainloop()  # Inicia el bucle principal / Starts main loop
    
    def ordenar(self):  # Método para ordenar calificaciones / Method to sort grades
        try:
            nombre = self.nom.get()  # Obtiene nombre del estudiante / Gets student name
            c1 = float(self.c1.get())  # Obtiene y convierte calificación 1 / Gets and converts grade 1
            c2 = float(self.c2.get())  # Obtiene y convierte calificación 2 / Gets and converts grade 2
            c3 = float(self.c3.get())  # Obtiene y convierte calificación 3 / Gets and converts grade 3
            mas = max(c1,c2,c3)  # Encuentra la calificación máxima / Finds maximum grade
            mi = min(c1,c2,c3)  # Encuentra la calificación mínima / Finds minimum grade
            if mas > c1 and mi < c1:  # Verifica si c1 es la calificación media / Checks if c1 is middle grade
                self.lis = ([nombre, mas, c1, mi])  # Crea lista ordenada [nombre, mayor, medio, menor] / Creates sorted list [name, max, middle, min]
                messagebox.showinfo('Correcto','Datos guardados con éxito')  # Muestra mensaje de éxito / Shows success message
            elif mas > c2 and mi < c2:  # Verifica si c2 es la calificación media / Checks if c2 is middle grade
                self.lis = ([nombre, mas, c2, mi])  # Crea lista ordenada / Creates sorted list
                messagebox.showinfo('Correcto','Datos guardados con éxito')  # Muestra mensaje de éxito / Shows success message
            elif mas > c3 and mi < c3:  # Verifica si c3 es la calificación media / Checks if c3 is middle grade
                self.lis = ([nombre, mas, c3, mi])  # Crea lista ordenada / Creates sorted list
                messagebox.showinfo('Correcto','Datos guardados con éxito')  # Muestra mensaje de éxito / Shows success message
            lista.append(self.lis)  # Agrega a lista global / Adds to global list
            print(lista)  # Imprime lista global en consola / Prints global list to console
        except ValueError:  # Captura error de conversión / Catches conversion error
            messagebox.showerror('Error', 'Introduce valores')  # Muestra mensaje de error / Shows error message

lista = []  # Lista global para almacenar todos los estudiantes / Global list to store all students
if __name__ == '__main__':
    app = Ventana()  # Crea instancia de la clase Ventana / Creates instance of Ventana class