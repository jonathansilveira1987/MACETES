# Par ou Ímpar.

n = int(input("\nDigite um número qualquer: "))
resultado = n % 2
# print("O resultado foi {}.".format(resultado))
if resultado == 0: # O resto da divisão de qualquer número par por 2 é "0" e qualquer número ímpar por 2 é "1".
    print("\nO número \033[0;31m{}\033[m é PAR.\n".format(n))
else:
    print("\nO número \033[0;31m{}\033[m é ÍMPAR.\n".format(n))