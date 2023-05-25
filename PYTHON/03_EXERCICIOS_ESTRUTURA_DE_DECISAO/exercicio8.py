# 8. Faça um programa que pergunte o preço de três produtos e informe qual produto você 
# deve comprar, sabendo que a decisão é sempre pelo mais barato.
# Desenvolvido por Jonathan Silveira - Instagram: @ jonathandev01

precoProduto1 = float(input("Digite o preço do primeiro produto: "))
precoProduto2 = float(input("Digite o preço do segundo produto: "))
precoProduto3 = float(input("Digite o preço do terceiro produto: "))

if precoProduto1 < precoProduto2:
    if precoProduto1 < precoProduto3:
        print("Você deve comprar o primeiro produto!")
    else:
        print("Você deve comprar o terceiro produto!")
else:
    if precoProduto2 < precoProduto3:
        print("Você deve comprar o segundo produto!")
    else:
        print("Você deve comprar o terceiro produto!")