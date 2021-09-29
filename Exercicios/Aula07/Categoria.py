class Categoria:

    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    def imprimir(self):
        print("ID Categoria: ", self.id)
        print("Categoria: ", self.nome)