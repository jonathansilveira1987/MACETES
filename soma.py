# Primeira Solução.

soma = cont = 0
while True:
    num = int(input("\nDigite um valor (999 para parar a execução): "))
    if num == 999:
        break
    cont = cont + 1
    soma = soma + num
print("\nA soma dos {} valores foi {}.".format(cont, soma))