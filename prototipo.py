from time import sleep

while True:
    
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

    unidade = int(input("Informe a unidade desejada: "))

    # Byte.
    if unidade == 1:
        byte = 8 * 1
        print('Calculando...')
        sleep(3)
        print("\n1 Byte possui {} bits.\n".format(byte))
    # KiloByte.
    if unidade == 2:
        kilobyte = 1 * 1024
        bit = (2 ** 10) * 8
        print('Calculando...')
        sleep(3)
        print("\n-> 1 Kilobyte possui {0:,} Bytes.".format(kilobyte).replace(",", "."))
        sleep(3)
        print("-> 1 Kilobyte possui {0:,} Bits.\n".format(bit).replace(",", "."))
        sleep(3)
        print("Abaixo segue número lido por extenso...")
        sleep(3)
        print("8 mil .192 bits.\n")
    # MegaByte.
    if unidade == 3:
        megabyte = 1 * 1024
        byte = 2 ** 20
        bit = (2 ** 20) * 8
        print('Calculando...')
        sleep(3)
        print("\n-> 1 Megabyte possui {0:,} Kilobytes.".format(megabyte).replace(",", "."))
        sleep(3)
        print("-> 1 Megabyte possui {0:,} Bytes.".format(byte).replace(",", "."))
        sleep(3)
        print("-> 1 Megabyte possui {0:,} Bits.\n".format(bit).replace(",", "."))
        sleep(3)
        print("Abaixo segue número lido por extenso...")
        sleep(3)
        print("8 milhões .388 mil .608 bits.\n")
    # GigaByte.
    if unidade == 4:
        gigabyte = 1 * 1024
        byte = 2 ** 30
        bit = (2 ** 30) * 8
        print('Calculando...')
        sleep(3)
        print("\n-> 1 GigaByte possui {0:,} MegaBytes.".format(gigabyte).replace(",", "."))
        sleep(3)
        print("-> 1 GigaByte possui {0:,} Bytes.".format(byte).replace(",", "."))
        sleep(3)
        print("-> 1 GigaByte possui {0:,} Bits.\n".format(bit).replace(",", "."))
        sleep(3)
        print("Abaixo segue número lido por extenso...")
        sleep(3)
        print("8 bilhões .589 milhões .934 mil .592 bits.\n")
    # TeraByte.
    if unidade == 5:
        terabyte = 1 * 1024
        byte = 2 ** 40
        bit = (2 ** 40) * 8
        print('Calculando...')
        sleep(3)
        print("\n-> 1 TeraByte possui {0:,} GigaBytes.".format(terabyte).replace(",", "."))
        sleep(3)
        print("-> 1 TeraByte possui {0:,} Bytes.".format(byte).replace(",", "."))
        sleep(3)
        print("-> 1 TeraByte possui {0:,} Bits.\n".format(bit).replace(",", "."))
        sleep(3)
        print("Abaixo segue número lido por extenso...")
        sleep(3)
        print("8 trilhões .796 bilhões .093 milhões .022 mil .208 bits.\n")
    # PetaByte.
    if unidade == 6:
        petabyte = 1 * 1024
        byte = 2 ** 50
        bit = (2 ** 50) * 8
        print('Calculando...')
        sleep(3)
        print("\n-> 1 PetaByte possui {0:,} TeraBytes.".format(petabyte).replace(",", "."))
        sleep(3)
        print("-> 1 PetaByte possui {0:,} Bytes.".format(byte).replace(",", "."))
        sleep(3)
        print("-> 1 PetaByte possui {0:,} Bits.\n".format(bit).replace(",", "."))
        sleep(3)
        print("Abaixo segue número lido por extenso...")
        sleep(3)
        print("9 quatrilhões .007 trilhões .199 bilhões .254 milhões .740 mil .992 bits.\n")
    # 7. ExaByte
    if unidade == 7:
        exabyte = 1 * 1024
        byte = 2 ** 60
        bit = (2 ** 60) * 8
        print('Calculando...')
        sleep(3)
        print("\n-> 1 ExaByte possui {0:,} PetaBytes.".format(exabyte).replace(",", "."))
        sleep(3)
        print("-> 1 ExaByte possui {0:,} Bytes.".format(byte).replace(",", "."))
        sleep(3)
        print("-> 1 ExaByte possui {0:,} Bits.\n".format(bit).replace(",", "."))
        sleep(3)
        print("Abaixo segue número lido por extenso...")
        sleep(3)
        print("9 quintilhões .223 quatrilhões .372 trilhões .036 bilhões .854 milhões .775 mil .808 bits.\n")
    # 8. ZettaByte
    if unidade == 8:
        zettabyte = 1 * 1024
        byte = 2 ** 70
        bit = (2 ** 70) * 8
        print('Calculando...')
        sleep(3)
        print("\n-> 1 ZettaByte possui {0:,} ExaBytes.".format(zettabyte).replace(",", "."))
        sleep(3)
        print("-> 1 ZettaByte possui {0:,} Bytes.".format(byte).replace(",", "."))
        sleep(3)
        print("-> 1 ZettaByte possui {0:,} Bits.\n".format(bit).replace(",", "."))
        sleep(3)
        print("Abaixo segue número lido por extenso...")
        sleep(3)
        print("9 sextilhões .444 quintilhões .732 quatrilhões .965 trilhões .739 bilhões .290 milhões .427 mil .392 bits.\n")
    # 9. YottaByte
    if unidade == 9:
        yottabyte = 1 * 1024
        byte = 2 ** 80
        bit = (2 ** 80) * 8
        print('Calculando...')
        sleep(3)
        print("\n-> 1 YottaByte possui {0:,} ZettaBytes.".format(yottabyte).replace(",", "."))
        sleep(3)
        print("-> 1 YottaByte possui {0:,} Bytes.".format(byte).replace(",", "."))
        sleep(3)
        print("-> 1 YottaByte possui {0:,} Bits.\n".format(bit).replace(",", "."))
        sleep(3)
        print("Abaixo segue número lido por extenso...")
        sleep(3)
        print("9 septilhões .671 sextilhões .406 quintilhões .556 quatrilhões .917 trilhões .033 bilhões .397 milhôes .649 mil .408 bits.\n")
    
    resp = " "
    while resp not in "10":
        resp = str(input("\nDeseja continuar [1 - SIM / 0 - NÃO]? ")).strip().upper()[0]
    if resp == "0":
        break
    
print("\nVocê optou por finalizar!\n")