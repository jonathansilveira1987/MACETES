# Ano Bissexto

from datetime import date

print("Coloque 0 para analisar o ano atual")
ano = int(input("Ou informe o ano a ser analisado: "))

if ano == 0:
    ano = date.today().year
    
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano {} é BISSEXTO.".format(ano))
else:
    print("O ano {} NÃO É BISSEXTO.".format(ano))