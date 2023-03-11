# 7. Faça um programa que leia 5 números e informe o maior número.
# Desenvolvido por Jonathan Silveira - Instagram: @jonathandev01

print("\nVocê vai informar 5 números e eu vou dizer qual deles é o maior")
print("Digite apenas números inteiros\n")
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
num4 = int(input("Digite o quarto número: "))
num5 = int(input("Digite o quinto número: "))

if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5:
    print("O maior número é este -> ",num1)
elif num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5:
    print("O maior número é este -> ",num2)
elif num3 > num1 and num3 > num2 and num3 > num4 and num3 > num5:
    print("O maior número é este -> ",num3)
elif num4 > num1 and num4 > num2 and num4 > num3 and num4 > num5:
    print("O maior número é este -> ",num4)
else:
    print("O maior número é este -> ",num5)