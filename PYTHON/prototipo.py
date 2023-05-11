titulo = str(input('\nDefina um título: '))
print(f'\n{titulo: ^50}') # Centralizado.
print(f'\n{titulo: >50}') # Direita.
print(f'\n{titulo: <50}') # Esquerda.

# Contador Manual.
n = int(input('\nAté quanto você deseja contar: '))
print('\033[32m')
for i in range(n + 1):
    print(i)
print('\033[m')

# Contador com Ponto Incial & Final.
a = int(input('Ponto Inicial: '))
b = int(input('Ponto Final: '))
print('\033[33m')
c = range(a, b + 1)
for d in c:
    print(d)
print('\033[m')