# Calcular bits e bytes. Versão 2.0.

from time import sleep

byte = 8

while True:
    try:
        # Programa principal!
        print('''\nBIT é a menor unidade de medida computacional!
    1 BIT equivale a 1 caractere.\n
    Escolha uma unidade abaixo para saber quantos bits & bytes a mesma possui...\n 
    [ 1 ] - Byte
    [ 2 ] - KiloByte
    [ 3 ] - MegaByte
    [ 4 ] - GigaByte
    [ 5 ] - TeraByte
    [ 6 ] - PetaByte
    [ 7 ] - ExaByte
    [ 8 ] - ZettaByte
    [ 9 ] - YottaByte
    ''')

        unidade = input("Informe a unidade desejada (0 ou ENTER para encerrar): ")

        # Encerrar aplicação.
        if unidade in '0':
            break
        # Byte.
        elif unidade == '1':
            print('Calculando...')
            sleep(2)
            print(f'\n\033[0;32m1 Byte equivale a {byte} Bits.\033[m\n')
        # KiloByte
        elif unidade == '2':
            print('Calculando...')
            b1 = 2 ** 10
            b1r = '{0:,}'.format(b1).replace(',','.') # Aqui coloca os pontos
            kilobyte = byte * b1
            b2r = '{0:,}'.format(kilobyte).replace(',','.') # Aqui coloca os pontos
            sleep(2)
            print(f'\n\033[0;33m1 KiloByte equivale a {b1r} Bytes.\033[m')
            sleep(2)
            print(f'\033[0;32m1 KiloByte equivale a {b2r} Bits.\033[m\n')
        # MegaByte.
        elif unidade == '3':
            print('Calculando...')
            b1 = 2 ** 20
            b1r = '{0:,}'.format(b1).replace(',','.') # Aqui coloca os pontos
            megabyte = byte * b1
            b2r = '{0:,}'.format(megabyte).replace(',','.') # Aqui coloca os pontos
            sleep(2)
            print(f'\n\033[0;33m1 MegaByte equivale a {b1r} Bytes.')
            sleep(2)
            print(f'\033[0;32m1 MegaByte equivale a {b2r} Bits.\n')
        # GigaByte.
        elif unidade == '4':
            print('Calculando...')
            b1 = 2 ** 30
            b1r = '{0:,}'.format(b1).replace(',','.') # Aqui coloca os pontos
            gigabyte = byte * b1
            b2r = '{0:,}'.format(gigabyte).replace(',','.') # Aqui coloca os pontos
            sleep(2)
            print(f'\n\033[0;33m1 GigaByte equivale a {b1r} Bytes.')
            sleep(2)
            print(f'\033[0;32m1 GigaByte equivale a {b2r} Bits.\n')
        # TeraByte.
        elif unidade == '5':
            print('Calculando...')
            b1 = 2 ** 40
            b1r = '{0:,}'.format(b1).replace(',','.') # Aqui coloca os pontos
            terabyte = byte * b1
            b2r = '{0:,}'.format(terabyte).replace(',','.') # Aqui coloca os pontos
            sleep(2)
            print(f'\n\033[0;33m1 TeraByte equivale a {b1r} Bytes.')
            sleep(2)
            print(f'\033[0;32m1 TeraByte equivale a {b2r} Bits.\n')
        # PetaByte.
        elif unidade == '6':
            print('Calculando...')
            b1 = 2 ** 50
            b1r = '{0:,}'.format(b1).replace(',','.') # Aqui coloca os pontos
            petabyte = byte * b1
            b2r = '{0:,}'.format(petabyte).replace(',','.') # Aqui coloca os pontos
            sleep(2)
            print(f'\n\033[0;33m1 PetaByte equivale a {b1r} Bytes.')
            sleep(2)
            print(f'\033[0;32m1 PetaByte equivale a {b2r} Bits.\n')
        # ExaByte.
        elif unidade == '7':
            print('Calculando...')
            b1 = 2 ** 60
            b1r = '{0:,}'.format(b1).replace(',','.') # Aqui coloca os pontos
            exabyte = byte * b1
            b2r = '{0:,}'.format(exabyte).replace(',','.') # Aqui coloca os pontos
            sleep(2)
            print(f'\n\033[0;33m1 ExaByte equivale a {b1r} Bytes.')
            sleep(2)
            print(f'\033[0;32m1 ExaByte equivale a {b2r} Bits.\n')
        # ZettaByte.
        elif unidade == '8':
            print('Calculando...')
            b1 = 2 ** 70
            b1r = '{0:,}'.format(b1).replace(',','.') # Aqui coloca os pontos
            zettabyte = byte * b1
            b2r = '{0:,}'.format(zettabyte).replace(',','.') # Aqui coloca os pontos
            sleep(2)
            print(f'\n\033[0;33m1 ZettaByte equivale a {b1r} Bytes.')
            sleep(2)
            print(f'\033[0;32m1 ZettaByte equivale a {b2r} Bits.\n')
        # YottaByte.
        elif unidade == '9':
            print('Calculando...')
            b1 = 2 ** 80
            b1r = '{0:,}'.format(b1).replace(',','.') # Aqui coloca os pontos
            yottabyte = byte * b1
            b2r = '{0:,}'.format(yottabyte).replace(',','.') # Aqui coloca os pontos
            sleep(2)
            print(f'\n\033[0;33m1 YottaByte equivale a {b1r} Bytes.')
            sleep(2)
            print(f'\033[0;32m1 YottaByte equivale a {b2r} Bits.\n')
        else:
            # Aqui vai o "Tente novamente!"
            unidade != '1, 2, 3, 4, 5, 6, 7, 8, 9'
            print("\n\033[0;31mInformação incorreta, tente novamente.\033[m\n", end=" ")
            continue
    except ValueError:
        print("\n\033[0;31mERRO! Informação incorreta, tente novamente.\033[m\n", end=" ")
        continue
# Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break    
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")