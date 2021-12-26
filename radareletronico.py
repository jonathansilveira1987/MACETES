# Radar eletrônico
while True:
    # Programa principal!
    velocidade = float(input("\nQual é a velocidade atual do carro? "))
    if velocidade > 80:
        print("\n\033[0;31mMULTADO! Você excedeu o limite permitido de velocidade que é de 80km/h.\033[m")
        multa = (velocidade - 80) * 7
        print("\033[0;33mVocê deve pagar uma multa de R$ {:.2f}.\033[m".format(multa))
    print("\n\033[0;32mTenha um bom dia! Dirija com segurança!\033[m\n")
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break    
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")