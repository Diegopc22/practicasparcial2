from tkinter import *  # Importa todos los módulos de tkinter / Imports all tkinter modules
from tkinter import messagebox  # Importa el módulo messagebox / Imports messagebox module

def Ventana():
    def revisar():  # Función para verificar credenciales / Function to check credentials
        try:
            u = str(us.get())  # Obtiene usuario del campo / Gets username from field
            p = str(pas.get())  # Obtiene contraseña del campo / Gets password from field
            if u == 'admin' and p == '12345':  # Verifica credenciales / Checks credentials
                messagebox.showinfo('Validacion','Usuario y Contraseña correctos')  # Mensaje de éxito / Success message
            else:
                messagebox.showerror('Error', 'Usuario y/o contraseña incorrectos')  # Mensaje de error / Error message
        except ValueError:
            messagebox.showerror('Error', 'Introduce datos')  # Error si no hay datos / Error if no data
    ven = Tk()  # Crea ventana principal / Creates main window
    ven.title('Programa 1 con ventanas')  # Establece título / Sets title
    ven.geometry('400x200')  # Define tamaño ventana / Defines window size
    label = Label(ven, text='Usuario')  # Crea etiqueta usuario / Creates username label
    label.pack(pady=4)  # Empaqueta con espacio / Packs with spacing
    us = Entry(ven)  # Crea campo entrada usuario / Creates username entry field
    us.pack(pady=4)  # Empaqueta con espacio / Packs with spacing
    Label(ven, text='Password').pack(pady=4)  # Etiqueta contraseña y empaqueta / Password label and packs
    pas = Entry(ven)  # Crea campo entrada contraseña / Creates password entry field
    pas.pack(pady=4)  # Empaqueta con espacio / Packs with spacing
    boton = Button(ven, text='Aceptar',command=revisar).pack(pady=4)  # Botón que ejecuta revisar / Button that runs check
    ven.mainloop()  # Inicia bucle principal / Starts main loop

if __name__ == '__main__':
    Ventana()  # Ejecuta la función Ventana / Runs Ventana function