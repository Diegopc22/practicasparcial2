from tkinter import *  # Importa todos los módulos de tkinter / Imports all tkinter modules
from tkinter import messagebox  # Importa el módulo messagebox / Imports messagebox module

class Ventana():  # Define una clase para la ventana / Defines a class for the window
    def __init__(self):  # Constructor de la clase / Class constructor
        self.ven = Tk()  # Crea la ventana principal / Creates main window
        self.ven.title('Programa 1 con ventanas')  # Establece el título / Sets the title
        self.ven.geometry('400x200')  # Define el tamaño de la ventana / Defines window size
        self.inicio()  # Llama al método inicio / Calls inicio method
    
    def inicio(self):  # Método para crear la interfaz / Method to create interface
        label = Label(self.ven, text='Usuario').pack()  # Crea y empaqueta etiqueta usuario / Creates and packs username label
        self.us = Entry(self.ven)  # Crea campo de entrada para usuario / Creates username entry field
        self.us.pack(pady=4)  # Empaqueta el campo usuario con espacio / Packs username field with spacing
        Label(self.ven, text='Password').pack(pady=4)  # Crea y empaqueta etiqueta contraseña / Creates and packs password label
        self.pas = Entry(self.ven)  # Crea campo de entrada para contraseña / Creates password entry field
        self.pas.pack(pady=4)  # Empaqueta el campo contraseña con espacio / Packs password field with spacing
        boton = Button(self.ven, text='Aceptar',command=self.revisar).pack(pady=4)  # Crea y empaqueta botón / Creates and packs button
        self.ven.mainloop()  # Inicia el bucle principal / Starts main loop
    
    def revisar(self):  # Método para verificar credenciales / Method to check credentials
        try:
            u = str(self.us.get())  # Obtiene el texto del campo usuario / Gets text from username field
            p = str(self.pas.get())  # Obtiene el texto del campo contraseña / Gets text from password field
            if u == 'admin' and p == '12345':  # Verifica las credenciales / Checks credentials
                messagebox.showinfo('Validacion','Usuario y Contraseña correctos')  # Mensaje de éxito / Success message
            else:
                messagebox.showerror('Error', 'Usuario y/o contraseña incorrectos')  # Mensaje de error / Error message
        except ValueError:
            messagebox.showerror('Error', 'Introduce datos')  # Error si no hay datos válidos / Error if no valid data
    
    
if __name__ == '__main__':
    app = Ventana()  # Crea una instancia de la clase Ventana / Creates an instance of Ventana class