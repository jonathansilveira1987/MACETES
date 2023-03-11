# Cálculo do Fatorial.

# Utilizando Módulo.
from math import factorial
n = int(input("Digite um número para calcular seu Fatorial: "))
f = factorial(n)
print("O Fatorial de {} é {}.".format(n, f))


# Modo Tradicional.
n = int(input("Digite um número para calcular seu Fatorial: "))
c = n
f = 1
print("Calculando {}! = ".format(n), end=" ")
while c > 0:
    print("{}".format(c), end=" ")
    print("X" if c > 1 else "=", end=" ")
    f *= c
    c -= 1
print("{}.".format(f))