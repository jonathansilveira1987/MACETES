# Números primos.

while True:
    # Programa principal!
    num = int(input("\nDigite um número: "))
    tot = 0
    for c in range(1, num + 1):
        if num % c == 0:
            print("\033[33m", end=" ")
            tot += 1
        else:
            print("\033[31m", end=" ")
        print("{}".format(c), end=" ")
    print("\n\033[mO número {} foi divisível {} vezes.\n".format(num, tot))
    if tot == 2:
        print("E por isso ele É PRIMO!")
    else:
        print("E por isso ele NÃO É PRIMO!")
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\n\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break    
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")