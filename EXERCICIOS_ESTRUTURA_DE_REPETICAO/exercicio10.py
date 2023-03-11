# 10. Faça um programa que receba dois números inteiros e gere os números inteiros 
# que estão no intervalo compreendido por eles.
# Desenvolvido por Jonathan Silveira - Instagram: @jonathandev01

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

for i in range (num1 + 1, num2):
    print(i)