# Grupo da Maioridade.

from datetime import date

atual = date.today().year
totalmaior = 0
totalmenor = 0

for pessoas in range(1, 5):
    nasc = int(input("Em que ano a {}ª pessoa nasceu? ".format(pessoas)))
    idade = atual - nasc
    if idade >= 21:
        totalmaior += 1        
    else:
        totalmenor += 1

print("\nAo todo tivemos {} pessoa(s) maior(es) de idade.".format(totalmaior))
print("E também tivemos {} pessoa(s) menor(es) de idade.\n".format(totalmenor))