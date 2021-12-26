# Calcular pressão atmosférica.
while True:
    # Programa principal!
    atm = 101.325 # A pressão atmosférica ao nível do mar é equivalente a uma força de 101.325 N a cada m² de superfície.
    n = float(input('\nInforme o número de atmosferas: '))
    pa = n * atm
    print(f'\n\033[0;32m{n}\033[m atmosferas equivalem a \033[0;32m{pa} kg\033[m de pressão para cada m².\n')
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break    
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")