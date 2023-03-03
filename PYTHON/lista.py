elemento = int(input('\nInforme o número de elementos para a lista: '))
print()
conteudo = [input("Dado: ") for i in range(elemento)]
with open('lista.txt', 'w') as arquivo:
    arquivo.write("\n".join(conteudo))
    arquivo.write(f'\nTotal de arquivos {len(conteudo)}') # Informa total de arquivos.
print('\nArquivo salvo com o nome de lista\n')










'''

with open('lista01.txt', 'w') as arquivo:
    arquivo.write(str(conteudo))




# conteudo = [1, 2, 3]
# Primeira solução.
elemento = int(input('\nInforme o número de elementos para a lista: '))
print()
conteudo = [input("Dado: ") for i in range(elemento)]
print(f'\n\033[0;32m{conteudo}\033[m')

'''