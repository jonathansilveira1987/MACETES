# ADICIONA MAIS DADOS EM UM MESMO ARQUIVO.
nome = input('\nNome do Arquivo: ')
elemento = int(input('\nInforme o número de elementos para a lista: '))
print()
c = 0
for i in range(c + 1):
    conteudo = [input(f'{i + 1}º dado: ') for i in range(elemento)]
    with open(nome + '.txt', 'a') as arquivo:
        arquivo.write('\n'.join(conteudo))
        arquivo.write(f'\nTotal de arquivos informados = {len(conteudo)}') # Informa total de arquivos.
        arquivo.write('\n\n')
    print(f'\nArquivo salvo com o nome de {nome}\n')
    break