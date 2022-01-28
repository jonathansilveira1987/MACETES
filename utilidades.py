# Utilidades.

from time import sleep
from random import choice
import random
from speedtest import Speedtest
from random import randint
from time import sleep
import urllib
import urllib.request
from random import shuffle
from datetime import date

while True:
    # Programa principal!
    print('''
                            PACOTE DE FERRAMENTAS
    [ 01 ] - Apresentação                           [ 26 ] - Padrão
    [ 02 ] - Imprimir na tela                       [ 27 ] - Ordem de manutenção
    [ 03 ] - Olá Mundo!                             [ 28 ] - Ordem de apresentação
    [ 04 ] - Teste de conexão de internet           [ 29 ] - Número por Extenso
    [ 05 ] - Loading...                             [ 30 ] - Nome convertido
    [ 06 ] - Unindo dicionários e listas            [ 31 ] - Nome e sobrenome
    [ 07 ] - Sortear aluno                          [ 32 ] - Menu de opções
    [ 08 ] - Sorteio aleatório                      [ 33 ] - Análise de dados
    [ 09 ] - Detector de palíndromo                 [ 34 ] - Texto
    [ 10 ] - Semáforo                               [ 35 ] - Grupo da maioridade
    [ 11 ] - Tamanho do texto                       [ 36 ] - Loop Infinito
    [ 12 ] - Tem SANTO?                             [ 37 ] - Lista completa / pares / ímpares
    [ 13 ] - Vogais                                 [ 38 ] - Inversão de texto
    [ 14 ] - Validando expressões matemáticas       [ 39 ] - Interpolação de Strings
    [ 15 ] - Validando entrada de dados             [ 40 ] - Input padrão
    [ 16 ] - Validação de Dados                     [ 41 ] - 
    [ 17 ] - Tuplas com Times de Futebol            [ 42 ] - 
    [ 18 ] - Adivinhar número                       [ 43 ] - 
    [ 19 ] - Triângulo                              [ 44 ] - 
    [ 20 ] - Trabalhar com texto                    [ 45 ] - 
    [ 21 ] - Verificar se site está acessível       [ 46 ] -
    [ 22 ] - Sistema interativo de ajuda            [ 47 ] -
    [ 23 ] - Seu nome tem?                          [ 48 ] -
    [ 24 ] - Radar eletrônico                       [ 49 ] -
    [ 25 ] - Print especial                         [ 50 ] -
    ''')

    opcao = input("Informe a ferramenta desejada (0 para encerrar): ")

    # Encerrar aplicação.
    if opcao in '0':
        break
    # Apresentação.
    elif opcao == '01':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        nome = input("\nDigite seu nome: ")
        print("\nÉ um prazer te conhecer, {}!".format(nome))
    # Imprimir na tela.
    elif opcao == '02':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        # print("Hello world")
        a = input('\nDigite o que você deseja imprimir na tela: ')
        print('Você digitou: ', a)
    # Olá Mundo!
    elif opcao == '03':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Aqui vai o programa principal!
            print('''
Escolha uma das opções de "Olá Mundo":

[ 1 ] \033[1;31mVermelho\033[m
[ 2 ] \033[1;32mVerde\033[m
[ 3 ] \033[1;33mAmarelo\033[m
[ 4 ] \033[1;34mRoxo\033[m
[ 5 ] \033[1;35mRosa\033[m
[ 6 ] \033[1;36mAnil\033[m''')
            try:
                escolha = int(input("\nSua escolha (0 para encerrar)? ").strip())
                # Encerrar aplicação.
                if escolha == 0:
                    break
                elif escolha == 1:
                    print("\033[1;31m\nOlá, Mundo!\033[m") # Vermelho
                elif escolha == 2:
                    print("\033[1;32m\nOlá, Mundo!\033[m") # Verde
                elif escolha == 3:
                    print("\033[1;33m\nOlá, Mundo!\033[m") # Amarelo
                elif escolha == 4:
                    print("\033[1;34m\nOlá, Mundo!\033[m") # Roxo
                elif escolha == 5:
                    print("\033[1;35m\nOlá, Mundo!\033[m") # Rosa
                elif escolha == 6:
                    print("\033[1;36m\nOlá, Mundo!\033[m") # Anil
                else:
                    print("\nOPÇÃO NÃO ACEITA! Escolha entre 1, 2, 3, 4, 5 ou 6.")
            except ValueError:
                print('\nCOMANDO NÃO ACEITO!')
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\nDeseja continuar [1 - SIM / 0 - NÃO]? ")).strip().upper()[0]
            if resp == "0":
                break    
        print("\nVocê optou por finalizar!")
        # (Obs. Esse foi meu codigo usando cores e outras coisas, mas o que vai resolver é 
        # colocar o TRY, e o if dentro dele. Caso o usuario digite outra coisa, o EXCEPT VALUEERROR 
        # vai resolver mostrando um print.
    # Teste de conexão de internet.
    elif opcao == '04':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Aqui vai o programa principal!
            # SPEEDTEST 1.
            st = Speedtest()
            st.get_servers()
            best = st.get_best_server()
            ping_result = st.results.ping
            print('\n\033[32mSPEEDTEST 1\033[m')
            print('Obtendo informações...')
            print(f"\nServidor encontrado --> \033[31m{best['host']}\033[m localizado em \033[31m{best['country']}\033[m.\n")
            print('Sua velocidade de Download é de \033[0;33m{:.2f}\033[m Mbit/s.'.format(st.download() / 1024 / 1024))
            print('Sua velocidade de Upload é de \033[0;33m{:.2f}\033[m Mbit/s.'.format(st.upload() / 1024 / 1024))
            print('Seu PING atual é de \033[0;33m{:.2f}\033[m ms.\n'.format(ping_result))
            # SPEEDTEST 2.
            print('\033[32mSPEEDTEST 2\033[m')
            print('Obtendo informações...')
            def test():
                s = Speedtest()
                s.get_servers()
                s.get_best_server()
                s.download()
                s.upload()
                res = s.results.dict()
                return res['download'], res['upload'], res['ping']
            def main():
                for i in range(3):
                    d, u, p = test()
                    print('\nDownload: {:.2f} kb/s.'.format(d / 1024))
                    print('Upload: {:.2f} kb/s.'.format(u / 1024))
                    print('Ping: {} kb/s.\n'.format(p))
                    break
            if __name__ == "__main__":
                main()
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\033[0;33mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Loading...
    elif opcao == '05':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('''\033[0;32m
Loading…
█▒▒▒▒▒▒▒▒▒
\033[m''')

        sleep(3)
        print('''\033[0;32m
10%
███▒▒▒▒▒▒▒
\033[m''')

        sleep(3)
        print('''\033[0;32m
30%
█████▒▒▒▒▒
\033[m''')

        sleep(3)
        print('''\033[0;32m
50%
███████▒▒▒
\033[m''')

        sleep(3)
        print('''\033[0;32m
100%
██████████
\033[m''')

        sleep(2)
        print('\033[0;32mACREDITE\n')
        sleep(2)
        print('VOCÊ\n')
        sleep(2)
        print('SERÁ...\033[m')
        sleep(2)
        print('\n\033[0;33mMUITO FELIZ!!!\033[m \U0001F600')
    # Unindo dicionários e listas.
    elif opcao == '06':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        galera = list()
        pessoa = dict()
        soma = media = 0
        while True:
            pessoa.clear()
            pessoa['Nome'] = str(input('Nome: '))
            while True:
                pessoa['Sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
                if pessoa['Sexo'] in 'MF':
                    break
                print('ERRO! Por favor, digite apenas M ou F.')
            pessoa['Idade'] = int(input('Idade: '))
            soma = soma + pessoa['Idade']
            galera.append(pessoa.copy())
            while True:
                resp = str(input('Quer continuar [S/N]? ')).upper()[0]
                if resp in 'SN':
                    break
                print('ERRO! Responda apenas S ou N.')
            if resp == 'N':
                break
        print('-=' * 30)
        print(f'\nA - Ao todo temos {len(galera)} pessoas cadastradas.')
        media = soma / len(galera)
        print(f'B - A média de idade é de {media:5.2f} anos.')
        print(f'C - As mulheres cadastradas foram ', end='')
        for p in galera:
            if p['Sexo'] == 'F':
                print(f'{p["Nome"]}', end=' ')
        print()
        print(f'D - Lista das pessoas que estão acima da média: ')
        for p in galera:
            if p['Idade'] >= media:
                print('   ', end='')
                for k, v in p.items():
                    print(f'{k} = {v}; ', end='')
                print()
        print('<< ENCERRADO >>')
    # Sortear aluno.
    elif opcao == '07':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Programa principal!
            n1 = str(input("\n1º aluno: "))
            n2 = str(input("2º aluno: "))
            n3 = str(input("3º aluno: "))
            n4 = str(input("4º aluno: "))

            lista = [n1, n2, n3, n4]
            escolhido = choice(lista)

            print("\nO aluno escolhido foi \033[0;32m{}\033[m.\n".format(escolhido))
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Sorteio aleatório.
    elif opcao == '08':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Programa principal!
            dados1 = random.sample(range(10, 50), k=10)
            dados2 = random.sample(range(10, 50), k=5)
            dados3 = random.sample(range(10, 50), k=10)
            dados4 = random.sample(range(10, 50), k=5)

            print('\nRESULTADO DO SORTEIO ALEATÓRIO')
            print('\nSorteio 1 ->', dados1)
            print('Sorteio 2 ->', dados2)
            print('Sorteio 3 ->', dados3)
            print(f'Sorteio 4 -> {dados4}\n')
            # Sorteio aleatório com Tupla.
            numeros = (randint(1, 10), randint(1, 10), 
            randint(1, 10), randint(1, 10), randint(1, 10))
            print(f"\nOs valores sorteados foram: ", end="")
            for n in numeros:
                print(f"{n} ", end="")
            print(f"\nO maior valor sorteado foi {max(numeros)}.")
            print(f"O menor valor sorteado foi {min(numeros)}.\n")
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Palíndromo.
    elif opcao == '09':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Aqui vai o programa principal!
            frase = str(input("\nDigite algo: ")).strip().upper() # Espaços eliminados antes e depois / Letras todas em Maiúsculas.
            palavras = frase.split() # Frase separada em um vetor, em uma lista.
            junto = "".join(palavras) # Juntei a lista em uma string só para eliminar os espaços.
            print("Você digitou a frase {}.".format(junto))
            inverso = ""
            for letra in range(len(junto) - 1, -1, -1,):
                inverso += junto[letra] # Realizei o inverso da lista.
            print("O inverso de {} é {}.".format(junto, inverso))
            if inverso == junto:
                print("\033[0;34mTemos um PALÍNDROMO!\033[m")
            else:
                print("A frase digitada NÃO É UM PALÍNDROMO!")
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\n\033[0;33mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Semáforo. 
    elif opcao == '10':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Programa principal!
            print('\nSemáforo.')
            cor = input('\nCor (999 para encerrar): ').strip().upper().lower()
            if cor in "999":
                break
            elif cor == 'verde':
                        print('\n\033[0;32mAcelerar!\033[m\n')
            elif cor == 'amarelo':
                        print('\n\033[0;33mAtenção!\033[m\n')
            elif cor == 'vermelho':
                        print('\n\033[0;31mPare!\033[m\n')
            else:
                # Aqui vai o "Tente novamente!"
                cor != 'verde' 'amarelo' 'vermelho'
                print("\n\033[0;31mERRO! Informação incorreta, tente novamente.\033[m\n", end=" ")
                continue
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")
    # Tamanho do texto.
    elif opcao == '11':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Aqui vai o programa principal!
            texto = str(input('\nDigite seu texto: '))
            # "Aprendendo Python na disciplina de linguagem de programação."
            print(f"\nTamanho do texto = {len(texto)}")
            print(f"\nPython in texto = {'Python' in texto}")
            print(f"\nQuantidade de y no texto = {texto.count('y')}")
            print(f"\nAs 3 primeiras letras são: {texto[0:3]}\n")
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\n\033[0;33mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Tem SANTO?
    elif opcao == '12':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        cidade = str(input("\nEm que cidade você nasceu: ")).strip()
        print()
        print(cidade[0:5].upper() == "SANTO")
    # Vogais.
    elif opcao == '13':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        vogais = ['a', 'e', 'i', 'o', 'u'] # também poderia ter sido criada usando aspas duplas.
        for vogal in vogais:
            print(f'\nPosição = \033[0;32m{vogais.index(vogal)}\033[m, valor = \033[0;33m{vogal}\033[m')
    # Validando expressões matemáticas.
    elif opcao == '14':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Aqui vai o programa principal!
            expr = str(input("\nDigite a expressão: "))
            pilha = []
            for simb in expr:
                if simb == "(":
                    pilha.append("(")
                elif simb == ")":
                    if len(pilha) > 0:
                        pilha.pop()
                    else:
                        pilha.append(")")
                        break
            if len(pilha) == 0:
                print("\nSua expressão está válida!")
            else:
                print("\nSua expressão está inválida!")
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\n\033[0;33mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Validando entrada de dados.
    elif opcao == '15':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        def leiaInt(msg):
            ok = False
            valor = 0
            while True:
                n = str(input(msg))
                if n.isnumeric():
                    valor = int(n)
                    ok = True
                else:
                    print('\n\033[0;31mERRO! Digite um número inteiro válido.\033[m')
                if ok:
                    break
            return valor
        # Programa principal
        n = leiaInt('\nDigite um número: ')
        print(f'\nVocê acabou de digitar o número {n}')
    # Validação de Dados.
    elif opcao == '16':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        sexo = str(input("\nInforme seu sexo [M/F]: ")).strip().upper()[0]
        while sexo not in "MmFf":
            sexo = str(input("\033[0;31mDados inválidos.\033[m Por favor informe seu sexo [M/F]: ")).strip().upper()[0]
        print("\nSexo {} registrado com sucesso!".format(sexo))
    # 
    elif opcao == '17':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        times = ("Corinthians", "Palmeiras", "Santos", "Grêmio",
         "Cruzeiro", "Flamengo", "Vasco", "Chapecoense",
          "Atlético", "Botafogo", "Atlético-PR", "Bahia", 
        "São Paulo", "Fluminense", "Sport Recife",
         "EC Vitória", "Coritiba", "Avaí", "Ponte Preta",
          "Atlético-GO")
        print("-=" * 15)
        print(f"Lista de Times: {times}")
        print("-=" * 15)
        print(f"Os 5 primeiros são {times[0:5]}")
        print("-=" * 15)
        print(f"Os 4 útlimos são: {times[-4:]}")
        print("-=" * 15)
        print(f"Times em ordem alfabética: {sorted(times)}")
        print("-=" * 15)
        print(f'Posição do Chapecoense: {times.index("Chapecoense")+1}ª posição.')
        print("-=" * 15)
    # Adivinhar número.
    elif opcao == '18':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        computador = randint(0, 5) # Faz o computador "PENSAR".
        print("-=-" * 20)
        print("Vou pensar em um número entre 0 e 5. Tente Adivinhar...")
        print("-=-" * 20)
        jogador = int(input("Em que número eu pensei? ")) # Jogador tenta adivinhar
        print("Processando...")
        sleep(3)
        if jogador == computador:
            print("Parabéns, você conseguiu me vencer!")
        else:
            print("GANHEI! Eu pensei no número {} e não no {}!".format(computador, jogador))
    # Triângulo.
    elif opcao == '19':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n')
        def star_triangle(n):
            for i in range(n):
                print(" "*(n-1-i), end="")
                print("\033[0;31m*\033[m"*((i*2)+1))
        star_triangle(5)
        print()
    # Trabalhar com texto.
    elif opcao == '20':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        # Criar arquivo TXT.
        arquivo = open('bancodedados.txt', 'a')
        file = input('Digite algo: ')
        arquivo.write(file)
        # Lendo o arquivo criado:
        arquivo = open('bancodedados.txt','r')
        for linha in arquivo:
            linha = linha.rstrip()
            print (linha)
        arquivo.close()
        # Acrescentando texto ao arquivo criado, usando o modo de acesso 'a'
        print("\n")
        texto = input("Digite uma frase para acrescentar ao arquivo:\n")
        arquivo = open('arq01.txt','a')
        arquivo.write(texto + "\n")
        print("Opera��o conclu�da no arquivo " + arquivo.name + " usando o modo de acesso " + arquivo.mode)
        arquivo.close()
        print("\nTexto alterado:")
        arquivo = open('arq01.txt','r')
        for linha in arquivo:
            linha = linha.rstrip()
            print (linha)
        arquivo.close()
        # Acrescentando texto ao in�cio do arquivo, usando o modo 'r+'
        print("\n")
        texto = input("Digite um titulo para acrescentar ao arquivo:\n")
        arquivo = open('arq01.txt','r+')
        arquivo.seek(0)
        arquivo.write(texto + '\n')
        arquivo.close()
        print("\nTexto alterado:")
        arquivo = open('arq01.txt','r')
        for linha in arquivo:
            linha = linha.rstrip()
            print (linha)
        arquivo.close()
        arquivo = open("bancodedados.txt", "a")
        file = input('Digite algo: ')
        arquivo.write(file)
        # solution...?
        arquivo = open("texto.txt", "a")
        frases = list()
        frases.append("TreinaWeb \n")
        frases.append("Python \n")
        frases.append("Arquivos \n")
        frases.append("Django \n")
        arquivo.writelines(frases)
    # Verificar se site está acessível.
    elif opcao == '21':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        try:
            # site = urllib.request.urlopen('\nhttps://www.google.com.br/?gws_rd=ssl')
            site = urllib.request.urlopen(input('\nInforme o site: '))
        except:
            urllib.error.URLError
            print(f'\nO site não está acessível no momento.')
        else:
            print(f'\nO site foi acessado com sucesso!')
            # print(site.read())
    # Sistema interativo de ajuda.
    elif opcao == '22':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        c = ('\033[m',         # 0 - sem cores
            '\033[0;30;41m',  # 1 - vermelho
            '\033[0;30;42m',  # 2 - verde
            '\033[0;30;43m',  # 3 - amarelo
            '\033[0;30;44m',  # 4 - azul
            '\033[0;30;45m',  # 5 - roxo
            '\033[7;30m'      # 6 - branco
            )
        def ajuda(com):
            titulo(f'Acessando o manual do comando \'{com}\'', 4)
            print(c[6], end='')
            help(com)
            print(c[0], end='')
            sleep(2)
        def titulo(msg, cor=0):
            tam = len(msg) + 4
            print(c[cor], end='')
            print('~' * tam)
            print(f'  {msg}')
            print('~' * tam)
            print(c[0], end='')
            sleep(1)
        # Programa Principal
        comando = ''
        while True:
            titulo('SISTEMA DE AJUDA PyHELP', 2)
            comando = str(input("Função ou Biblioteca > "))
            if comando.upper == 'FIM':
                break
            else:
                ajuda(comando)
        titulo('ATÉ LOGO!', 1)
    # Seu nome tem?
    elif opcao == '23':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        nome = str(input("\nDigite seu nome completo: "))
        print("Seu nome tem Silva? {}.".format("SILVA" in nome.upper() or ("silva" in nome.lower())))
    # Radar eletrônico.
    elif opcao == '24':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Programa principal!
            velocidade = float(input("\nQual é a velocidade atual do carro? "))
            if velocidade > 80:
                print("\n\033[0;31mMULTADO! Você excedeu o limite permitido de velocidade que é de 80km/h.\033[m")
                multa = (velocidade - 80) * 7
                print("\033[0;33mVocê deve pagar uma multa de R$ {:.2f}.\033[m".format(multa))
            print("\n\033[0;32mTenha um bom dia! Dirija com segurança!\033[m\n")
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Print especial.
    elif opcao == '25':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        def escreva(msg):
            tam = len(msg) + 4
            print('*' * tam)
            print(f'  {msg}')
            print('*' * tam)
        escreva('Jonathan da Costa Silveira')
        escreva('Software Developer')
        escreva('Instagram: @jonathandev')
        escreva('Todo esse material foi desenvolvido, é atualizado e sempre melhorado por Jonathan.')
    # Padrão.
    elif opcao == '26':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
        # Aqui vai o programa principal!
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
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\n\033[0;33mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Ordem de manutenção.
    elif opcao == '27':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        ordens = [  '20565285',
            '30565285',
            '10565285',
            '30565285',
            '50565285',
            '20565285',
            '30565285',
            '90565285'
        ]
        print('\nOrdens de Manutenção:')
        print()
        for ordem in ordens:
            if ordem [0] == '2':
                print(f'Ordem {ordem} - \033[0;31mManutenção Preventiva.\033[m')
            if ordem [0] == '3':
                print(f'Ordem {ordem} - \033[0;33mManutenção Corretiva.\033[m')
            else:
                print(f'Ordem {ordem} - \033[0;32mManutenção Preditiva.\033[m')
    # Ordem de apresentação.
    elif opcao == '28':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        n1 = str(input("Primeiro aluno: "))
        n2 = str(input("Segundo aluno: "))
        n3 = str(input("Terceiro aluno: "))
        n4 = str(input("Quarto aluno: "))
        lista = [n1, n2, n3, n4]
        shuffle(lista)
        print("A ordem de apresentação será: ", lista)
    # Número por Extenso.
    elif opcao == '29':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        cont = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco",
                "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", 
                "Doze", "Treze", "Catorze", "Quinze", "Dezesseis", 
                "Dezessete", "Dezoito", "Dezenove", "Vinte")
        while True:
            num = int(input("Digite um número entre 0 e 20: "))
            if 0 <= num <= 20:
                break
            print("Valor incorreto, tente novamente.", end=" ")
        print(f"Você digitou o número {cont[num]}.")
    # Nome convertido.
    elif opcao == '30':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        def convert_letter(letter): # Função que converte as vogais para os símbolos.
            letter = letter.upper()
            if(letter == 'A'):
                return '@'
            if(letter == 'E'):
                return '&'
            if(letter == 'I'):
                return '!'
            if(letter == 'O'):
                return '#'
            if(letter == 'U'):
                return '*'
        def main():
            nome = input("\nDigite seu nome: ")
            print()
            new_name = ''
            for i in nome: # Realiza a iteração sobre as letras da palavra.
                print(i.upper())
                if(i.upper() == 'A' or i.upper() == 'E' or i.upper() == 'I' or i.upper() == 'O' or i.upper() == 'U'): # Aqui verificamos se a letra é uma vogal ou não
                    new_name += convert_letter(i.upper()) # Aqui a função é chamada para converter a letra
                else:
                    new_name += i.upper()
            print(new_name)
        if __name__ == '__main__':
            main()
    # Nome e sobrenome.
    elif opcao == '31':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        n = str(input("\nDigite seu nome completo: ")).strip()
        n = n.split()
        print("\nPrazer em te conhecer {}!".format(n[0]))
        print("Seu primeiro nome é {}.".format(n[0]))
        print("Seu último nome é {}.".format(n[len(n)-1]))
    # Menu de opções.
    elif opcao == '32':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        n1 = int(input("\n1º valor: "))
        n2 = int(input("2º valor: "))
        opcao = 0
        while opcao != 5:
            print('''
        - MENU -

[ 1 ] - Somar
[ 2 ] - Multiplicar
[ 3 ] - Maior
[ 4 ] - Novos Números
[ 5 ] - Sair do Programa
            ''')

            opcao = int(input("Qual sua opção? "))

            if opcao == 1:
                soma = n1 + n2
                print("A soma entre {} e {} é: {}.".format(n1, n2, soma))
            elif opcao == 2:
                produto = n1 * n2
                print("O resultado de {} X {} é: {}.".format(n1, n2, produto))    
            elif opcao == 3:
                if n1 > n2:
                    maior = n1
                else:
                    maior = n2
                print("Entre {} e {} o maior valor é: {}.".format(n1, n2, maior))
            elif opcao == 4:
                print("Informe os números novamente: ")
                n1 = int(input("Primeiro valor: "))
                n2 = int(input("Segundo valor: "))
            elif opcao == 5:
                print("Finalizando...")
            else:
                print("Opção inválida. Tente Novamente.")
            print("-=" * 10)
            sleep(2)    
        print("Fim do Programa! Volte Sempre!")
    # Análise de dados.
    elif opcao == '33':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        a = input("\nDigite algo: ")
        print("O tipo primitivo desse algo é: ", type(a))
        print("Só tem espaços?", a.isspace())
        print("É um número? ", a.isnumeric())
        print("É alfabético? ", a.isalpha())
        print("É alfanumérico? ", a.isalnum())
        print("Está em maiúsculas? ", a.isupper())
        print("Está em minúsculas? ", a.islower())
        print("Está capitalizada? ", a.istitle())
    # Maiúsculas & Minúsculas.
    elif opcao == '34':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        texto = input('\nDigite palavra ou texto: ')
        # texto = "Aprendendo Python na disciplina de linguagem de programação."
        print(f"\nPalavra / Texto = {texto}")
        print(f"Tamanho palavra / texto = {len(texto)} letras.")
        palavras = texto.split()
        palavras = texto.upper()
        print(f"\nMaiúscula(s) = {palavras}.")
        print(f"Tamanho de palavras = {len(palavras)}")
    # Grupo da Maioridade.
    elif opcao == '35':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        atual = date.today().year
        totalmaior = 0
        totalmenor = 0
        print()
        for pessoas in range(1, 5):
            nasc = int(input("Em que ano a {}ª pessoa nasceu: ".format(pessoas)))
            idade = atual - nasc
            if idade >= 21:
                totalmaior += 1        
            else:
                totalmenor += 1
        print("\nAo todo tivemos {} pessoa(s) maior(es) de idade.".format(totalmaior))
        print("E também tivemos {} pessoa(s) menor(es) de idade.".format(totalmenor))
    # Loop Infinito.
    elif opcao == '36':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        mundo4 = False
        print('\nObrigado pelo incrível trabalho')
        while not mundo4:
            print('No aguardo de novidades :D\n')
            break
        print(1)
        print(2)
        print(3)
        print(4)
        n = 1
        while True:
            print(n)
            n = n + 1
            break
    # Lista completa, pares, ímpares.
    elif opcao == '37':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        num = list()
        pares = list()
        impares = list()
        while True:
            print()
            num.append(int(input("Digite um número: ")))
            resp = str(input("Quer continuar [S/N]? "))
            if resp in "Nn":
                break
        for i, v in enumerate(num):
            if v % 2 == 0:
                pares.append(v)
            elif v % 2 == 1:
                impares.append(v)
        print("-=" * 30)
        print(f"A lista completa é {num}")
        print(f"A lista de pares é {pares}")
        print(f"A lista de ímpares {impares}")
    # Inversão de Texto.
    elif opcao == '38':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:    
            txt = str(input('\033[0;32m\nDigite o texto: \033[m'))[::-1]
            print()
            print(txt)   
            resp = " "
            while resp not in "10":
                resp = str(input("\nDeseja continuar [1 - SIM / 0 - NÃO]? ")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Interpolação de strings.
    elif opcao == '39':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        nome = str(input('\nNome: '))
        idade = int(input('Idade: '))

        print('\nPython 2')
        print('\033[0;31m%s tem %d anos.\033[m' % (nome, idade))

        print('\nPython 3')
        print('\033[0;32m{} tem {} anos.\033[m'.format(nome, idade))
        
        print('\nPython 3.6+')
        print(f'\033[0;33m{nome} tem {idade} anos.\033[m')
    # Input padrão.
    elif opcao == '40':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
        # Aqui vai o programa principal!
            print('\nDigite algo.')
            a = input(('\n\033[0;32m>\033[m '))
            print('\nVocê digitou...', a)
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\n\033[0;33mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")




    # 
    elif opcao == '41':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
    # 
    elif opcao == '42':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
    # 
    elif opcao == '43':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
    # 
    elif opcao == '44':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
        # 
    elif opcao == '45':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
        # 
    elif opcao == '46':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
        # 
    elif opcao == '47':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
        # 
    elif opcao == '48':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
        # 
    elif opcao == '49':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
        # 
    elif opcao == '50':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')























    else:
        # Aqui vai o "Tente novamente!"
        opcao != '01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40'
        print("\n\033[0;31mInformação incorreta, tente novamente.\033[m\n", end=" ")
        continue
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\n\033[0;34mDeseja continuar no programa principal [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")