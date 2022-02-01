# Operações Matemáticas 2.0.

from time import sleep

while True:
    # Programa principal!
    print('''\033[0;33m
            OPERAÇÕES MATEMÁTICAS
    Escolha abaixo a ferramenta desejada...

    [ 01 ] - Custo de viagem                                                 [ 21 ] - 
    [ 02 ] -                                                                 [ 21 ] - 
    [ 03 ] -                                                                 [ 21 ] - 
    [ 04 ] -                                                                 [ 21 ] - 
    [ 05 ] -                                                                 [ 21 ] - 
    [ 06 ] -                                                                 [ 21 ] - 
    [ 07 ] -                                                                 [ 21 ] - 
    [ 08 ] -                                                                 [ 21 ] - 
    [ 09 ] -                                                                 [ 21 ] - 
    [ 10 ] -                                                                 [ 21 ] - 
    [ 11 ] -                                                                 [ 21 ] - 
    [ 12 ] -                                                                 [ 21 ] - 
    [ 13 ] -                                                                 [ 21 ] - 
    [ 14 ] -                                                                 [ 21 ] - 
    [ 15 ] -                                                                 [ 21 ] - 
    [ 16 ] -                                                                 [ 21 ] - 
    [ 17 ] -                                                                 [ 21 ] - 
    [ 18 ] -                                                                 [ 21 ] - 
    [ 19 ] -                                                                 [ 21 ] - 
    [ 20 ] -                                                                 [ 21 ] - 
    \033[0m''')

    opcao = input("Informe sua escolha desejada (0 para encerrar): ")
    
    # Encerrar aplicação.
    if opcao in '0':
        break
    # Custo de Viagem.
    elif opcao == '01':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Programa principal!
            print('''
Escolha o modo de confecção da porção inteira. 
[ 1 ] - Utilizando "ESCREVA"
[ 2 ] - Utilizando "SE" simplificado / hífen line / operador ternário
''')

            modo = input("Informe o modo desejado (0 para encerrar): ")

            # Encerrar aplicação.
            if modo in '0':
                break
            elif modo == '1':
                # Utilizando "ESCREVA".
                distancia = float(input("\n\033[0;32mDigite a distância da sua viagem: "))
                print("\nVocê está prestes a começar uma viagem de {} km.".format(distancia))
                if distancia <= 200:
                    preco = distancia * 0.50
                else:
                    preco = distancia * 0.45
                print("O preço de sua passagem será de R$ {:.2f}\033[m".format(preco))

            elif modo == '2':
                # Utilizando "SE" simplificado / hífen line / operador ternário.
                distancia = float(input("\n\033[0;33mDigite a distânica da sua viagem: "))
                print("\nVocê está prestes a começar uma viagem de {} km.".format(distancia))
                preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
                print("O preço de sua passagem será de R$ {:.2f}\033[m".format(preco))
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\nContinuar [1 - SIM / 0 - NÃO]? ")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")







    # 
    elif opcao == '02':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;31mA ferramenta escolhida não possui algoritmo!\033[m')
    # 
    elif opcao == '03':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;31mA ferramenta escolhida não possui algoritmo!\033[m')
    # 
    elif opcao == '04':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;31mA ferramenta escolhida não possui algoritmo!\033[m')
    # 
    elif opcao == '05':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;31mA ferramenta escolhida não possui algoritmo!\033[m')
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