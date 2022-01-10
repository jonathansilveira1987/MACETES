# Games.

from time import sleep
from datetime import date
import datetime as dt
from random import randint

while True:
    # Programa principal!
    print('''\033[0;33m
                GAMES
    Escolha abaixo o jogo desejado...

    [ 01 ] - Jogo da Adivinhação
    [ 02 ] - 
    [ 03 ] - 
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
    elif opcao == '02':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
    elif opcao == '03':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
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