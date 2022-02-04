# Utilidades 2.0.

from time import sleep
from random import choice
from datetime import date
from datetime import datetime
import calendar
from datetime import datetime, time
import datetime as dt

while True:
    # Programa principal!
    print('''
                            PACOTE DE FERRAMENTAS
    [ 01 ] - Escolha                                [ 26 ] - 
    [ 02 ] - Envio de e-mail                        [ 27 ] - 
    [ 03 ] - Emojis                                 [ 28 ] - 
    [ 04 ] - Descobrir número                       [ 29 ] - 
    [ 05 ] - Dissecando dado                        [ 30 ] - 
    [ 06 ] - Contagem regressiva                    [ 31 ] - 
    [ 07 ] - Classificando atletas                  [ 32 ] - 
    [ 08 ] - Casas decimais                         [ 33 ] - 
    [ 09 ] - Contar semanas                         [ 34 ] - 
    [ 10 ] - Calendário                             [ 35 ] - 
    [ 11 ] - Cadastro de trabalhador                [ 36 ] - 
    [ 12 ] - Alistamento Militar                    [ 37 ] - 
    [ 13 ] - Analisador completo                    [ 38 ] - 
    [ 14 ] - Analisando triângulo                   [ 39 ] - 
    [ 15 ] - Análise completa de nome               [ 40 ] - 
    [ 16 ] - Análise de dados                       [ 41 ] - 
    [ 17 ] - Análise de unidades                    [ 42 ] - 
    [ 18 ] - Análise de letra específica            [ 43 ] - 
    [ 19 ] - Ano bissexto                           [ 44 ] - 
    [ 20 ] - Data & hora atual                      [ 45 ] - 
    [ 21 ] - Cores em Python                        [ 46 ] - 
    [ 22 ] - Agenda                                 [ 47 ] - 
    [ 23 ] - Cadastro de jogador                    [ 48 ] - 
    [ 24 ] - Ficha do jogador                       [ 49 ] - 
    [ 25 ] -                                        [ 50 ] - 
    ''')

    opcao = input("Informe a ferramenta desejada (0 para encerrar): ")

    # Encerrar aplicação.
    if opcao in '0':
        break
    # Escolha.
    elif opcao == '01':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        n1 = str(input("\n1º nome: "))
        n2 = str(input("2º nome: "))
        n3 = str(input("3º nome: "))
        n4 = str(input("4º nome: "))
        lista = [n1, n2, n3, n4]
        escolhido = choice(lista)
        print("\nO escolhido(a) foi {}.".format(escolhido))
    # Envio de e-mail.
    elif opcao == '02':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        dict_1 = {
        'nome': ['nome_1'],
        'email': ['email_1'],
        'enviado': [False]
        }

        dados_1 = {
            'nome': ['Sonia Weber', 'Daryl Lowe', 'Vernon Carroll', 'Basil Gilliam', 'Mechelle Cobb', 'Edan Booker',
                    'Igor Wyatt', 'Ethan Franklin', 'Reed Williamson', 'Price Singleton'],
            'email': ['Lorem.ipsum@cursusvestibulumMauris.com', 'auctor@magnis.org', 'at@magnaUttincidunt.org',
                    'mauris.sagittis@sem.com', 'nec.euismod.in@mattis.co.uk', 'egestas@massaMaurisvestibulum.edu',
                    'semper.auctor.Mauris@Crasdolordolor.edu', 'risus.Quisque@condimentum.com',
                    'Donec@nislMaecenasmalesuada.net', 'Aenean.gravida@atrisus.edu'],
            'enviado': [False, False, False, False, False, False, False, True, False, False]
        }

        dados_2 = {
            'nome': ['Travis Shepherd', 'Hoyt Glass', 'Jennifer Aguirre', 'Cassady Ayers', 'Colin Myers', 'Herrod Curtis',
                    'Cecilia Park', 'Hop Byrd', 'Beatrice Silva', 'Alden Morales'],
            'email': ['at@sed.org', 'ac.arcu.Nunc@auctor.edu', 'nunc.Quisque.ornare@nibhAliquam.co.uk', 'non.arcu@mauriseu.com',
                    'fringilla.cursus.purus@erategetipsum.ca', 'Fusce.fermentum@tellus.co.uk', 'dolor.tempus.non@ipsum.net',
                    'blandit.congue.In@libero.com', 'nec.tempus.mauris@Suspendisse.com', 'felis@urnaconvalliserat.org'],
            'enviado': [False, False, False, True, True, True, False, True, True, False]
        }

        # emails = (dict_1, dados_1, dados_2)
        print(f"\nParâmetros = \033[0;32m{dict_1}\033[m\n")
        print(f"Grupo de Usuários 1 = \033[0;33m{dados_1}\033[m\n")
        print(f"Grupo de Usuários 2 = \033[0;34m{dados_2}\033[m")
    # Emojis.
    elif opcao == '03':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\U0001F917')
        print('\U0001F637')
        print('\U0001F62A')
        print('\U0001F618')
        print('\U0001F600') # rosto sorridente
        print("\U0001f604") # rosto sorridente com olhos sorridentes
        print("\U0001F606") 
        print("\U0001F923") # rolando de rir no chão
        print("\U0001F603") # rosto sorridente com olhos grandes
        print("\U0001F601") # rosto radiante com olhos sorridentes
        print("\U0001F606") # rosto sorridente e vesgo
        print("\U0001F605") # rosto sorridente com suor
        print("\U0001F642") # rosto ligeiramente sorridente
        print("\U0001F602") # rosto com lágrimas de alegria
        print("\U0001F609") # rosto piscando
        print("\U0001F60A") # rosto sorridente com olhos sorridentes
        print("\U0001F607") # rosto sorridente com auréola
        print("\U0001F970") # rosto sorridente com 3 corações	U + 1F970
        print("\U0001F60D") # rosto sorridente com olhos de coração	U + 1F60D
        print("\U0001F929") # atingido por estrelas	U + 1F929
        print("\U0001F618") # cara mandando um beijo	U + 1F618
        print("\U0001F617") # rosto beijando	U + 1F617
        print("\U0001F61A") # rosto com olhos fechados	U + 1F61A
        print("\U0001F619") # beijando rosto com olhos sorridentes	U + 1F619
        print("\U0001F60B") # cara saboreando comida	U + 1F60B
        print("\U0001F61B") # cara com língua	U + 1F61B
        print("\U0001F61C") # rosto piscando com língua	U + 1F61C
        print("\U0001F92A") # cara maluca	U + 1F92A
        print("\U0001F61D") # rosto apertando os olhos com a língua	U + 1F61D
        print("\U0001F911") # cara que fala dinheiro	U + 1F911
        print("\U0001F917") # rosto abraçando	U + 1F917
        print("\U0001F92D") # rosto com mão sobre a boca	U + 1F92D
        print("\U0001F92B") # cara calada	U + 1F92B
        print("\U0001F914") # cara pensativa	U + 1F914
        print("\U0001F928") # cara com boca de zíper	U + 1F910
        print("\U0001F928") # rosto com sobrancelha levantada	U + 1F928
        print("\U0001F610") # rosto neutro	U + 1F610
        print("\U0001F611") # rosto sem expressão	U + 1F611
        print("\U0001F636") # cara sem boca	U + 1F636
        print("\U0001F60F") # rosto sorridente	U + 1F60F
        print("\U0001F612") # rosto não divertido	U + 1F612
        print("\U0001F644") # rosto com olhos revirados	U + 1F644
        print("\U0001F62C") # rosto fazendo careta	U + 1F62C
        print("\U0001F925") # cara mentirosa	U + 1F925
        print("\U0001F60C") # rosto aliviado	U + 1F60C
        print("\U0001F614") # rosto pensativo	U + 1F614
        print("\U0001F62A") # cara de sono	U + 1F62A
        print("\U0001F924") # cara babando	U + 1F924
        print("\U0001F634") # rosto adormecido	U + 1F634
        print("\U0001F637") # rosto com máscara médica	U + 1F637
        print("\U0001F912") # rosto com termômetro	U + 1F912
        print("\U0001F915") # rosto com bandagem na cabeça	U + 1F915
        print("\U0001F922") # rosto nauseado	U + 1F922
        print("\U0001F602") # rosto sorridente com gotas nos olhos
    # Descobrir Número.
    elif opcao == '04':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            print ("\nOlá, vou descobrir o resultado final de acordo com o número que você escolher ;)")
            sleep(5)
            print('Vamos começar!!\n')
            sleep(5)

            print("\033[0;31m--> Escolha um número entre 17 & 77\n")
            sleep(10)

            print ("\033[0;32m--> Acrescente ao número escolhido o valor 7\n")
            sleep(10)

            print ("\033[0;33m--> Agora multiplique essa soma por dois\n")
            sleep(10)

            print ("\033[0;34m--> Agora subtraia o valor 4 dessa soma\n")
            sleep(10)

            print ("\033[0;35m--> Agora divida o resultado por dois\n")
            sleep(10)

            print ("\033[0;36m--> Agora subtraia esse resultado pelo número original escolhido no início\n")
            sleep(10)

            print ("\033[0;37m--> O resultado final que temos é...\n")
            sleep(5)

            print('\033[0;31m--> 5 <--\033[m')

            resp = " "
            while resp not in "10":
                resp = str(input("\nDeseja continuar [1 - SIM / 0 - NÃO]? ")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
        
    # Dissecando Dado.
    elif opcao == '05':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        a = input('\nDigite algo: ')
        print(f'\nO tipo primitivo desse valor é {type(a)}')
        print(f'Só tem espaços? {a.isspace()}')
        print(f'É um número? {a.isnumeric()}')
        print(f'É alfabético? {a.isalpha()}')
        print(f'É alphanumérico? {a.isalnum()}')
        print(f'Está em maiúsculas? {a.isupper()}')
        print(f'Está em minúsculas? {a.islower()}')
        print(f'Esta capitalizado? {a.istitle()}')
        print(f'TODAS MAIÚSCULAS -> {a.upper()}')
        print(f'TODAS MINÚSCULAS -> {a.lower()}')
        print(f'Elimina espaços -> {a.strip()}')
    # Contagem Regressiva.
    elif opcao == '06':
        print('Disponibilizando ferramenta, por favor aguarde...\n')
        sleep(2)
        for cont in range(10, -1, -1):
            print(cont)
            sleep(1)
        print("\nBUM! BUM! POOOOOWW!!!\n")
        for cont in range(4, -1, -1):
            print("#")
            sleep(1)
        print("\nBUM! BUM! POOOOOWW!!!")
    # Classificando Atletas.
    elif opcao == '07':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        atual = date.today().year
        nascimento = int(input("\nAno de Nascimento: "))
        idade = atual - nascimento
        print("\nO atleta tem {} anos.".format(idade))
        if idade <= 9:
            print("Classificação: MIRIM.")
        elif idade <= 14:
            print("Classificação: INFANTIL.")
        elif idade <= 19:
            print("Classificação: JÚNIOR.")
        elif idade <= 25:
            print("Classificação: SÊNIOR.")
        else:
            print("Classificação: MASTER.")
    # Casas decimais.
    elif opcao == '08':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        teste = float(input('\nInforme um número float: '))
        numero = round(teste)

        print('\nO valor de teste formatado é {:.1f}'.format(teste))
        print('O valor de teste formatado é {:.2f}'.format(teste))
        print('O valor de teste formatado é {:.3f}'.format(teste))
        print('O valor de teste formatado é {:.4f}'.format(teste))
        print('O valor de teste formatado é {:.5f}'.format(teste))
        print('O valor de teste formatado é {:.6f}'.format(teste))
        print('O valor de teste formatado é {:.7f}'.format(teste))
        print('O valor de teste formatado é {:.8f}'.format(teste))
        print('O valor de teste formatado é {:.9f}'.format(teste))
        print('O valor de teste formatado é {:.10f}'.format(teste))
        print()
        print(numero)
    # Contar semanas.
    elif opcao == '09':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Aqui vai o programa principal!
            ano = 365
            semana = 7
            contsemanas = ano / semana
            print('\nUm ano contém {} semanas.'.format(contsemanas))

            a = int(input('\nAnos: '))
            resultado = a * contsemanas

            print(resultado)
            print('\n{} ano(s) possuem {} semanas.'.format(a, resultado))
            numero = round(resultado)
            print('{} ano(s) possuem {} semanas.'.format(a, numero))
            resultado = '{0:,}'.format(numero).replace(',','.') #Aqui coloca os pontos
            print(resultado, 'semanas.')
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\n\033[0;33mDeseja continuar contando semanas [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar a contagem de semanas!\033[m")
    # Calendário.
    elif opcao == '10':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            print("\n\033[0;33mDigite 0 para imprimir o calendário do ano atual ou informe o ano desejado.\033[m\n")
            ano = int(input("\033[0;32m> "))
            print('\033[m')
            if ano == 0:
                ano_atual = date.today().year
                print(calendar.calendar(ano_atual))   
            else:
                print(calendar.calendar(ano))
            resp = " "
            while resp not in "10":
                resp = str(input("Deseja continuar [1 - SIM / 0 - NÃO]? ")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar o gerador de calendário!\033[m")
    # Cadastro de Trabalhador.
    elif opcao == '11':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        dados = dict()
        dados['Nome'] = str(input('Nome: '))
        nasc = int(input('Ano de Nascimento: '))
        dados['Idade'] = datetime.now().year - nasc
        dados['CTPS'] = int(input('Carteira de Trabalho: (0 não tem): '))
        if dados['CTPS'] != 0:
            dados['Contratacao'] = int(input('Ano de Contratação: '))
            dados['Salário'] = float(input('Salário: R$ '))
            dados['Aposentadoria'] = dados['Idade'] + ((dados['Contratacao'] + 35) - datetime.now().year)
        print('-=' * 30)
        for k, v in dados.items():
            print(f' -> {k}: {v}.')
    # Sistema de hotel para animais de estimação.
    elif opcao == '12':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        atual = date.today().year
        nasc = int(input("\nAno de Nascimento: "))
        idade = atual - nasc
        print("\nQuem nasceu em {} tem {} anos em {}.".format(nasc, idade, atual))
        if idade == 18:
            print("Você tem que se alistar IMEDIATAMENTE!")
        elif idade < 18:
            saldo = 18 - idade
            print("\nVocê ainda não tem 18 anos. Ainda faltam {} ano(s) para o alistamento.".format(saldo))
            ano = atual + saldo
            print("Seu alistamento será em {}.".format(ano))
        else:
            saldo = idade - 18
            print("\nVocê já deveria ter se alistado a {} anos.".format(saldo))
            ano = atual - saldo
            print("Seu alistamento foi em {}.".format(ano))
    # Analisador Completo.
    elif opcao == '13':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        somaidade = 0
        mediaidade = 0
        maioridadehomem = 0
        nomevelho = ""
        totmulher20 = 0

        for p in range(1, 5):
            print("------ {}ª PESSOA ------".format(p))
            nome = str(input("Nome: ")).strip()
            idade = int(input("Idade: "))
            sexo = str(input("Sexo [M/F]: ")).strip()
            somaidade = somaidade + idade

            if p == 1 and sexo in "Mn":
                maioridadehomem = idade
                nomevelho = nome
            if sexo in "Mn" and idade > maioridadehomem:
                maioridadehomem = idade
                nomevelho = nome
            if sexo in "Ff" and idade > 20:
                totmulher20 += 1

        mediaidade = somaidade / 4

        print("\nA média de idade do grupo é de {} anos.".format(mediaidade))
        print(f"\nO homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}.")
        print("\nAo todo são {} mulheres com menos de 20 anos.\n".format(totmulher20))
    # Analisando Triângulo.
    elif opcao == '14':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        # Analisando Triângulo v1.0.
        print("\nAnalisador de Triângulos")
        r1 = float(input("\n1º segmento: "))
        r2 = float(input("2º segmento: "))
        r3 = float(input("3º segmento: "))

        if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
            print("\nOs segmentos acima \033[0;32mPODEM FORMAR\033[m um triângulo!\n")
        else:
            print("\nOs segmentos \033[0;31mNÃO PODEM FORMAR\033[m triângulo!\n")

        # Analisando Triângulos v2.0.
        print("-=" * 20)
        print("Analisador de Triângulos")
        r1 = float(input("\nDigite o 1º segmento: "))
        r2 = float(input("Digite o 2º segmento: "))
        r3 = float(input("Digite o 3º segmento: "))

        if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
            print("Os segmentos acima PODEM FORMAR um triângulo = ", end="")
            if r1 == r2 == r3:
                print("EQUILÁTERO!")
            elif r1 != r2 != r3 != r1:
                print("ESCALENO!")
            else:
                print("ISÓSCELES!")
        else:
            print("Os segmentos NÃO PODEM FORMAR triângulo!")
    # Análise Completa de Nome.
    elif opcao == '15':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Aqui vai o programa principal!
            n = str(input("\nDigite seu nome completo: ")).strip()
            print("\nAnalisando seu nome...")
            sleep(3)
            print()
            print("Seu nome em letras maiúsculas é {}.".format(n.upper()))
            print("Seu nome em letras minúsculas é {}.".format(n.lower()))
            print("Seu nome tem {} letras.".format(len(n)-n.count(" ")))
            print("Seu primeiro nome tem {} letras.".format(n.find(" ")))
            separa = n.split()
            print("Seu primeiro nome é {} e tem {} letras.".format(separa[0], len(separa[0])))
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\n\033[0;33mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Análise de Dados.
    elif opcao == '16':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\nANÁLISE DE DADOS DO GRUPO')

        tot18 = toth = totm20 = 0

        while True:

            idade = int(input("\nIdade: "))
            
            sexo = " "
            while sexo not in "MF":
                sexo = str(input("Sexo [M/F]? ")).strip().upper()[0]
            if idade >= 18:
                tot18 = tot18 + 1
            if sexo == "M":
                toth = toth + 1
            if sexo == "F" and idade < 20:
                totm20 = totm20 + 1    
            resp = " "
            while resp not in "SN":
                resp = str(input("\nQuer continuar [S/N]? ")).strip().upper()[0]
            if resp == "N":
                break

        print(f"\nTotal de pessoas com mais de 18 anos: {tot18}.")
        print(f"Total de homens cadastrados: {toth}.")
        print(f"Total de mulheres com menos de 20 anos cadastradas: {totm20}.")

        print('\nANÁLISE DE DADOS - V1.0')

        n = input("\n\033[0;33mDigite algo: \033[m").strip()

        print("\n\033[0;36mAnalisando informações...\033[m")
        sleep(3)
        print(f"Informação digitada = \033[0;32m{n}\033[m")
        print(f"Total de caracteres com espaços = \033[0;32m{len(n)}\033[m")
        print("Total de caracteres sem espaços = \033[0;32m{}\033[m".format(len(n)-n.count(" ")))
        # print("\nEspaços = \033[0;32m{}\033[m".format(len(" ")-n.count(" ")))
        totpalavras = n.split()
        print(f"Total de palavras = \033[0;32m{len(totpalavras)}\033[m")
        palavras = n.upper()
        print(f"Maiúsculas = \033[0;32m{palavras}\033[m")
        print("Maiúsculas: \033[0;32m{}\033[m".format(n.upper()))
        print("Minúsculas: \033[0;32m{}\033[m".format(n.lower()))
        print("A primeira composição tem \033[0;32m{}\033[m caractere(s)".format(n.find(" ")))
        separa = n.split()
        print("A primeira composição de caracteres é \033[0;32m{}\033[m e tem \033[0;32m{}\033[m caracteres".format(separa[0], len(separa[0])))

        print('\nANÁLISE DE DADOS EM UMA TUPLA')
        num = (int(input("\nDigite um número: ")),
                int(input("Digite outro número: ")),
                int(input("Digite mais um número: ")),
                int(input("Digite o último número: ")))
        print(f"\nVocê digitou os valores {num}")
        print(f"\nO valor 9 apareceu {num.count(9)} vezes.")
        if 3 in num:
            print(f"\nO valor 3 apareceu na {num.index(3)+1}ª posição.")
        else:
            print("O valor 3 não foi digitado em nenhuma posição.")
        print("Os valores pares digitados foram: ",end="")
        for n in num:
            if n % 2 == 0:
                print(n, end=" ")
    # Análise de Unidades.
    elif opcao == '17':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        num = int(input("\nInforme um número: "))
        u = num // 1 % 10
        d = num // 10 % 10
        c = num // 100 % 10
        m = num // 1000 % 10
        dm = num // 10000 % 10
        cm = num // 100000 % 10
        # print("\nAnalisando o número {}.".format(num))
        resultado = '{0:,}'.format(num).replace(',','.') #Aqui coloca os pontos
        print("\nAnalisando o número \033[0;31m{}\033[m.".format(resultado))
        sleep(3)
        print("\nUnidade: {}.".format(u))
        print("Dezena: {}.".format(d))
        print("Centena: {}.".format(c))
        print("Milhar: {}.".format(m))
        print("Dezena de Milhar: {}.".format(dm))
        print("Centena de Milhar: {}.".format(cm))

        print('\nSendo obrigatório uso de 4 dígitos ou mais!')
        numero = int(input("Informe um número: "))
        n = str(num)
        print("\nAnalisando o número \033[0;32m{}\033[m.".format(resultado))
        sleep(3)
        print("\nUnidade: {}.".format(n[3]))
        print("Dezena: {}.".format(n[2]))
        print("Centena: {}.".format(n[1]))
        print("Milhar: {}.".format(n[0]))
    # Análise de Letra Específica.
    elif opcao == '18':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        frase = str(input("\nDigite uma frase: ")).upper().strip()
        print("\nA letra A aparece {} vezes na frase.".format(frase.count("A")))
        print("A primeira letra A apareceu na posição {}.".format(frase.find("A")+1))
        print("A útima letra A apareceu na posição {}.".format(frase.rfind("A")+1))
    # Ano Bissexto.
    elif opcao == '19':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            print("\nDigite 999 para analisar o ano atual.\n")
            ano = int(input("Ou informe o ano a ser analisado: "))
            if ano == 999:
                ano = date.today().year
            if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
                print("\nO ano {} é BISSEXTO.".format(ano))
            else:
                print("\nO ano {} NÃO É BISSEXTO.".format(ano))
            resp = " "
            while resp not in "10":
                resp = str(input("\n\033[0;33mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Data & Hora Atual.
    elif opcao == '20':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        # Data atual.
        print('\nSolução I.')
        data_e_hora_atuais = datetime.now()
        data_e_hora_em_texto = data_e_hora_atuais.strftime("%d/%m/%Y")
        print('Em instantes você verá a data atual...')
        sleep(3)
        print(f'\033[0;33mA data atual é {data_e_hora_em_texto}.\033[m')
        # Hora atual.
        hora_atual = dt.datetime.now()
        hora_atual = hora_atual.strftime("%H hora(s) %M minuto(s) %S segundo(s) & %M milésimo(s) de segundo(s).")
        print('\nem seguida você verá a hora atual...')
        sleep(3)
        print(f"\033[0;32mA hora atual é {hora_atual}\033[m")
        # Data e hora atual.
        print('\nSolução II.')
        from datetime import datetime, time
        data_e_hora_atuais = datetime.now()
        data_e_hora_em_texto = data_e_hora_atuais.strftime("\033[0;32mDia %d/%m/%Y - %H hora(s) %M minuto(s) %S segundo(s) & %M milésimo(s) de segundo(s).\033[m")
        print('Agora você verá a data e hora atual juntas...')
        sleep(3)
        print('Segue data e hora atual = ', data_e_hora_em_texto)
        # Obter o dia da semana, mês, dia, hora e ano.
        from datetime import datetime
        import time
        print('\nSolução III.')
        print('Agora você verá dia da semana, mês, dia, hora e ano....')
        sleep(3)
        A = time.ctime()
        A = A.split()
        A
        ['Tue', 'Oct', '29', '12:38:44', '2019']
        print(f'\n\033[0;32m{A}\033[m')
    # Cores em Python.
    elif opcao == '21':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('''
        Cores no Python

        # Style                  Text               Back
        #   0 - nenhum            30 - branco        40 - branco
        #   1 - Negrito           31 - vermelho      41 - vermelho
        #   4 - Sublinhado        32 - verde         42 - verde
        #   7 - Negativo          33 - amarelo       43 - amarelo
        #                         34 - azul          44 - azul
        #                         35 - roxo          45 - roxo
        #                         36 - celeste       46 - celeste   
        #                         37 - cinza         47 - cinza
        ''')

        print("\n\033[0;31m Olá Mundo!\n") # Vermelho
        print("\033[0;32m Olá Mundo!\n") # Verde
        print("\033[0;33m Olá Mundo!\n") # Amarelo
        print("\033[0;34m Olá Mundo!\n") # Roxo
        print("\033[0;35m Olá Mundo!\n") # Rosa
        print("\033[0;36m Olá Mundo!\n") # Anil
        print("\033[0;37m Olá Mundo!\n") # Branco

        print('\n                    ◉     Cores de Letra     ◉                    \n')
        print('\033[30mPreto')
        print('\033[31mVermelho')
        print('\033[32mVerde')
        print('\033[33mAmarelo')
        print('\033[34mRoxo')
        print('\033[35mRosa')
        print('\033[36mAnil')
        print('\033[37mCinza')
        print('\033[38mBranco')

        print('\n                    ◉     Cores de Fundo     ◉                    \n')
        print('\033[40mPreto')
        print('\033[41mRosa')
        print('\033[42mVerde Claro')
        print('\033[43mAmarelo')
        print('\033[44mRoxo')
        print('\033[45mRosa')
        print('\033[46mCyano')
        print('\033[47mBranco\033[m')
    # Agenda.
    elif opcao == '22':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        #-*- coding: cp1252 -*-                     #
            # ------------------------------------------#
            # Agenda eletronica em Python.              #
            # @autor: Jhonathan Paulo Banczek           #
            # data:05/09/2010                           #
            # ------------------------------------------#

        #------------------------------------------------------------------------------#


        #--------------------GLOBAL--------------------#
        lista = [] #define uma variavel para a lista

        #le os dados do arquivo e joga pra lista

        arq2 = open("agenda.csv","a+")
        lista = arq2.readlines()
        arq2.close()
        #-----------------------------------------------#
            

        #------------------------------------------------------------------------------#

        #fun��o: menu, constroi o menu

        def menu():
            print("\n", "=" * 50)
            print("""\nAGENDA ELETRÔNICA\n\n
                        Escolha a opção: \n
                        1 -  INSERIR CONTATO\n
                        2 -  DELETAR\n
                        3 -  MOSTRAR AGENDA\n
                        4 -  FINALIZAR PROGRAMA\n""")
            
        #fim da fun��o menu



        #------------------------------------------------------------------------------#
            
        #fun��o: lista_agenda, adiciona, remove e mostra a lista
            
        def lista_agenda(nome, data, opc):

            if( opc == 1):
                contato = nome + " - " + data + "\n" #concatenao o 'nome' ';' e 'data'
                lista.append(contato)
                lista.sort() #ordena a lista por prioridade

            elif (opc == 2):
                print("=" * 30)
                if ( lista == []): #se lista for vazia
                    print("Lista Vazia\n")
                else:
                    lista.pop(0)#remove o elemento de maior prioridade, ou seja, indice 0 da lista
                    print("Removido o elemento de maior prioridade")
                print("=" * 30)

            elif (opc == 3):
                print("=" * 30)
                if (lista == []):
                    print("Lista vazia!")
                else:
                    print("Nome & Data de Nascimento: \n")
                    for i in lista:
                        print(i)
                print("=" * 30)

            elif (opc == 4):
                arq = open("agenda.csv","w") #escreve por cima do arquivo antigo (atualiza lista)
                tam = len(lista) #recebe o tamanho da lista
                #for que insere os valores no arquivo separado por ';' sendo nome = indice par e data = impar

                for i in range(tam):
                    arq.write(lista[i])

                arq.close()

        #fim da fun��o lista_agenda


                
        #------------------------------------------------------------------------------#
        #funcao principal


        opc = 0 #variavel pro menu

        while (opc != 4 ):

            menu() #chama o menu

            while True:
                try:
                    opc = int(input('> ')) #recebe a op��o
                    break
                except:
                    print("ERRO, digite só números válidos!")

            if ( opc == 1 ):
                print("\nInforme o nome do contato.")
                nome = input('> ')

                print("\ninforme a data de nascimento.")
                data = input('> ')

                lista_agenda(nome, data, 1) #chama a fun��o para inserir na lista

            elif ( opc == 2):
                lista_agenda(0,0,2) #chama a fun��o para deletar o nome na lista

            elif (opc == 3): #chama a fun��o para mostrar na tela
                print("Lista de contatos: ")
                lista_agenda(0,0,3)
                        

        lista_agenda(0,0,4) #grava a lista na agenda
        print("\nFIM DO PROGRAMA! ")

        #------------------------------------------------------------------------------#
        #fim
    # Cadastro de Jogador.
    elif opcao == '23':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        jogador = dict()
        partidas = list()
        jogador['Nome'] = str(input('\nNome do Jogador: '))
        tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
        for c in range(0, tot):
            partidas.append(int(input(f' Quantos gols na partida {c+1}? ')))
        jogador['gols'] = partidas[:]
        jogador['total'] = sum(partidas)
        print('-=' * 30)
        print(jogador)
        print('-=' * 30)
        for k, v in jogador.items():
            print(f'O campo {k} tem o valor {v}.')
        print('-=' * 30)
        print(f'O jogador {jogador["Nome"]} jogou {len(jogador["gols"])} partidas.')
        for i, v in enumerate(jogador['gols']):
            print(f'=> Na partida {i+1}, fez {v} gols.')
        print(f'Foi um total de {jogador["total"]} gols.')
    # Ficha do Jogador.
    elif opcao == '24':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        def ficha(jog='desconhecido', gol=0):
            print(f'\nO jogador {jog} fez {gol} gol(s) no campeonato.')
        # Programa principal
        n = str(input('\nNome do Jogador: '))
        g = str(input('Número de Gols: '))
        if g.isnumeric():
            g = int(g)
        else:
            g = 0
        if n.strip() == '':
            ficha(gol=g)
        else:
            ficha(n, g)



















    # 
    elif opcao == '25':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;31mA ferramenta escolhida não possui algoritmo!\033[m')
    # 
    elif opcao == '26':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;31mA ferramenta escolhida não possui algoritmo!\033[m')
    # 
    elif opcao == '27':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;31mA ferramenta escolhida não possui algoritmo!\033[m')
    # 
    elif opcao == '28':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;31mA ferramenta escolhida não possui algoritmo!\033[m')
    # 
    elif opcao == '29':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;31mA ferramenta escolhida não possui algoritmo!\033[m')
    # 
    elif opcao == '30':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;31mA ferramenta escolhida não possui algoritmo!\033[m')
    






















        


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