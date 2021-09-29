
from Pessoa import Pessoa
from Cidade import Cidade


class Fisica(Pessoa):
    
    def __init__(self, id, nome,cid: Cidade, cpf):
        super().__init__(id, nome, cid)
        self.cpf = cpf

    def imprimir(self):
        print(" Pessoa Fisica ", self.id, " - ", self.nome)
        print(" Mora em: ", self.municipio.nome)
        print(" CPF: ", self.cpf)