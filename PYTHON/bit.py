gigabyte = float(input('\nGigabyte: '))
convert = gigabyte * 1024
print(f'\n{gigabyte} Gigabyte(s) equivale a {int(convert)} Megabytes.\n')

n = int(input('Informe um número inteiro: '))
quadrado = n * n 
print(f'\nO quadrado de {n} é {quadrado}\n')

s = 'Python Possibilities'
print(len(s.partition('P')[0]))
print()

# n = 5
for i in range(1, n+1):
    print(' ' * (i-1), end='')
    print('*' * (2*(n-i)+1))
print()

a = float(input('\nVetor A: '))
b = float(input('Vetor B: '))

if a < b:
    c = a / b
    d = c * 100
    print(f'\n{a:.2f} equivale a {round(d)}% de {b:.2f}\n')
else:
    c = b / a
    d = c * 100
    print(f'\n{b:.2f} equivale a {c}% de {a:.2f}\n')


# Por exemplo, se você quer calcular 35% de 500, 
# multiplique 35 por 500. Fazendo isso você obtém o valor de 
# 35 x 500 = 17500; Divida o resultado obtido por 100