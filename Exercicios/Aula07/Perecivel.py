from Produto import Produto

class Perecivel(Produto):

    def __init__(self, tempMin, tempMax, id, nome, categoria, preco):
        super().__init__(id, nome, categoria, preco)
        self.tempMin = tempMin
        self.tempMax = tempMax
    
    def imprimir(self):
        super().imprimir()
        print(" Temperatura minima: ", self.tempMin)
        print(" Temperatura Máxima: ", self.tempMax)

    