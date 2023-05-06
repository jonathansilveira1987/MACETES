# Criar arquivo TXT.
nome = input('\nNome do Arquivo: ')
arquivo = open(nome + '.txt', 'a')
file = input('\nDigite algo: ')
arquivo.write(file + '\n')
print()
# Alterar conteúdo.
print('Conteúdo alterado: ')
arquivo = open(nome + '.txt', 'r')
for linha in arquivo:
    linha = linha.rstrip()
    print (linha)
arquivo.close()
arquivo = open(nome + '.txt', 'a')
file = input('\nDigite algo: ')
arquivo.write(file)
print()