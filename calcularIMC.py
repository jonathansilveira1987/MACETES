#  Índice de Massa Corporal.

while True:
    try:
        # Programa principal!
        print('\nIMC - ìndice de Massa Corporal.')
        peso = float(input("\nInforme seu peso (KG): "))
        altura = float(input("Informe sua altura (M): "))
        imc = peso / (altura ** 2) # altura ao quadrado.
        print("\n\033[0;32mO IMC dessa pessoa é de {:.1f}.\033[m".format(imc))
        if imc < 18.5:
            print("\nVocê está ABAIXO do peso normal.\n")
        elif 18.5 <= imc < 25:
            print("\nParabéns! Você está na faixa de peso NORMAL.\n")
        elif 25 <= imc < 30:
            print("\nVocê está com SOBREPESO.")
        elif 30 <= imc < 40:
            print("\nVocê está em OBESIDADE.\n")
        elif imc >= 40:
            print("\n\033[0;31mVocê está em OBESIDADE MÓRBIDA, CUIDADO!\033[m\n")
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