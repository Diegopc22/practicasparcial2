class Validacion():
    def __init__(self):
        pass

    def ValidarMinus(self, valor):
        if len(valor) == 0:
            return True
        if ord(valor[0]) < 97 or ord(valor[0]) > 122:
            return False
        return self.ValidarMinus(valor[1:])
    
    def ValidarMayus(self, valor):
        if len(valor) == 0:
            return True
        if ord(valor[0]) < 65 or ord(valor[0]) > 90:
            return False
        return self.ValidarMayus(valor[1:])

    
    def ValidarNumeros(self, valor):
        if len(valor) == 0:
            return True
        if ord(valor[0]) < 48 or ord(valor[0]) > 57:
            return False
        return self.ValidarNumeros(valor[1:])

if __name__ == '__main__':
    app = Validacion()

