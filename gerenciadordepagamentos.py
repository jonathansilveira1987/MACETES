# Gerenciador de Pagamentos.

print("{:=^60}".format(" Lojas Silveira "))
compra = float(input("\nInforme o valor da compra: "))
print('''\nEscolha a forma de pagamento:
[ 1 ] - Dinheiro / Cheque.
[ 2 ] - À vista no Cartão de Crédito.
[ 3 ] - 2 x no Cartão de Crédito.
[ 4 ] - 3 x ou mais no cartão de Crédito.\n''')
pagamento = int(input("Escolha a forma de pagamento: "))
# Dinheiro ou Cheque.
if pagamento == 1:
    dinheiro_cheque = compra - (compra * 10 / 100)
    print("\nVocê recebeu desconto de 10% em sua compra.")
    print("O valor total à pagar é de R$ {:.2f}.\n".format(dinheiro_cheque))
# À vista no cartão de Crédito.
elif pagamento == 2:
    cartao = compra - (compra * 5 / 100)
    print("\nVocê recebeu 5% de desconto em sua compra.")
    print("O valor total à pagar é de R$ {:.2f}.\n".format(cartao))
# 2 X no Cartão de Crédito.
elif pagamento == 3:
    parcela = compra / 2
    print("\nSua compra será dividida em duas parcelas de R$ {:.2f}.".format(parcela))
    print("O valor total que será pago em parcelas é de R$ {:.2f}.\n".format(compra))
# 3 X ou mais no Cartão de Crédito.
elif pagamento == 4:
    parcelado = compra + (compra * 20 / 100)
    totalparcelas = int(input("Quantas parcelas? "))
    parcela = parcelado / totalparcelas
    print("\nSua compra teve acréscimo de 20% de juros.")
    print("Sua compra será parcelada em {} X de R$ {:.2f}.".format(totalparcelas, parcela))
    print("O valor total à pagar é de R$ {:.2f}.\n".format(parcelado))
else:
    print("\nForma de pagamento incorreta, tente novamente!\n")