# Criar nome TXT.
nome = input('\nNome do Arquivo: ')
arquivo = open(nome + '.txt', 'a')
frases = list()
frases.append('Python \n')
frases.append('Arquivos \n')
frases.append('Django \n')
frases.append('Flask \n')
frases.append('Developer \n')
arquivo.writelines(frases)
print(f'\nO arquivo {nome} foi criado com sucesso!\n')