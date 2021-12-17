# Arredondamento de números.

while True:
    # Programa principal!
    n = int(input('\nNúmero/Base: '))
    p = int(input('Potência/Expoente: '))
    resultado = n ** p
    # Fórmulas.
    print('\n{}'.format(round(resultado, 1)))
    print("\n{0:.50f}\n".format(round(resultado)))
    result = resultado = '{0:,}'.format(resultado).replace(',','.') #Aqui coloca os pontos
    print(result, '\n')
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break    
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")