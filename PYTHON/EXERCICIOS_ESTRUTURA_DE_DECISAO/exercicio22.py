# 22. Faça um Programa que peça um número inteiro e determine se ele é par ou impar. 
# Dica: utilize o operador módulo (resto da divisão).
# Desenvolvido por Jonathan Silveira - Instagram: @ jonathandev01

num = int(input("Digite um número inteiro: "))

if (num % 2) == 0:
    print("O número digitado é PAR")
else:
    print("O número digitado é ÍMPAR")