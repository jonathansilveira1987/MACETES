# Semáforo.

while True:    
    # Programa principal!
    print('\nSemáforo.')

    cor = input('\nCor: ')

    while True:
    # Aqui vai o "Tente novamente!"
    
        if cor == 'verde' 'vermelho' 'amarelo':
            break
        print("\n\033[0;31mERRO! Informação incorreta, digite verde, vermelho ou amarelo.\033[m\n", end=" ")
    
    
    
    
        if cor == 'verde':
            print('\n\033[0;32mAcelerar\033[m')
        if cor == 'amarelo':
            print('\n\033[0;33mAtenção\033[m')
        else:
            print('\n\033[0;31mParar\033[m')
    

        # Aqui vai o "Deseja continuar?"
        resp = " "
        while resp not in "10":
            resp = str(input("\nDeseja continuar [1 - SIM / 0 - NÃO]? ")).strip().upper()[0]
        if resp == "0":
            break
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")