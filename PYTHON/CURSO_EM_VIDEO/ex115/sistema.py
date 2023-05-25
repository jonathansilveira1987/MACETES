from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'basededados.txt'

if arquivoExiste(arq):
    print('\nArquivo encontrado com sucesso!\n')
else:
    print('\nArquivo não encontrado!\n')
    criarArquivo(arq)

cabecalho('SISTEMA DE ARQUIVO v 1.0')

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # cabecalho('Opção 1')
        # Opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        # Opção para cadastrar uma nova pessoa.
        # cabecalho('Opção 2')
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opção de sair do sistema.
        cabecalho('Saindo do Sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(1)



