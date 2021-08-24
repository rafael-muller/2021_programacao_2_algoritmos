#Sem parâmetros e sem retorno
def imprimirMeuNome():
    print("Olá pessoal")
    print("Bem-Vindos ao novo semestre")

#Com parâmetros e com retorno
def getCalcularSalario (horas, valorHora):
    if horas == None or valorHora == None:
        return None
    else:
        salario = horas * valorHora
        return salario
    


#Com parâmetros e sem retorno
def imprimirSalario(horas, valorHora):
    salario = horas * valorHora
    print("Salario: ", salario)

#Com parâmetros e sem retorno
def imprimirSalario2(horas = 220, valorHora = 10):
    salario = getCalcularSalario(horas, valorHora)
    print("Salario: ", salario)

#Sem parâmetros e com retorno
def getValorPI():
    return 3.14

areaCirculo = getValorPI() * (2 * 2)
print("Área do circulo com raio 2: ", areaCirculo)

imprimirSalario2( )
imprimirSalario2( 150)
imprimirSalario2( 100 , 20 )
imprimirSalario2( None , 15)

carros = ["Uno", "Doblo", "Toro"]
print( carros )

print ( carros[1] )


posicao = int( input("Informe a posição do Veículo (de 0 a 2)") )
print ("Carro Selecionado: ", carros[posicao])