from Produto import Produto
from Categoria import Categoria
from Perecivel import Perecivel

cat = Categoria(1, "Hortifruti")
prod = Produto(1, "Maçã", cat, 4.50)

#categoria.imprimir()
prod.imprimir()
#prod.categoria.imprimir()

perecivel1 = Perecivel(10, 15, 1, "Manga", cat, 9.00)

#Perecivel1.imprimir chama linha 10 do perecivel
perecivel1.imprimir()
#perecivel1.categoria.imprimir chama a linha 7 da categoria
#perecivel1.categoria.imprimir()










#categoria = Categoria(1, "Hortifruti")

#p1 = Produto(1, "Maçã", categoria, 1.50)

#p1.imprimir()

#prod1 = Perecivel(12.0, 30.0, 1, "Cebola", categoria, 3.50)

#prod1.imprimir()