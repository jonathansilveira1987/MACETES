# Sorteio
from random import choice

n1 = str(input("\n1º aluno: "))
n2 = str(input("2º aluno: "))
n3 = str(input("3º aluno: "))
n4 = str(input("4º aluno: "))

lista = [n1, n2, n3, n4]
escolhido = choice(lista)

print("\nO aluno escolhido foi \033[0;32m{}\033[m.\n".format(escolhido))