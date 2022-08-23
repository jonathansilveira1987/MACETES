linhas = int(input('\nLinhas: '))
colunas = int(input('Colunas: '))
print()
for i in range(linhas):
    for linhas in range(colunas):
        print('\033[0;31m ● \033[m', end='')
    print()
print()