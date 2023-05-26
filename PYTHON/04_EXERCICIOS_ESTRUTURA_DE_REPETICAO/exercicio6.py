# 6. Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. 
# Depois modifique o programa para que ele mostre os números um ao lado do outro.
# Desenvolvido por Jonathan Silveira - Instagram: @jonathandev01

lista1 = int(input('\nQuantidade de valores na lista 1: '))
lista2 = int(input('\nQuantidade de valores na lista 2: '))

print('\033[32m')
for j in range (lista1 + 1):
    print(j)

print('\033[m \033[33m')
print(list(range(lista2 + 1)))
print('\033[m')