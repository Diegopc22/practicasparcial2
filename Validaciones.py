class validacion():  # Define la clase validacion / Defines validation class
    def __init__(self):  # Constructor de la clase / Class constructor
        self.suma = 0  # Inicializa variable para suma / Initializes variable for sum
        self.promedio = 0.0  # Inicializa variable para promedio / Initializes variable for average
    
    def ValidarNumeros(self, valor):  # Método para validar si es número / Method to validate if number
        if valor.isdigit():  # Verifica si el string contiene solo dígitos / Checks if string contains only digits
            return True  # Retorna verdadero si es número / Returns true if number
        else:
            return False  # Retorna falso si no es número / Returns false if not number
        
    def Promedio(self, lista):  # Método para calcular promedio / Method to calculate average
        for i in lista:  # Itera sobre cada elemento de la lista / Iterates over each list element
            self.suma += i  # Suma el elemento actual al total / Adds current element to total
        self.promedio = self.suma / len(lista)  # Calcula el promedio (suma/cantidad) / Calculates average (sum/count)
        return self.promedio  # Retorna el valor del promedio / Returns average value