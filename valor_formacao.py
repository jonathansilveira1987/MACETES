while True:
    # Aqui vai o programa principal!
    valor_formacao = float(input('\nInforme o valor total da formação R$: '))
    # Diário.
    diario_1 = valor_formacao / 365
    diario_2 = valor_formacao / 730
    diario_3 = valor_formacao / 1095
    diario_4 = valor_formacao / 1460
    diario_5 = valor_formacao / 1825
    # Mensal.
    mensal_1 = valor_formacao / 12
    mensal_2 = valor_formacao / 24
    mensal_3 = valor_formacao / 36
    mensal_4 = valor_formacao / 48
    mensal_5 = valor_formacao / 60
    print('\n\033[0;32mDIÁRIO')
    print('O valor diário da formação em 1 ano é R$ {:.2f}'.format(diario_1))
    print('O valor diário da formação em 2 anos é R$ {:.2f}'.format(diario_2))
    print('O valor diário da formação em 3 anos é R$ {:.2f}'.format(diario_3))
    print('O valor diário da formação em 4 anos é R$ {:.2f}'.format(diario_4))
    print('O valor diário da formação em 5 anos é R$ {:.2f}\033[m'.format(diario_5))
    print('\n\033[0;33mMENSAL')
    print('O valor mensal da formação em 1 ano é R$ {:.2f}'.format(mensal_1))
    print('O valor mensal da formação em 2 anos é R$ {:.2f}'.format(mensal_2))
    print('O valor mensal da formação em 3 anos é R$ {:.2f}'.format(mensal_3))
    print('O valor mensal da formação em 4 anos é R$ {:.2f}'.format(mensal_4))
    print('O valor mensal da formação em 5 anos é R$ {:.2f}\033[m'.format(mensal_5))
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\n\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break    
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")