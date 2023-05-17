# 21. Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário o valor
# do saque e depois informar quantas notas de cada valor serão fornecidas.
# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais 
# e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas 
# notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três 
# notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
# Desenvolvido por Jonathan Silveira - Instagram: @ jonathandev01

saque = int(input("Digite o valor do saque: "))

if saque < 10 or saque > 600:
    print("Valor inválido!")

cem = int(saque/100)
saque = saque % 100
    
cinquenta = int(saque/50)
saque = saque % 50

vinte = int(saque/20)
saque = saque % 20

dez = int(saque/10)
saque = saque % 10

cinco = int(saque/5)
saque = saque % 5

um = int(saque/1)
saque = saque % 1

print("{} Nota(s) R$ 100,00." .format(cem))
print("{} Notas(s) R$ 50,00." .format(cinquenta))
print("{} Notas(s) R$ 20,00." .format(vinte))
print("{} Notas(s) R$ 10,00." .format(dez))
print("{} Notas(s) R$ 5,00." .format(cinco))
print("{} Notas(s) R$ 1,00." .format(um))