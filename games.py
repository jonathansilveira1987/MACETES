# Games.

from time import sleep
from datetime import date
import datetime as dt
from random import randint
from random import randint
from time import sleep
from operator import itemgetter

while True:
    # Programa principal!
    print('''\033[0;33m
                GAMES
    Escolha abaixo o game desejado...

    [ 01 ] - Jogo da Adivinhação
    [ 02 ] - GAME: Pedra Papel e Tesoura
    [ 03 ] - Jogo da Adivinhação
    [ 04 ] - Jogo de dados
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
    # GAME: Pedra Papel e Tesoura.
    elif opcao == '02':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        itens = ("Pedra", "Papel", "Tesoura")
        computador = randint(0, 2)
        print('''
Sua opção:
[ 0 ] - PEDRA.
[ 1 ] - PAPEL.
[ 2 ] - TESOURA.''')
        jogador = int(input("\nQual é a sua jogada? "))
        print("JO")
        sleep(1)
        print("KEN")
        sleep(1)
        print("PO!!!!!!")
        print("-=" * 15)
        print("Computador jogou: {}.".format(itens[computador]))
        print("Jogador jogou: {}.".format(itens[computador]))
        # print("O computador escolheu: {}".format(itens[computador]))
        print("-=" * 15)
        # Computador jogou PEDRA.
        if computador == 0:
            if jogador == 0:
                print("\nEMPATE!")
            elif jogador == 1:
                print("\nJOGADOR VENCE!")
            elif jogador == 2:
                print("\nCOMPUTADOR VENCE!")
            else:
                print("\nJOGADA INVÁLIDA!")
        # Computador jogou PAPEL
        elif computador == 1:
            if jogador == 0:
                print("\nCOMPUTADOR VENCE!")
            elif jogador == 1:
                print("\nEMPATE!")
            elif jogador == 2:
                print("\nJOGADOR VENCE!")
            else:
                print("\nJOGADA INVÁLIDA!")
        # Computador jogou TESOURA
        elif computador == 2:
            if jogador == 0:
                print("\nJOGADOR VENCE!")    
            elif jogador == 1:
                print("\nCOMPUADOR VENCE!")
            elif jogador == 2:
                print("\nEMPATE!")
            else:
                print("\nJOGADA INVÁLIDA!")
    # Jogo da Adivinhação.
    elif opcao == '03':
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
    # Jogo de dados.
    elif opcao == '04':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        jogo = {"Jogador 1": randint(1, 6),
        "Jogador 2": randint(1, 6),
        "Jogador 3": randint(1, 6),
        "Jogador 4": randint(1, 6),}
        ranking = list()
        print("\nValores Sorteados: ")
        for k, v in jogo.items():
            print(f"{k} tirou {v} no dado.")
            sleep(1)
        ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
        print("-=" * 30)
        print("== RANKING DOS JOGADORES ==")
        for i, v in enumerate(ranking):
            print(f"{i+1}º lugar: {v[0]} com {v[1]}.")






    #
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