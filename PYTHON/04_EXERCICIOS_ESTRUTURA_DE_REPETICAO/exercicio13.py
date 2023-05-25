# 13. Faça um programa que peça dois números, base e expoente, calcule e mostre 
# o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.
# Desenvolvido por Jonathan Silveira - Instagram: @jonathandev01

base = int(input("Digite o valor Base: "))
expoente = int(input("Digite o valor Expoente: "))
count = 1
potencia = 1

while count <= expoente:
    potencia *= base
    count += 1
print(base,"^",expoente,"=",potencia)