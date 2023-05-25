# 11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.
# Desenvolvido por Jonathan Silveira - Instagram: @jonathandev01

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
numr = float(input("Digite um número real: "))

print ("Soma: ", ((2*num1) * (num2 / 2)))
print ("Produto: ", (3 * num1) + numr)
print ("Cubo: ", numr ** numr)