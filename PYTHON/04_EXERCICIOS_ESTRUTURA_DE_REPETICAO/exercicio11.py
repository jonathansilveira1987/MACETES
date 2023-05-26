# 11. Altere o programa anterior para mostrar no final a soma dos números.
# Desenvolvido por Jonathan Silveira - Instagram: @jonathandev01

num1 = int(input('\nDigite o primeiro número inteiro: '))
num2 = int(input('Digite o segundo número inteiro: '))

print()
for i in range(num1, num2 + 1):
    print(i)
for j in range(num2, num1 + 1):
    print(j)

soma = num1 + num2
print(f'\nA soma dos dois números inteiros é {soma}\n')