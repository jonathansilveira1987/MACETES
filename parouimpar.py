# Par ou Ímpar.

while True:
    try:
        # Programa principal!
        n = int(input("\nDigite um número qualquer: "))
        resultado = n % 2
        if resultado == 0: # O resto da divisão de qualquer número par por 2 é "0" e qualquer número ímpar por 2 é "1".
            print("\nO número \033[0;31m{}\033[m é PAR.\n".format(n))
        else:
            print("\nO número \033[0;31m{}\033[m é ÍMPAR.\n".format(n))
    except ValueError:
        print("\n\033[0;31mERRO! Informação incorreta, tente novamente.\033[m\n", end=" ")
        continue
# Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break    
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")
































'''

# Código simples.
n = int(input("\nDigite um número qualquer: "))
resultado = n % 2
# print("O resultado foi {}.".format(resultado))
if resultado == 0: # O resto da divisão de qualquer número par por 2 é "0" e qualquer número ímpar por 2 é "1".
    print("\nO número \033[0;31m{}\033[m é PAR.\n".format(n))
else:
    print("\nO número \033[0;31m{}\033[m é ÍMPAR.\n".format(n))

'''