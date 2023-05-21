def menu():
    ano = int(input('\nDigite o ano desejado: '))
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print('\nBissexto')
    else:
        print('\nNão é bissexto')
while True:
    menu()