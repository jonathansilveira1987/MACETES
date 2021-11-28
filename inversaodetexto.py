# Inversão de Texto.

while True:    
    txt = str(input('\033[0;32m\nDigite o texto: \033[m'))[::-1]
    print(txt)   
    resp = " "
    while resp not in "10":
        resp = str(input("\nDeseja continuar [1 - SIM / 0 - NÃO]? ")).strip().upper()[0]
    if resp == "0":
        break    
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")