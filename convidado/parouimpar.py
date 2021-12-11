n = int(input("Digite um número qualquer: "))
resultado = n % 2
# print("O resultado foi {}.".format(resultado))
if resultado == 0: # O resto da divisão de qualquer número par por 2 é "0" e qualquer número ímpar por 2 é "1".
    print("O número {} é PAR.".format(n))
else:
    print("O número {} é ÍMPAR.".format(n))