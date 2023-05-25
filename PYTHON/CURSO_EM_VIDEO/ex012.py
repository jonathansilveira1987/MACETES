preco = float(input("\nQual é o preço do produto: R$ "))
novo = preco - (preco * 5 / 100)
valor_desconto = preco - novo
print("\nO produto que custava R$ {:.2f}, na promoção com desconto de 5% vai custar R$ {:.2f}\n".format(preco, novo))
print("Você obteve um desconto de R$ {:.2f}.\n".format(valor_desconto))