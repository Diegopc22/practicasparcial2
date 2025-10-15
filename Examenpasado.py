def inicio():
    lista1 = []  # Lista vacía para guardar los datos del usuario / Empty list to store user's data
    nom = input('Cual es tu nombre')  # Solicita el nombre del usuario / Asks for the user's name
    c1 = int(input('Ingresa una calificacion'))  # Pide la primera calificación / Asks for the first grade
    c2 = int(input('Ingresa una calificacion'))  # Pide la segunda calificación / Asks for the second grade
    c3 = int(input('Ingresa una calificacion'))  # Pide la tercera calificación / Asks for the third grade
    
    mayor = max(c1,c2,c3)  # Encuentra la calificación más alta / Finds the highest grade
    menor = min(c1,c2,c3)  # Encuentra la calificación más baja / Finds the lowest grade
    
lista2 = []  # Lista vacía para guardar múltiples registros / Empty list to store multiple records
if __name__ == '__main__':  # Comprueba si el programa se ejecuta directamente / Checks if the program runs directly
    while(True):  # Bucle infinito hasta que el usuario decida salir / Infinite loop until user decides to exit
        inicio()  # Llama a la función inicio() / Calls the inicio() function
        a = input('Quieres añadir otro registro s/n')  # Pregunta si desea añadir otro registro / Asks if the user wants to add another record
        if a == 'N' or a == 'n':  # Si el usuario responde 'n' o 'N', termina el ciclo / If user answers 'n' or 'N', ends the loop
            print(lista2)  # Muestra la lista de registros / Displays the list of records
            break  # Rompe el ciclo while / Breaks the while loop
