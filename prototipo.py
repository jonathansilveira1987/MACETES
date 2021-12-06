# Semáforo.

while True:
    # Programa principal!
    print('\nSemáforo.')
    cor = input('\nCor: ')
    if cor == 'verde':
                print('\n\033[0;32mAcelerar!\033[m\n')
    elif cor == 'amarelo':
                print('\n\033[0;33mAtenção!\033[m\n')
    elif cor == 'vermelho':
                print('\n\033[0;31mPare!\033[m\n')
    else:
        # Aqui vai o "Tente novamente!"
        cor != 'verde' 'amarelo' 'vermelho'
        print("\n\033[0;31mValor incorreto, tente novamente.\033[m\n", end=" ")
        continue
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\n\033[0;33mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break    
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")