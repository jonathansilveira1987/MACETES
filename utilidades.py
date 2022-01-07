# Utilidades 1.0.

from time import sleep

while True:
    # Programa principal!
    print('''
    Pacote de Ferramentas!
    Escolha abaixo a ferramenta desejada...\n
    [ 01 ] - Apresentação                       [ 11 ] - 
    [ 02 ] - Imprimir na tela                   [ 12 ] - 
    [ 03 ] - Olá Mundo!                         [ 13 ] - 
    [ 04 ] -                                    [ 14 ] - 
    [ 05 ] -                                    [ 15 ] - 
    [ 06 ] -                                    [ 16 ] - 
    [ 07 ] -                                    [ 17 ] - 
    [ 08 ] -                                    [ 18 ] - 
    [ 09 ] - Detector de palíndromo             [ 19 ] - 
    [ 10 ] - Semáforo                           [ 20 ] - 
    ''')

    opcao = input("Informe sua escolha desejada (0 para encerrar): ")

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
        print("\nVocê optou por finalizar!\n")
        # (Obs. Esse foi meu codigo usando cores e outras coisas, mas o que vai resolver é 
        # colocar o TRY, e o if dentro dele. Caso o usuario digite outra coisa, o EXCEPT VALUEERROR 
        # vai resolver mostrando um print.







    # 
    elif opcao == '04':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
    # 
    elif opcao == '05':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
    # 
    elif opcao == '06':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
    # 
    elif opcao == '07':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
    # 
    elif opcao == '08':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
    # 
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
    # 
    elif opcao == '11':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
    # 
    elif opcao == '12':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
    # 
    elif opcao == '13':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
    # 
    elif opcao == '14':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
    # 
    elif opcao == '15':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
    # 
    elif opcao == '16':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
    # 
    elif opcao == '17':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
    # 
    elif opcao == '18':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
    # 
    elif opcao == '19':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
    # 
    elif opcao == '20':
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