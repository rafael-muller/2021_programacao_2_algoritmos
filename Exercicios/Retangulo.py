class Retangulo:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura


    def imprimir(self):
        print("Altura: ", self.altura)
        print("Largura: ", self.largura)

    def calculaArea(self):
        area = self.altura * self.largura
        return area

a = float(input("Informe a Altura: "))
l = float(input("Informe a Largura: "))
retangulo = Retangulo(a, l)
print(f"\nA área do retângulo é: {retangulo.calculaArea()} m quadrados")






