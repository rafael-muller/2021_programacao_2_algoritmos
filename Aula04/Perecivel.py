from Produto import Produto
from datetime import date

class Perecivel( Produto):

    def __init__(self, nome = None, preco = 0.0, validade = date.today()):
        super().__init__(self, nome, preco)
        self.validade = validade

    def cadastrar(self):
       print("O Produto", self.nome, "de preço", self.preco, "com validade ", self.validade, "foi cadastrado") 