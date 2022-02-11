from time import sleep

while True:
    # Programa principal!
    print('''
                ALFABETO

    [ 01 ] - \033[0;32mA\033[m          [ 14 ] - \033[0;32mN\033[m
    [ 02 ] - \033[0;32mB\033[m          [ 15 ] - \033[0;32mO\033[m
    [ 03 ] - \033[0;32mC\033[m          [ 16 ] - \033[0;32mP\033[m
    [ 04 ] - \033[0;32mD\033[m          [ 17 ] - \033[0;32mQ\033[m
    [ 05 ] - \033[0;32mE\033[m          [ 18 ] - \033[0;32mR\033[m
    [ 06 ] - \033[0;32mF\033[m          [ 19 ] - \033[0;32mS\033[m
    [ 07 ] - \033[0;32mG\033[m          [ 20 ] - \033[0;32mT\033[m
    [ 08 ] - \033[0;32mH\033[m          [ 21 ] - \033[0;32mU\033[m
    [ 09 ] - \033[0;32mI\033[m          [ 22 ] - \033[0;32mV\033[m
    [ 10 ] - \033[0;32mJ\033[m          [ 23 ] - \033[0;32mW\033[m
    [ 11 ] - \033[0;32mK\033[m          [ 24 ] - \033[0;32mX\033[m
    [ 12 ] - \033[0;32mL\033[m          [ 25 ] - \033[0;32mY\033[m
    [ 13 ] - \033[0;32mM\033[m          [ 26 ] - \033[0;32mZ\033[m
    ''')

    letra = str(input("Informe a letra que deseja exibir (0 para encerrar): "))

    # Encerrar aplicação.
    if letra in '0':
        break
    # A
    elif letra == '01':
        print('Disponibilizando, por favor aguarde...')
        sleep(2)
        print('\n')
        for row in range(7):
            for col in range(5):
                if (row==0) and (col in {1,2,3}):
                    print("\033[0;32m*\033[m", end=" ")
                elif (row in {1,2,3,4,5,6}) and (col in {0,4}):
                    print("\033[0;32m*\033[m", end=" ")
                elif row==3:
                    print("\033[0;32m*\033[m", end=" ")
                else:
                    print(" ", end=" ")
            print()
    # B
    elif letra == '02':
        print('Disponibilizando, por favor aguarde...')
        sleep(2)
        print()
        for row in range(7):
            for col in range(5):
                if (row in {0, 3, 6}) and (col in {0, 1, 2, 3}):
                    print("*", end=" ")
                elif (row in {1, 2, 4, 5}) and (col in {0, 4}):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    # C
    elif letra == '03':
        print('Disponibilizando, por favor aguarde...')
        sleep(2)
        print()
        for row in range(7):
            for col in range(5):
                if (row in {0, 6}) and (col in {1, 2, 3}):
                    print("*", end=" ")
                elif (row in {1, 5}) and (col in {0, 4}):
                    print("*", end=" ")
                elif (row in {2, 3, 4}) and (col == 0):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    # D
    elif letra == '04':
        print('Disponibilizando, por favor aguarde...')
        sleep(2)
        print()
        for row in range(7):
            for col in range(5):
                if (row in {0, 6}) and (col in {0, 1, 2, 3}):
                    print("*", end=" ")
                elif (row in {1, 2, 3, 4, 5}) and (col in {0, 4}):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
















    # E
    elif letra == '05':
        print('Disponibilizando, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
    # F
    elif letra == '06':
        print('Disponibilizando, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
    # G
    elif letra == '07':
        print('Disponibilizando, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
    # H
    elif letra == '08':
        print('Disponibilizando, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
    # I
    elif letra == '09':
        print('Disponibilizando, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
    # J
    elif letra == '10':
        print('Disponibilizando, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
    # K
    elif letra == '11':
        print('Disponibilizando, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
    # L
    elif letra == '12':
        print('Disponibilizando, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
    # M
    elif letra == '13':
        print('Disponibilizando, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
    # N
    elif letra == '14':
        print('Disponibilizando, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
    # O
    elif letra == '15':
        print('Disponibilizando, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
    # P
    elif letra == '16':
        print('Disponibilizando, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
    # Q
    elif letra == '17':
        print('Disponibilizando, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
    # R
    elif letra == '18':
        print('Disponibilizando, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
    # S
    elif letra == '19':
        print('Disponibilizando, por favor aguarde...')
        sleep(2)
        print()
        for row in range(7):
            for col in range(5):
                if (row in {0,3,6}) and (col in {1,2,3}):
                    print("*", end=" ")
                elif (row in {1,5}) and (col in {0,4}):
                    print("*", end=" ")
                elif (row == 2) and (col == 0):
                    print("*", end=" ")
                elif (row == 4) and (col == 4):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    # T
    elif letra == '20':
        print('Disponibilizando, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
    # U
    elif letra == '21':
        print('Disponibilizando, por favor aguarde...')
        sleep(2)
        print()
        for row in range(7):
            for col in range(5):
                if (row != 6) and (col in {0,4}):
                    print("*", end=" ")
                elif (row == 6) and (col in {1,2,3}):
                    print("*", end= " ")
                else:
                    print(" ", end=" ")
            print()
    # V
    elif letra == '22':
        print('Disponibilizando, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
    # W
    elif letra == '23':
        print('Disponibilizando, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
    # X
    elif letra == '24':
        print('Disponibilizando, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
    # Y
    elif letra == '25':
        print('Disponibilizando, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
    # Z
    elif letra == '26':
        print('Disponibilizando, por favor aguarde...')
        sleep(2)
        print(
'''
* * * * * * * * 
            *   
          *     
        *       
      *         
    *           
  *             
* * * * * * * * 
'''
)
    else:
        # Aqui vai o "Tente novamente!"
        letra != '01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26'
        print("\n\033[0;31mInformação incorreta, tente novamente.\033[m\n", end=" ")
        continue
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\n\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break    
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")