# Aquele clássico da Média.

while True:
    # Programa principal!
    nota1 = float(input("\nPrimeira nota: "))
    nota2 = float(input("Segunda nota: "))
    media = (nota1 + nota2) / 2
    print("\nTirando {:.1f} e {:.1f}. a média do aluno é {:.1f}.".format(nota1, nota2, media))
    if 7 > media >= 5:
        print("O aluno está em RECUPERAÇÃO.\n")
    elif media < 5:
        print("O aluno está REPROVADO.\n")
    elif media >= 7:
        print("O aluno está APROVADO.\n")
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break    
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")