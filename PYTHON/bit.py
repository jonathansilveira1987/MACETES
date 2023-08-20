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