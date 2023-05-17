# 6. Faça um Programa que leia três números e mostre o maior deles.
# Desenvolvido por Jonathan Silveira - Instagram: @ jonathandev01

num1 = int(input("Número um: "))
num2 = int(input("Número dois: "))
num3 = int(input("Número três: "))

if num1 > num2 and num1 > num3:
    print("O número um é o maior: ", num1)
elif num2 > num1 and num2 > num3:
    print("O número dois é o maior: ", num2)
else:
    print("O número três é o maior: ", num3)