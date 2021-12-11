# Par ou Ímpar.

while True:


    # Programa principal!
    n = int(input("\nDigite um número qualquer: "))
    resultado = n % 2
    # print("O resultado foi {}.".format(resultado))
    
    if type(n) == str and type(n) == float and type(n) == bool:
        print("\n\033[0;31mERRO! Informação incorreta, tente novamente.\033[m\n", end=" ")
        n = int(input("\nDigite um número qualquer: "))
        resultado = n % 2
        if resultado == 0: # O resto da divisão de qualquer número par por 2 é "0" e qualquer número ímpar por 2 é "1".
            print("\nO número \033[0;31m{}\033[m é PAR.\n".format(n))
        elif resultado == 1:
            print("\nO número \033[0;31m{}\033[m é ÍMPAR.\n".format(n))
    else:
        
        if resultado == 0: # O resto da divisão de qualquer número par por 2 é "0" e qualquer número ímpar por 2 é "1".
            print("\nO número \033[0;31m{}\033[m é PAR.\n".format(n))
        elif resultado == 1:
            print("\nO número \033[0;31m{}\033[m é ÍMPAR.\n".format(n))



    

    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break    
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")