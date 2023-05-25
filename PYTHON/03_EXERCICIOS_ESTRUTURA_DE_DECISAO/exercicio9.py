# 9. Faça um Programa que leia três números e mostre-os em ordem decrescente.
# Desenvolvido por Jonathan Silveira - Instagram: @ jonathandev01

lista = []
num = int(input('\nQuantos números deseja adicionar na lista: '))
qtd = num
print()
for i in range(qtd):
    elemento = int(input('Digite um número: '))
    lista.append(elemento)

lista.sort(reverse = True) # Ordena os elementos
print(f'\n{lista}\n')