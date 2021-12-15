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
print(f'1 TeraByte equivale a {b3r} Bytes.')
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



'''

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














































































# Semáforo.

while True:


    # Programa principal.
    print('\nSemáforo.')
    cor = input('\nInforme uma das três cores de um semáforo (0 para encerrar): ')
    
    
    # Encerrar aplicação.
    if cor in '0':
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