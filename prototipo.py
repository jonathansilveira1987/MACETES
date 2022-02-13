






















'''


while True:
    # Aqui vai o programa principal!

    while True:
        num = int(input("\n\033[0;32mDigite um número entre 0 e 20: \033[m"))
        # Aqui vai o "Tente novamente!"
        if 0 <= num <= 20:
            break
        print("\n\033[0;31mValor incorreto, tente novamente.\033[m\n", end=" ")
        print(f"\nVocê digitou o número {num}.")

        n = int(input('\nNúmero/Base: '))
        p = int(input('Potência/Expoente: '))
        a = n ** p
        print()
        resultado = '{0:,}'.format(a).replace(',','.') #Aqui coloca os pontos
        print(resultado)
    
    
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\n\033[0;33mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")





'''