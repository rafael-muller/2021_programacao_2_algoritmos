from Categoria import Categoria
 
class Produto:

    def __init__(self, id, nome, categoria, preco):
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
    
    def imprimir(self):
        print("ID do produto:", self.id)
        print("Nome do produto: ", self.nome)
        print("Categoria do produto: ", self.categoria.nome)
        print(" Preço: ", self.preco)