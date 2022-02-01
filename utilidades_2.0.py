# Utilidades 2.0.

from time import sleep
from random import choice

while True:
    # Programa principal!
    print('''
                            PACOTE DE FERRAMENTAS
    [ 01 ] - Escolha                                [ 26 ] - 
    [ 02 ] - Envio de e-mail                        [ 26 ] - 
    [ 03 ] - Emojis                                 [ 26 ] - 
    [ 04 ] - Descobrir número                       [ 26 ] - 
    [ 05 ] - Dissecando dado                        [ 26 ] - 
    [ 06 ] -                                        [ 26 ] - 
    [ 07 ] -                                        [ 26 ] - 
    [ 08 ] -                                        [ 26 ] - 
    [ 09 ] -                                        [ 26 ] - 
    [ 10 ] -                                        [ 26 ] - 
    [ 11 ] -                                        [ 26 ] - 
    [ 12 ] -                                        [ 26 ] - 
    [ 13 ] -                                        [ 26 ] - 
    [ 14 ] -                                        [ 26 ] - 
    [ 15 ] -                                        [ 26 ] - 
    [ 16 ] -                                        [ 26 ] - 
    [ 17 ] -                                        [ 26 ] - 
    [ 18 ] -                                        [ 26 ] - 
    [ 19 ] -                                        [ 26 ] - 
    [ 20 ] -                                        [ 26 ] - 
    [ 21 ] -                                        [ 26 ] - 
    [ 22 ] -                                        [ 26 ] - 
    [ 23 ] -                                        [ 26 ] - 
    [ 24 ] -                                        [ 26 ] - 
    [ 25 ] -                                        [ 26 ] - 
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
    # 
    elif opcao == '06':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;31mA ferramenta escolhida não possui algoritmo!\033[m')
    # 
    elif opcao == '07':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;31mA ferramenta escolhida não possui algoritmo!\033[m')
    # 
    elif opcao == '08':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;31mA ferramenta escolhida não possui algoritmo!\033[m')
    # 
    elif opcao == '09':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;31mA ferramenta escolhida não possui algoritmo!\033[m')
    # 
    elif opcao == '10':
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