# Calcular Hipotenusa.

import math

while True:
    # Programa principal!
    print('''
    Fórmula para calcular a Hipotenusa.

    [ 1 ] - Fórmula matemática
    [ 2 ] - Fórmula com módulo
    ''')

    opcao = input("Informe a opção desejada (0 para encerrar): ")

    # Encerrar aplicação.
    if opcao in '0':
        break
    elif opcao == '1':
        # Fórmula matemática.
        co = float(input("\nInforme o comprimento do Cateto Oposto: "))
        ca = float(input("Informe o comprimento do Cateto Adjacente: "))
        hi = (co ** 2 + ca ** 2) ** (1/2)
        print("\nA hipotenusa vai medir -> {:.2f}.".format(hi))
    elif opcao == '2':
        # Fórmula com módulo.
        co = float(input("\nInforme o comprimento do Cateto Oposto: "))
        ca = float(input("Informe o comprimento do Cateto Adjacente: "))
        hi = math.hypot(co, ca)
        print("\nA hipotenusa vai medir -> {:.2f}.".format(hi))
    else:
        # Aqui vai o "Tente novamente!"
        opcao != '1' '2'
        print("\n\033[0;31mERRO! Informação incorreta, tente novamente.\033[m\n", end=" ")
        continue
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\n\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break    
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")