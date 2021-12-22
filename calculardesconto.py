# Calcular desconto.

preco = float(input("\nQual é o preço do produto: R$ "))
desc = float(input('Desconto % : '))
novo = preco - (preco * desc / 100)
valor_desconto = preco - novo
print("\nO produto que custava R$ {:.2f}, na promoção com desconto de {:.0f}% vai custar R$ {:.2f}.".format(preco, desc, novo))
print("Você obteve um desconto de R$ {:.2f}.\n".format(valor_desconto))