from time import sleep

byte = 8

# Modo Manual.
# 9. YottaByte

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



# Modo Automático.
# 9. YottaByte

print('Calculando...')
b1 = 2 ** 80
b1r = '{0:,}'.format(b1).replace(',','.') # Aqui coloca os pontos
yottabyte = byte * b1
b2r = '{0:,}'.format(yottabyte).replace(',','.') # Aqui coloca os pontos
sleep(2)
print(f'\n\033[0;33m1 YottaByte equivale a {b1r} Bytes.')
sleep(2)
print(f'\033[0;32m1 YottaByte equivale a {b2r} Bits.\n')