linhas = int(input('\nDigite o número de linhas de padrão diamante: '))

print('\033[36m')
for i in range(1, linhas + 1):
    for j in range(1, linhas - i + 1):
        print(end = ' ')
    for k in range(1, (2 * i)):
        print(k, end = '')
    print()
for i in range(linhas - 1, 0, -1):
    for j in range(1, (linhas - i + 1)):
        print(end = ' ')
    for k in range(1, (2 * i)):
        print(k, end = '')
    print()
print('\033[m')