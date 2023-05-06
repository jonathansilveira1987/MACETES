# Criar arquivo TXT.
nome = input('\nNome do Arquivo: ')
arquivo = open(nome + '.txt', 'a')
file = input('\nDigite algo: ')
arquivo.write(file + '\n')
print()
# Acrescentando título ao início do arquivo, usando o modo 'r+'
titulo = input('Digite um título para acrescentar ao arquivo: ')
arquivo = open(nome + '.txt', 'r+')
arquivo.seek(0)
arquivo.write(titulo + '\n')
arquivo.close()
print()



'''

print("\nTexto alterado:")
arquivo = open(nome + '.txt', 'r')
for linha in arquivo:
    linha = linha.rstrip()
    print (linha)
arquivo.close()
arquivo = open(nome + '.txt', 'a')
file = input('Digite algo: ')
arquivo.write(file)



'''
