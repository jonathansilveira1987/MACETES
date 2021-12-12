# Estatísticas em produtos.

total = totmil = menor = cont = 0
barato = ""
while True:
    produto = str(input("Produto: "))
    preco = float(input("Preço: R$ "))
    cont = cont + 1
    total = total + preco
    if preco > 1000:
        totmil = totmil + 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if resp == "N":
        break
print("{:-^40}".format("FIM DO PROGRAMA"))
print(f"O total da compra foi R$ {total:.2f}.")
print(f"Temos {totmil} produtos custando mais de R$ 1.000,00 reais.")
print(f"O produto mais barato foi {barato} que custa R$ {menor:.2f}.")