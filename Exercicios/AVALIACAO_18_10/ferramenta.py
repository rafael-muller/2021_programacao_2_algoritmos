from Exercicios.AVALIACAO_18_10.furadeira import Furadeira
from Exercicios.AVALIACAO_18_10.lixadeira import Lixadeira


class Ferramenta:
    def __init__(self, nome, tensao, preco):
        self.nome = nome
        self.tensao = tensao
        self.preco = preco

    def getInformacoes(self):
        return self.nome, self.tensao, self.preco

    def imprimir(self):
        print ("Nome do produto: ",self.nome)
        print ("Tensao do produto: ", self.tensao)
        print ("Preco: ", self.preco)
        print (Furadeira)
        print (Lixadeira)