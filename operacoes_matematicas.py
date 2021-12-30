# Operações Matemáticas.

from time import sleep
import math

while True:
    # Programa principal!
    print('''
            OPERAÇÕES MATEMÁTICAS
    Escolha abaixo a ferramenta desejada...

    [ 01 ] - Calculadora                [ 11 ] - 
    [ 02 ] -                            [ 12 ] - 
    [ 03 ] -                            [ 13 ] - 
    [ 04 ] -                            [ 14 ] - 
    [ 05 ] -                            [ 15 ] - 
    [ 06 ] -                            [ 16 ] - 
    [ 07 ] -                            [ 17 ] - 
    [ 08 ] -                            [ 18 ] - 
    [ 09 ] -                            [ 19 ] - 
    [ 10 ] -                            [ 20 ] - 
    
    ''')
    opcao = input("Informe sua escolha desejada (0 para encerrar): ")
    # Encerrar aplicação.
    if opcao in '0':
        break
    # Calculadora.
    elif opcao == '01':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            operador = input('''
+   para Adição
-   para Subtração
*   para Multiplicação
/   para Divisão

Informe a operação matemática desejada (0 para encerrar): ''')
            if operador == "+":
                num1 = float(input('Valor 1: '))
                num2 = float(input('Valor 2: '))
                soma = num1 + num2
                print(f'\033[0;32m{num1} + {num2} = {soma}.\033[m')
            elif operador == "-":
                num1 = float(input('Valor 1: '))
                num2 = float(input('Valor 2: '))
                diferenca = num1 - num2
                print(f'\033[0;32m{num1} - {num2} = {diferenca}.\033[m')
            elif operador == "*":
                num1 = float(input('Valor 1: '))
                num2 = float(input('Valor 2: '))
                produto = num1 * num2
                print(f'\033[0;32m{num1} * {num2} = {produto}.\033[m')
            elif operador == "/":
                num1 = float(input('Valor 1: '))
                num2 = float(input('Valor 2: '))
                if num2 == 0:
                    print("Divisor não pode ser zero")
                    continue
                produto = num1 / num2
                print(f'\033[0;32m{num1} / {num2} = {produto}.\033[m')
            elif operador == "0":
                break
            else:
                print("\n\033[0;31mOperação inválida, tente novamente!\033[m")



















    # 
    elif opcao == '02':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
    # 
    elif opcao == '03':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
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
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
    # 
    elif opcao == '10':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
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