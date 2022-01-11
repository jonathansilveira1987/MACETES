# Games.

from time import sleep
from datetime import date
import datetime as dt
from random import randint
import random
from random import choice

while True:
    # Programa principal!
    print('''\033[0;33m
                GAMES
    Escolha abaixo o jogo desejado...

    [ 01 ] - Jogo da Adivinhação
    [ 02 ] - Sorteio aleatório
    [ 03 ] - Sortear aluno
    [ 04 ] - 
    [ 05 ] - 
    \033[0m''')

    opcao = input("Informe sua escolha desejada (0 para encerrar): ")
    
    # Encerrar aplicação.
    if opcao in '0':
        break
    # Jogo da Adivinhação.
    elif opcao == '01':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Aqui vai o programa principal!
            computador = randint(0, 10)
            print("\nSou seu computador... Acabei de pensar em um número entre 0 e 10.")
            sleep(3)
            print("Será que você consegue adivinhar qual foi? ")
            sleep(3)
            acertou = False
            palpites = 0
            while not acertou:
                jogador = int(input("\nQual é o seu palpite? "))
                palpites += 1
                if jogador == computador:
                    acertou = True
                else:
                    if jogador < computador:
                        print("\nMais... Tente mais uma vez.")
                    elif jogador > computador:
                        print("\nMenos... Tente mais uma vez.")
            print("\n\033[0;32mAcertou com {} tentativas. Parabéns!\033[m".format(palpites))
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\n\033[0;33mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # 
    elif opcao == '02':
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
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")








    # 
    elif opcao == '03':
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






    elif opcao == '04':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
    elif opcao == '05':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')






















        
    else:
        # Aqui vai o "Tente novamente!"
        opcao != '01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20'
        print("\n\033[0;31mInformação incorreta, tente novamente.\033[m\n", end=" ")
        continue
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\n\033[0;34mDeseja continuar no programa principal [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")