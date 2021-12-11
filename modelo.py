# Semáforo.

while True:

    # Seu código vai aqui...
    # Programa principal!
    print('\nSemáforo.')
    print('\nInforme uma das três cores de um semáforo ou pressione 999 a qualquer momento para encerrar.')
    # cor = input('\nCor (ou pressione 999 para encerrar): ')
    cor = input('\n> ')
    if cor in '999':
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