# Maior e menor valores.

a = int(input("\n1º valor: "))
b = int(input("2º valor: "))
c = int(input("3º valor: "))

# Verificando quem é o menor.
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

# Verificando que é o maior.
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print("\nO menor valor digitado foi \033[0;32m{}\033[m.".format(menor))
print("\nO maior valor digitado foi \033[0;33m{}\033[m.\n".format(maior))