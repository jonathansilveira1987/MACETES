# Análise de dados.

from time import sleep

# Análise de dados do grupo.

tot18 = toth = totm20 = 0

while True:

    idade = int(input("\nIdade: "))
    
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Sexo [M/F]? ")).strip().upper()[0]
    if idade >= 18:
        tot18 = tot18 + 1
    if sexo == "M":
        toth = toth + 1
    if sexo == "F" and idade < 20:
        totm20 = totm20 + 1    
    resp = " "
    while resp not in "SN":
        resp = str(input("\nQuer continuar [S/N]? ")).strip().upper()[0]
    if resp == "N":
        break

print(f"\nTotal de pessoas com mais de 18 anos: {tot18}.")
print(f"Total de homens cadastrados: {toth}.")
print(f"Total de mulheres com menos de 20 anos cadastradas: {totm20}.\n")


# Análise de dados v1.0.

n = input("\n\033[0;33mDigite algo: \033[m").strip()

print("\n\033[0;36mAnalisando informações...\033[m")
sleep(3)
print(f"\nInformação digitada = \033[0;32m{n}\033[m")
print(f"\nTotal de caracteres com espaços = \033[0;32m{len(n)}\033[m")
print("\nTotal de caracteres sem espaços = \033[0;32m{}\033[m".format(len(n)-n.count(" ")))
# print("\nEspaços = \033[0;32m{}\033[m".format(len(" ")-n.count(" ")))
totpalavras = n.split()
print(f"\nTotal de palavras = \033[0;32m{len(totpalavras)}\033[m")
palavras = n.upper()
print(f"\nMaiúsculas = \033[0;32m{palavras}\033[m")
print("\nMaiúsculas: \033[0;32m{}\033[m".format(n.upper()))
print("\nMinúsculas: \033[0;32m{}\033[m".format(n.lower()))
print("\nA primeira composição tem \033[0;32m{}\033[m caractere(s)".format(n.find(" ")))
separa = n.split()
print("\nA primeira composição de caracteres é \033[0;32m{}\033[m e tem \033[0;32m{}\033[m caracteres\n".format(separa[0], len(separa[0])))


# Análise de dados em uma Tupla.

num = (int(input("\nDigite um número: ")),
        int(input("Digite outro número: ")),
        int(input("Digite mais um número: ")),
        int(input("Digite o último número: ")))

print(f"\nVocê digitou os valores {num}")
print(f"\nO valor 9 apareceu {num.count(9)} vezes.")

if 3 in num:
    print(f"\nO valor 3 apareceu na {num.index(3)+1}ª posição.")
else:
    print("O valor 3 não foi digitado em nenhuma posição.")

print("Os valores pares digitados foram: ",end="")
for n in num:
    if n % 2 == 0:
        print(n, end=" ")
print('\n')