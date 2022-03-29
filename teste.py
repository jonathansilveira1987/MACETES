a = 80000
b = 200000
ano = 0
while a <= b:
	a += a * 0.03
	b += b * 0.015
	ano += 1
taxaanualcrescimentoA = 80000 * 0.03
habitantesmes = taxaanualcrescimentoA / 12
print(f'\n\033[0;32mO crescimento habitacional do país A é de {int(habitantesmes)} habitantes por mês e {int(taxaanualcrescimentoA)} habitantes por ano.\033[m')
taxaanualcrescimentoB = 200000 * 0.015
habitantesmes = taxaanualcrescimentoB / 12
print(f'\033[0;33mO crescimento habitacional do país B é de {int(habitantesmes)} habitantes por mês e {int(taxaanualcrescimentoB)} habitantes por ano.\033[m')
print ( "\n\033[0;31mDados os valores acima o país A ultrapassa ou iguala o país B em %d anos!\033[m\n" %ano )