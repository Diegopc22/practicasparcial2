from tkinter import *  # Importa todos los módulos de tkinter / Imports all tkinter modules
from tkinter import messagebox  # Importa el módulo messagebox / Imports messagebox module

class Ventana():  # Define la clase Ventana / Defines Ventana class
    def __init__(self):  # Constructor de la clase / Class constructor
        self.ven = Tk()  # Crea la ventana principal / Creates main window
        self.ven.title('Organizador de 3 calificaiones')  # Establece el título / Sets the title
        self.ven.geometry('700x350')  # Define el tamaño de la ventana / Defines window size
        self.inicio()  # Llama al método inicio / Calls inicio method
    
    def inicio(self):  # Método para crear la interfaz / Method to create interface
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
            self.lista1 = []  # Lista temporal para datos del estudiante / Temporary list for student data
            nom = self.nom.get()  # Obtiene nombre del estudiante / Gets student name
            c1 = int(self.c1.get())  # Obtiene y convierte calificación 1 / Gets and converts grade 1
            c2 = int(self.c2.get())  # Obtiene y convierte calificación 2 / Gets and converts grade 2
            c3 = int(self.c3.get())  # Obtiene y convierte calificación 3 / Gets and converts grade 3
            if(c1 > c2):  # Compara calificación 1 y 2 / Compares grade 1 and 2
                if(c1 > c3):  # Verifica si calificación 1 es la mayor / Checks if grade 1 is maximum
                    print(f'es mayor {c1}')  # Imprime mayor / Prints maximum
                    self.lista1.append(nom)  # Agrega nombre a lista / Adds name to list
                    self.lista1.append(c1)  # Agrega calificación mayor / Adds maximum grade
                    if(c2 > c3):  # Compara las dos calificaciones restantes / Compares remaining two grades
                        print(f'El del medio es {c2}')  # Imprime medio / Prints middle
                        print(f'El menor es {c3}')  # Imprime menor / Prints minimum
                        self.lista1.append(c2)  # Agrega calificación media / Adds middle grade
                        self.lista1.append(c3)  # Agrega calificación menor / Adds minimum grade
                        lista2.append(self.lista1)  # Agrega a lista global / Adds to global list
                        print(lista2)  # Imprime lista global / Prints global list
                    else:
                        print(f'El del medio es {c3}')  # Imprime medio / Prints middle
                        print(f'El menor es {c2}')  # Imprime menor / Prints minimum
                        self.lista1.append(c3)  # Agrega calificación media / Adds middle grade
                        self.lista1.append(c2)  # Agrega calificación menor / Adds minimum grade
                        lista2.append(self.lista1)  # Agrega a lista global / Adds to global list
                        print(lista2)  # Imprime lista global / Prints global list
                else:
                    print(f'El mayor es {c3}')  # Imprime mayor / Prints maximum
                    print(f'El medio es {c1}')  # Imprime medio / Prints middle
                    print(f'El menor es {c2}')  # Imprime menor / Prints minimum
                    self.lista1.append(nom)  # Agrega nombre a lista / Adds name to list
                    self.lista1.append(c3)  # Agrega calificación mayor / Adds maximum grade
                    self.lista1.append(c1)  # Agrega calificación media / Adds middle grade
                    self.lista1.append(c2)  # Agrega calificación menor / Adds minimum grade
                    lista2.append(self.lista1)  # Agrega a lista global / Adds to global list
                    print(lista2)  # Imprime lista global / Prints global list
            else:
                if(c2 > c3):  # Verifica si calificación 2 es la mayor / Checks if grade 2 is maximum
                    print(f'El mayor es {c2}')  # Imprime mayor / Prints maximum
                    self.lista1.append(nom)  # Agrega nombre a lista / Adds name to list
                    self.lista1.append(c2)  # Agrega calificación mayor / Adds maximum grade
                    if(c1 > c3):  # Compara las dos calificaciones restantes / Compares remaining two grades
                        print(f'El del medio es {c1}')  # Imprime medio / Prints middle
                        print(f'El menor es {c3}')  # Imprime menor / Prints minimum
                        self.lista1.append(c1)  # Agrega calificación media / Adds middle grade
                        self.lista1.append(c3)  # Agrega calificación menor / Adds minimum grade
                        lista2.append(self.lista1)  # Agrega a lista global / Adds to global list
                        print(lista2)  # Imprime lista global / Prints global list
                    else:
                        print(f'El del medio es {c3}')  # Imprime medio / Prints middle
                        print(f'El menor es {c1}')  # Imprime menor / Prints minimum
                        self.lista1.append(c3)  # Agrega calificación media / Adds middle grade
                        self.lista1.append(c1)  # Agrega calificación menor / Adds minimum grade
                        lista2.append(self.lista1)  # Agrega a lista global / Adds to global list
                        print(lista2)  # Imprime lista global / Prints global list
                else:
                    print(f'El mayor es {c3}')  # Imprime mayor / Prints maximum
                    print(f'El medio es {c2}')  # Imprime medio / Prints middle
                    print(f'El menor es {c1}')  # Imprime menor / Prints minimum
                    self.lista1.append(nom)  # Agrega nombre a lista / Adds name to list
                    self.lista1.append(c3)  # Agrega calificación mayor / Adds maximum grade
                    self.lista1.append(c2)  # Agrega calificación media / Adds middle grade
                    self.lista1.append(c1)  # Agrega calificación menor / Adds minimum grade
                    lista2.append(self.lista1)  # Agrega a lista global / Adds to global list
                    print(lista2)  # Imprime lista global / Prints global list
        except ValueError:  # Captura error de conversión / Catches conversion error
            messagebox.showerror('Error', 'Introduce valores')  # Muestra mensaje de error / Shows error message

lista2 = []  # Lista global para almacenar todos los estudiantes / Global list to store all students
if __name__ == '__main__':
    app = Ventana()  # Crea instancia de la clase Ventana / Creates instance of Ventana class