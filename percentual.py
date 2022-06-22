from time import sleep

byte = 8
print()
# Modo Manual.
# 10. Brontobyte.
brontobyte = 1 * 1024
byte = 10 ** 27
bit = (10 ** 27) * 8
print('Calculando...')
sleep(3)
print("\033[0;32m\n-> 1 Brontobyte possui {0:,} YottaBytes.\033[m".format(brontobyte).replace(",", "."))
sleep(3)
print("\033[0;33m-> 1 Brontobyte possui {0:,} Bytes.\033[m".format(byte).replace(",", "."))
sleep(3)
print("\033[0;34m-> 1 Brontobyte possui {0:,} Bits.\033[m\n".format(bit).replace(",", "."))
sleep(3)
print("Abaixo segue número lido por extenso...")
sleep(3)
print("\033[0;31m8 octilhões de bits.\033[m\n")
# 11. Geopbyte.
geopbyte = 1 * 1024
byte = 10 ** 30
bit = (10 ** 30) * 8
print('Calculando...')
sleep(3)
print("\033[0;32m\n-> 1 Geopbyte possui {0:,} Brontobytes.\033[m".format(geopbyte).replace(",", "."))
sleep(3)
print("\033[0;33m-> 1 Geopbyte possui {0:,} Bytes.\033[m".format(byte).replace(",", "."))
sleep(3)
print("\033[0;34m-> 1 Geopbyte possui {0:,} Bits.\033[m\n".format(bit).replace(",", "."))
sleep(3)
print("Abaixo segue número lido por extenso...")
sleep(3)
print("\033[0;31m8 nonilhões de bits.\033[m\n")





# Modo Automático.
# 9. Brontobyte

print('Calculando...')
b1 = 10 ** 27
b1r = '{0:,}'.format(b1).replace(',','.') # Aqui coloca os pontos
brontobyte = byte * b1
b2r = '{0:,}'.format(brontobyte).replace(',','.') # Aqui coloca os pontos
sleep(2)
print(f'\n\033[0;33m1 Brontobyte equivale a {b1r} Bytes.')
sleep(2)
print(f'\033[0;32m1 Brontobyte equivale a {b2r} Bits.\n')


print()