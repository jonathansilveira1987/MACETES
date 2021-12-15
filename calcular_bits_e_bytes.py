# Calcular bits e bytes. Versão 1.0.

from time import sleep

while True:
    # Programa principal!
    print('''\nBIT é a menor unidade de medida computacional!
    1 BIT equivale a 1 caractere.\n
    Escolha uma unidade abaixo para saber quantos bits a mesma possui...\n 
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

    unidade = input("Informe a unidade desejada (0 para encerrar): ")

    # Encerrar aplicação.
    if unidade in '0':
        break
    # Byte.
    elif unidade == '1':
        byte = 8 * 1
        print('Calculando...')
        sleep(3)
        print("\033[0;32m\n1 Byte possui {} bits.\033[m\n".format(byte))
    # KiloByte.
    elif unidade == '2':
        kilobyte = 1 * 1024
        bit = (2 ** 10) * 8
        print('Calculando...')
        sleep(3)
        print("\033[0;32m\n-> 1 Kilobyte possui {0:,} Bytes.\033[m".format(kilobyte).replace(",", "."))
        sleep(3)
        print("\033[0;33m-> 1 Kilobyte possui {0:,} Bits.\033[m\n".format(bit).replace(",", "."))
        sleep(3)
        print("Abaixo segue número lido por extenso...")
        sleep(3)
        print("\033[0;31m8 mil .192 bits.\033[m\n")
    # MegaByte.
    elif unidade == '3':
        megabyte = 1 * 1024
        byte = 2 ** 20
        bit = (2 ** 20) * 8
        print('Calculando...')
        sleep(3)
        print("\033[0;32m\n-> 1 Megabyte possui {0:,} Kilobytes.\033[m".format(megabyte).replace(",", "."))
        sleep(3)
        print("\033[0;33m-> 1 Megabyte possui {0:,} Bytes.\033[m".format(byte).replace(",", "."))
        sleep(3)
        print("\033[0;34m-> 1 Megabyte possui {0:,} Bits.\033[m\n".format(bit).replace(",", "."))
        sleep(3)
        print("Abaixo segue número lido por extenso...")
        sleep(3)
        print("\033[0;31m8 milhões .388 mil .608 bits.\033[m\n")
    # GigaByte.
    elif unidade == '4':
        gigabyte = 1 * 1024
        byte = 2 ** 30
        bit = (2 ** 30) * 8
        print('Calculando...')
        sleep(3)
        print("\033[0;32m\n-> 1 GigaByte possui {0:,} MegaBytes.\033[m".format(gigabyte).replace(",", "."))
        sleep(3)
        print("\033[0;33m-> 1 GigaByte possui {0:,} Bytes.\033[m".format(byte).replace(",", "."))
        sleep(3)
        print("\033[0;34m-> 1 GigaByte possui {0:,} Bits.\033[m\n".format(bit).replace(",", "."))
        sleep(3)
        print("Abaixo segue número lido por extenso...")
        sleep(3)
        print("\033[0;31m8 bilhões .589 milhões .934 mil .592 bits.\033[m\n")
    # TeraByte.
    elif unidade == '5':
        terabyte = 1 * 1024
        byte = 2 ** 40
        bit = (2 ** 40) * 8
        print('Calculando...')
        sleep(3)
        print("\033[0;32m\n-> 1 TeraByte possui {0:,} GigaBytes.\033[m".format(terabyte).replace(",", "."))
        sleep(3)
        print("\033[0;33m-> 1 TeraByte possui {0:,} Bytes.\033[m".format(byte).replace(",", "."))
        sleep(3)
        print("\033[0;34m-> 1 TeraByte possui {0:,} Bits.\033[m\n".format(bit).replace(",", "."))
        sleep(3)
        print("Abaixo segue número lido por extenso...")
        sleep(3)
        print("\033[0;31m8 trilhões .796 bilhões .093 milhões .022 mil .208 bits.\033[m\n")
    # PetaByte.
    elif unidade == '6':
        petabyte = 1 * 1024
        byte = 2 ** 50
        bit = (2 ** 50) * 8
        print('Calculando...')
        sleep(3)
        print("\033[0;32m\n-> 1 PetaByte possui {0:,} TeraBytes.\033[m".format(petabyte).replace(",", "."))
        sleep(3)
        print("\033[0;33m-> 1 PetaByte possui {0:,} Bytes.\033[m".format(byte).replace(",", "."))
        sleep(3)
        print("\033[0;34m-> 1 PetaByte possui {0:,} Bits.\033[m\n".format(bit).replace(",", "."))
        sleep(3)
        print("Abaixo segue número lido por extenso...")
        sleep(3)
        print("\033[0;31m9 quatrilhões .007 trilhões .199 bilhões .254 milhões .740 mil .992 bits.\033[m\n")
    # 7. ExaByte
    elif unidade == '7':
        exabyte = 1 * 1024
        byte = 2 ** 60
        bit = (2 ** 60) * 8
        print('Calculando...')
        sleep(3)
        print("\033[0;32m\n-> 1 ExaByte possui {0:,} PetaBytes.\033[m".format(exabyte).replace(",", "."))
        sleep(3)
        print("\033[0;33m-> 1 ExaByte possui {0:,} Bytes.\033[m".format(byte).replace(",", "."))
        sleep(3)
        print("\033[0;34m-> 1 ExaByte possui {0:,} Bits.\033[m\n".format(bit).replace(",", "."))
        sleep(3)
        print("Abaixo segue número lido por extenso...")
        sleep(3)
        print("\033[0;31m9 quintilhões .223 quatrilhões .372 trilhões .036 bilhões .854 milhões .775 mil .808 bits.\033[m\n")
    # 8. ZettaByte
    elif unidade == '8':
        zettabyte = 1 * 1024
        byte = 2 ** 70
        bit = (2 ** 70) * 8
        print('Calculando...')
        sleep(3)
        print("\033[0;32m\n-> 1 ZettaByte possui {0:,} ExaBytes.\033[m".format(zettabyte).replace(",", "."))
        sleep(3)
        print("\033[0;33m-> 1 ZettaByte possui {0:,} Bytes.\033[m".format(byte).replace(",", "."))
        sleep(3)
        print("\033[0;34m-> 1 ZettaByte possui {0:,} Bits.\033[m\n".format(bit).replace(",", "."))
        sleep(3)
        print("Abaixo segue número lido por extenso...")
        sleep(3)
        print("\033[0;31m9 sextilhões .444 quintilhões .732 quatrilhões .965 trilhões .739 bilhões .290 milhões .427 mil .392 bits.\033[m\n")
    # 9. YottaByte
    elif unidade == '9':
        yottabyte = 1 * 1024
        byte = 2 ** 80
        bit = (2 ** 80) * 8
        print('Calculando...')
        sleep(3)
        print("\033[0;32m\n-> 1 YottaByte possui {0:,} ZettaBytes.\033[m".format(yottabyte).replace(",", "."))
        sleep(3)
        print("\033[0;33m-> 1 YottaByte possui {0:,} Bytes.\033[m".format(byte).replace(",", "."))
        sleep(3)
        print("\033[0;34m-> 1 YottaByte possui {0:,} Bits.\033[m\n".format(bit).replace(",", "."))
        sleep(3)
        print("Abaixo segue número lido por extenso...")
        sleep(3)
        print("\033[0;31m9 septilhões .671 sextilhões .406 quintilhões .556 quatrilhões .917 trilhões .033 bilhões .397 milhôes .649 mil .408 bits.\033[m\n")
    else:
        # Aqui vai o "Tente novamente!"
        unidade != '1, 2, 3, 4, 5, 6, 7, 8, 9'
        print("\n\033[0;31mInformação incorreta, tente novamente.\033[m\n", end=" ")
        continue
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break    
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")





























































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

        unidade = input("Informe a unidade desejada (0 para encerrar): ")

        # Encerrar aplicação.
        if unidade in '0':
            break
        # Byte.
        elif unidade == '1':
            print(f'1 Byte equivale a {byte} Bits.\n')
        # KiloByte
        elif unidade == '2':
            b1 = 2 ** 10
            b1r = '{0:,}'.format(b1).replace(',','.') # Aqui coloca os pontos
            kilobyte = byte * b1
            b2r = '{0:,}'.format(kilobyte).replace(',','.') # Aqui coloca os pontos
            print(f'\n1 KiloByte equivale a {b1r} Bytes.')
            print(f'1 KiloByte equivale a {b2r} Bits.\n')
        # MegaByte.
        elif unidade == '3':
            b1 = 2 ** 20
            b1r = '{0:,}'.format(b1).replace(',','.') # Aqui coloca os pontos
            megabyte = byte * b1
            b2r = '{0:,}'.format(megabyte).replace(',','.') # Aqui coloca os pontos
            print(f'\n1 MegaByte equivale a {b1r} Bytes.')
            print(f'1 MegaByte equivale a {b2r} Bits.\n')

        # GigaByte.
        elif unidade == '4':
            b1 = 2 ** 30
            b1r = '{0:,}'.format(b1).replace(',','.') # Aqui coloca os pontos
            gigabyte = byte * b1
            b2r = '{0:,}'.format(gigabyte).replace(',','.') # Aqui coloca os pontos
            print(f'\n1 GigaByte equivale a {b1r} Bytes.')
            print(f'1 GigaByte equivale a {b2r} Bits.\n')
        # TeraByte.
        elif unidade == '5':
            b1 = 2 ** 40
            b1r = '{0:,}'.format(b1).replace(',','.') # Aqui coloca os pontos
            terabyte = byte * b1
            b2r = '{0:,}'.format(terabyte).replace(',','.') # Aqui coloca os pontos
            print(f'\n1 TeraByte equivale a {b1r} Bytes.')
            print(f'1 TeraByte equivale a {b2r} Bits.\n')
        # PetaByte.
        elif unidade == '6':
            b1 = 2 ** 50
            b1r = '{0:,}'.format(b1).replace(',','.') # Aqui coloca os pontos
            petabyte = byte * b1
            b2r = '{0:,}'.format(petabyte).replace(',','.') # Aqui coloca os pontos
            print(f'\n1 PetaByte equivale a {b1r} Bytes.')
            print(f'1 PetaByte equivale a {b2r} Bits.\n')
        # ExaByte.
        elif unidade == '7':
            b1 = 2 ** 60
            b1r = '{0:,}'.format(b1).replace(',','.') # Aqui coloca os pontos
            exabyte = byte * b1
            b2r = '{0:,}'.format(exabyte).replace(',','.') # Aqui coloca os pontos
            print(f'\n1 ExaByte equivale a {b1r} Bytes.')
            print(f'1 ExaByte equivale a {b2r} Bits.\n')
        # ZettaByte.
        elif unidade == '8':
            b1 = 2 ** 70
            b1r = '{0:,}'.format(b1).replace(',','.') # Aqui coloca os pontos
            zettabyte = byte * b1
            b2r = '{0:,}'.format(zettabyte).replace(',','.') # Aqui coloca os pontos
            print(f'\n1 ZettaByte equivale a {b1r} Bytes.')
            print(f'1 ZettaByte equivale a {b2r} Bits.\n')
        # YottaByte.
        elif unidade == '9':
            b1 = 2 ** 80
            b1r = '{0:,}'.format(b1).replace(',','.') # Aqui coloca os pontos
            yottabyte = byte * b1
            b2r = '{0:,}'.format(yottabyte).replace(',','.') # Aqui coloca os pontos
            print(f'\n1 YottaByte equivale a {b1r} Bytes.')
            print(f'1 YottaByte equivale a {b2r} Bits.\n')
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

















'''


# Byte.
byte = 8

# KiloByte
b1 = 2 ** 10
b1r = '{0:,}'.format(b1).replace(',','.') # Aqui coloca os pontos
print(f'\n1 KiloByte equivale a {b1r} Bytes.')
kilobyte = byte * b1
b1r = '{0:,}'.format(kilobyte).replace(',','.') # Aqui coloca os pontos
print(f'1 KiloByte equivale a {b1r} Bits.\n')

# MegaByte.
b2 = 2 ** 20
b2r = '{0:,}'.format(b2).replace(',','.') # Aqui coloca os pontos
print(f'1 MegaByte equivale a {b2r} Bytes.')
megabyte = byte * b2
b2r = '{0:,}'.format(megabyte).replace(',','.') # Aqui coloca os pontos
print(f'1 MegaByte equivale a {b2r} Bits.\n')

# GigaByte.
b3 = 2 ** 30
b3r = '{0:,}'.format(b3).replace(',','.') # Aqui coloca os pontos
print(f'1 GigaByte equivale a {b3r} Bytes.')
gigabyte = byte * b3
b3r = '{0:,}'.format(gigabyte).replace(',','.') # Aqui coloca os pontos
print(f'1 GigaByte equivale a {b3r} Bits.\n')

# TeraByte.
b4 = 2 ** 40
b4r = '{0:,}'.format(b4).replace(',','.') # Aqui coloca os pontos
print(f'1 TeraByte equivale a {b4r} Bytes.')
terabyte = byte * b4
b4r = '{0:,}'.format(terabyte).replace(',','.') # Aqui coloca os pontos
print(f'1 TeraByte equivale a {b4r} Bits.\n')

# PetaByte.
b5 = 2 ** 50
b5r = '{0:,}'.format(b5).replace(',','.') # Aqui coloca os pontos
print(f'1 PetaByte equivale a {b5r} Bytes.')
petabyte = byte * b5
b5r = '{0:,}'.format(petabyte).replace(',','.') # Aqui coloca os pontos
print(f'1 PetaByte equivale a {b5r} Bits.\n')

# ExaByte.
b6 = 2 ** 60
b6r = '{0:,}'.format(b6).replace(',','.') # Aqui coloca os pontos
print(f'1 ExaByte equivale a {b6r} Bytes.')
exabyte = byte * b4
b6r = '{0:,}'.format(exabyte).replace(',','.') # Aqui coloca os pontos
print(f'1 ExaByte equivale a {b6r} Bits.\n')

# ZettaByte.
b7 = 2 ** 70
b7r = '{0:,}'.format(b7).replace(',','.') # Aqui coloca os pontos
print(f'1 ZettaByte equivale a {b7r} Bytes.')
zettabyte = byte * b7
b7r = '{0:,}'.format(zettabyte).replace(',','.') # Aqui coloca os pontos
print(f'1 ZettaByte equivale a {b7r} Bits.\n')

# YottaByte.
b8 = 2 ** 80
b8r = '{0:,}'.format(b8).replace(',','.') # Aqui coloca os pontos
print(f'1 YottaByte equivale a {b8r} Bytes.')
yottabyte = byte * b8
b8r = '{0:,}'.format(yottabyte).replace(',','.') # Aqui coloca os pontos
print(f'1 YottaByte equivale a {b8r} Bits.\n')






































1 Byte = 8 bits
1 Kilobyte (KB) = 1024 bytes
1 Megabyte (MB) = 1024 kilobytes
1 Gigabyte (GB) = 1024 megabytes
1 Terabyte (TB) = 1024 gigabytes
1 Petabyte (PB) = 1024 terabytes
1 Exabyte (EB) = 1024 petabytes
1 Zettabyte (ZB) = 1024 exabytes
1 Yottabyte (YB) = 1024 zettabytes

Unidade	    Símbolo	           Número de bytes
byte        BYTE    2^0 
kilobyte	KB      2^10    =  1024 bytes
megabyte	MB	    2^20    =  1,048,576 bytes
gigabyte	GB	    2^30    =  1,073,741,824 bytes
terabyte	TB	    2^40    =  1,099,511,627,776 bytes
petabyte	PB	    2^50    =  1,125,899,906,842,624 bytes
exabyte	    EB	    2^60    =  1,152,921,504,606,846,976 bytes
zettabyte	ZB	    2^70    =  1,180,591,620,717,411,303,424 bytes
yottabyte	YB	    2^80    =  1,208,925,819,614,629,174,706,176 bytes

# Uso do método replace.
a = 2 ** 80
resultado = '{0:,}'.format(a).replace(',','.') # Aqui coloca os pontos
print(resultado)

'''