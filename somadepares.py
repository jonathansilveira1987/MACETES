# Soma dos pares.

soma = 0
cont = 0
for c in range(1, 7):
    num = int(input("\nDigite o {}º valor: ".format(c)))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print("\n\033[0;35mVocê informou {} números PARES e a soma deles foi {}.\033[m\n".format(cont, soma))