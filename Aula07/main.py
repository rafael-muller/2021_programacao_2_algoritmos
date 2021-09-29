from Fisica import Fisica
from Cidade import Cidade
from Pessoa import Pessoa

cid01 = Cidade (1, "Porto Alegre")
cid02 = Cidade (2, "Capão da Canoa")

p1 = Pessoa(1, "João", cid02)
p2 = Pessoa(2, "Maria", cid01)
p3 = Pessoa(3, "José", cid02)

cid01.imprimir()
print("--------------------------")
p1.imprimir()

pf1 = Fisica(1, "J", cid01, "000")
pf1.imprimir()