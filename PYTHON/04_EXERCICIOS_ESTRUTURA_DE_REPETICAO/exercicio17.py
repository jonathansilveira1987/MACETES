# 17. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
# Ex.: 5!=5.4.3.2.1=120
# Desenvolvido por Jonathan Silveira - Instagram: @jonathandev01

# Função Fatorial
from math import factorial
n = int(input("Digite um número para calcular seu fatorial: "))
f = factorial(n)
print("O fatorial de {} é {}.".format(n, f))

# Calculando de forma manual
n = int(input("Digite um número para calcular seu fatorial: "))
c = n
f = 1
print("Calculando {}! = ".format(n), end="")
while c > 0:
    print("{}".format(c), end=" ")
    print("x" if c > 1 else "=", end=" ")
    f = f * c
    c -= 1

print("{}".format(f))