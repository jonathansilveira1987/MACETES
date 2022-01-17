# Soma ímpares múltiplos de três.
soma = input('Informe um valor inicial: ')
cont = input('Informe um valor final: ')
for c in range(soma, cont, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print("\nA soma de todos os {} valores solicitados é {}.\n".format(cont, soma))




'''
# Soma ímpares múltiplos de três.
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print("\nA soma de todos os {} valores solicitados é {}.\n".format(cont, soma))


'''