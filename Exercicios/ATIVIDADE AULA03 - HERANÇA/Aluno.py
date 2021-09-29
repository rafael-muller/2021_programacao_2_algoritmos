#construa um algoritmo com a classe aluno OK
#codigo, nome , mat.  a classe aluno
#possui duas subclasses a classe AluEnsinoMedio  'ano'
#AlunoGraduacao 'semestre'
#as 3 classes possuem metodo construtor
#e tambem metodo imprimir, que imprime
#na tela os valores de todos atributos da classe

class Aluno:
    
    def __init__(self, codigo, mat, nome):
        self.codigo = codigo
        self.nome = nome
        self.mat = mat

    def setNome(self, nome):
        self.nome =  nome

    def setCodAluno (self, codigo):
        self.codigo = codigo
    def setMatricula (self, mat):
       return self.mat

    def getNome(self, nome):
        return self.nome

    def getCodAluno (self, codigo):
        return self.codigo