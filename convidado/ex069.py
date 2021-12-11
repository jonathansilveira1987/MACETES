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
print(f"Total de mulheres com menos de 20 anos cadastradas: {totm20}.")