from time import sleep

byte = 8

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




print('''


escala	escala		notação	prefixo	símbolo
curta	longa		científica	SI*	SI*
um	um	1	100		
mil	mil	1000	103	quilo	k
milhão	milhão	1 000 000	106	mega	M
bilhão	mil milhões	1 000 000 000	109	giga	G
trilião	bilião	1 000 000 000 000	1012	tera	T
quatrilhão	mil biliões	1 000 000 000 000 000	1015	peta	p
quintilhão	trilião	1 000 000 000 000 000 000	1018	exa	E
sextilhão	mil triliões	1 000 000 000 000 000 000 000	1021	zetta	Z
setilhão	quatrilião	1 000 000 000 000 000 000 000 000	1024	yota	Y
octilhão	mil quatriliões	1 000 000 000 000 000 000 000 000 000	1027		
nonilhão	quintilião	1 000 000 000 000 000 000 000 000 000 000	1030		
decilhão	mil quintiliões	1 000 000 000 000 000 000 000 000 000 000 000	1033		
undecilhão	sextilião	1 000 000 000 000 000 000 000 000 000 000 000 000	1036		
dodecilhão	mil sextiliões	1 000 000 000 000 000 000 000 000 000 000 000 000 000	1039		
tredecilhão	septilião	1 000 000 000 000 000 000 000 000 000 000 000 000 000 000	1042		




''')