salario = float(input("\nQual é o preço do produto: R$ "))
novo_salario = salario + (salario * 15 / 100)
print("\nO salário atual do funcionário é R$ {:.2f}, após 15% de aumento, passará a receber R$ {:.2f}.\n".format(salario, novo_salario))