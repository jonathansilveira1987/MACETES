print('\nInsira o número de linhas.')
linhas = int(input('\033[0;32m>\033[m '))
print('\n')
for i in range(1, linhas + 1):
    for j in range(1, linhas + 1):
        if i == j or i + j == linhas + 1:
            print('X', end=' ')
        else:
            print('O', end=' ')
    print()
print('\n')