from ferramenta import Ferramenta


class Furadeira(Ferramenta):
    def __init__(self, nome, tensao, preco,potencia):
        self._potencia = potencia    

    def imprimir(self):
        print ("Potencia: ", self._potencia)
        print (Ferramenta)
#implementar metodo getinformacoes de ferramenta
