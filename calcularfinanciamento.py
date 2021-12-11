# Aprovando Empréstimo

valor_casa = float(input("Informe o valor do imóvel: R$ "))
salario_comprador = float(input("Informe o salário do comprador: R$ "))
anos = int(input("Infome em quantos anos o imóvel será pago: "))
prestacao = valor_casa / (anos * 12)
minimo = salario_comprador * 30 / 100
print("Para pagar uma casa de R$ {:.2f} em {:.0f} anos.".format(valor_casa, anos))
print("O valor da prestação será de R$ {:.2f}.".format(prestacao))
if prestacao <= minimo:
    print("Empréstimo pode ser CONCEDIDO!")
else:
    print("Empréstimo NEGADO!")




# print("COMPARANDO: Tem que pagar R$ {:.2f} e o mínimo é de R$ {:.2f}.".format(prestacao, minimo))