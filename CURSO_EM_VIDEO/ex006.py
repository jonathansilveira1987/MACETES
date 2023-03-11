n = int(input("\nDigite um número: "))

d = n * 2
t = n * 3
r = n ** (1/2)
# r = pow(n, (1/2)) # Usando função potência.

print("\nO dobro de {} é: {}.".format(n, d))
print("O triplo de {} é: {}.".format(n, t))
print("A raiz quadrada de {} é: {:.2f}.\n".format(n, r))