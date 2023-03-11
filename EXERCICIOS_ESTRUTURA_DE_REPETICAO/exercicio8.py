# 8. Faça um programa que leia 5 números e informe a soma e a média dos números.
# Desenvolvido por Jonathan Silveira - Instagram: @jonathandev01

print("\nVocê vai informar 5 números e eu vou calcular a méida entre eles")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
num4 = float(input("Digite o quarto número: "))
num5 = float(input("Digite o quinto número: "))

soma = num1 + num2 + num3 + num4 + num5
media = soma / 5

print("O valor média dos números digitados é: ",round(media))