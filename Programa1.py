# Introduccion a la recurcividad, como una funcion se llama asi misma dentro de la misma.
# Introduction to recursion, how a function calls itself within itself.

def inicio(num):
    #global num  # (Comentado) Se usaría si quisiéramos modificar la variable global 'num' / Would be used if we wanted to modify the global variable 'num'
    a = int(input('Escribe una calificacion \n'))  # Pide al usuario ingresar una calificación / Asks the user to enter a grade
    num += 1  # Incrementa el contador en 1 cada vez que se llama la función / Increases the counter by 1 each time the function is called
    lista.append(a)  # Agrega la calificación ingresada a la lista / Adds the entered grade to the list
    if num >= 5:  # Condición base: cuando se han ingresado 5 calificaciones / Base condition: when 5 grades have been entered
        print(lista)  # Muestra todas las calificaciones guardadas / Displays all stored grades
    else:
        #return inicio(num)  # (Comentado) Podría usarse para devolver el resultado de la llamada recursiva / Could be used to return the result of the recursive call
        inicio(num)  # Llamada recursiva: la función se llama a sí misma / Recursive call: the function calls itself


lista = []  # Lista vacía donde se almacenarán las calificaciones / Empty list where grades will be stored
global num  # Declaración de variable global 'num' / Declaration of global variable 'num'
num = 0  # Inicializa el contador en 0 / Initializes the counter at 0
if __name__ == '__main__':  # Verifica si el archivo se ejecuta directamente / Checks if the file is being run directly
    inicio(num)  # Llama a la función 'inicio' para comenzar el proceso / Calls the 'inicio' function to start the process
