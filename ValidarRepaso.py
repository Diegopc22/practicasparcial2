class Validar():  # Define la clase Validar / Defines Validation class
    def __init__(self):  # Constructor de la clase / Class constructor
        self.index = 0  # Inicializa contador para recorrer strings / Initializes counter for string traversal

    def ValidarAscii(self, valor):  # Método para validar usando códigos ASCII / Method to validate using ASCII codes
        con = 0  # Contador para dígitos / Counter for digits
        con2 = 0  # Contador para letras / Counter for letters
        for i in valor:  # Itera sobre cada carácter del string / Iterates over each character in string
            if ord(i) >= 48 and ord(i)<= 57:  # Verifica si es dígito (ASCII 48-57) / Checks if digit (ASCII 48-57)
                con += 1  # Incrementa contador de dígitos / Increments digit counter
            if (ord(i)>= 65 and ord(i)<=90) or (ord(i)>= 97 and ord(i)<=122):  # Verifica si es letra (A-Z o a-z) / Checks if letter (A-Z or a-z)
                con2 += 1  # Incrementa contador de letras / Increments letter counter

        if con == len(valor):  # Si todos los caracteres son dígitos / If all characters are digits
            return "Numeros"  # Retorna "Números" / Returns "Numbers"
        elif con2 == len(valor):  # Si todos los caracteres son letras / If all characters are letters
            return "Letras"  # Retorna "Letras" / Returns "Letters"
        else:  # Si es mezcla / If it's a mix
            return "Letras y numeros"  # Retorna "Letras y números" / Returns "Letters and numbers"

    def ValidarConError(self, valor):  # Método para validar usando manejo de errores / Method to validate using error handling
        a = 0  # Variable para enteros / Variable for integers
        b = 0.0  # Variable para decimales / Variable for decimals
        try:
            a = int(valor)  # Intenta convertir a entero / Tries to convert to integer
            return "numeros"  # Retorna "números" si es exitoso / Returns "numbers" if successful
        except ValueError:  # Captura error de conversión a entero / Catches integer conversion error
            try:
                b = float(valor)  # Intenta convertir a decimal / Tries to convert to decimal
                return "Es numero real o con decimales"  # Retorna mensaje para decimales / Returns message for decimals
            except ValueError:  # Captura error de conversión a decimal / Catches decimal conversion error
                return "letras o numeros"  # Retorna para texto mixto / Returns for mixed text
            
    def ValidarConString(self, valor):  # Método recursivo para validar correo / Recursive method to validate email
        print(valor)  # Imprime el valor para depuración / Prints value for debugging
        if self.index < len(valor):  # Verifica si no ha llegado al final del string / Checks if not reached end of string
            if valor[self.index] == '@':  # Busca el símbolo @ / Looks for @ symbol
                self.index = 0  # Reinicia el índice / Resets index
                return "se es un correo"  # Retorna que es correo (typo: debería ser "sí es un correo") / Returns it's email (typo: should be "sí es un correo")
            else:
                if self.index < len(valor):  # Verifica nuevamente el índice / Checks index again
                    self.index += 1  # Incrementa el índice / Increments index
                    return self.ValidarConString(valor)  # Llama recursivamente la función / Calls function recursively
                else:
                    self.index = 0  # Reinicia el índice / Resets index
                    return "no es un correo"  # Retorna que no es correo / Returns it's not email
        else:
            self.index = 0  # Reinicia el índice / Resets index
            return "no es un correo"  # Retorna que no es correo / Returns it's not email
        
        # if "@" in valor:  # Método alternativo comentado / Alternative method commented out
        #     return "si es un correo"  # Retorna que es correo / Returns it's email
        # else:
        #     return "no es in correo"  # Retorna que no es correo (typo) / Returns it's not email (typo)