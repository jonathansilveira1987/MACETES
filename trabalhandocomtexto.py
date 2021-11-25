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


# Análise Completa de Nome.
n = str(input("Digite seu nome completo: ")).strip()
print("Analisando seu nome...")
print("Seu nome letras maiúsculas é: {}.".format(n.upper()))
print("Seu nome em letras minúsculas é {}.".format(n.lower()))
print("Seu nome tem {} letras.".format(len(n)-n.count(" ")))
# print("Seu primeiro nome tem {} letras.".format(n.find(" ")))
separa = n.split()
print("Seu primeiro nome é {} e tem {} letras.\n".format(separa[0], len(separa[0])))


# Primeiro Nome e Último Sobrenome.
n = str(input("Digite seu nome completo: ")).strip()
n = n.split()
print("Prazer em te conhecer {}!".format(n[0]))
print("Seu primeiro nome é {}.".format(n[0]))
print("Seu último nome é: {}\n".format(n[len(n)-1]))


# Análise de Letra Específica.
frase = str(input("Digite uma frase: ")).upper().strip()
print("A letra A aparece {} vezes na frase.".format(frase.count("A")))
print("A primeira letra A apareceu na posição {}".format(frase.find("A")+1))
print("A útima letra A apareceu na posição {}\n".format(frase.rfind("A")+1))