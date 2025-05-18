salario = float(input("\nQual é o valor atual do salário: R$ "))
reajuste = float(input("Informe o valor de reajuste % : "))
novo_salario = salario + (salario * reajuste / 100)
print("\nO salário atual do funcionário é R$ {:.2f}, após {:.0f}% de aumento, passará a receber \033[0;33mR$ {:.2f}\033[m.".format(salario, reajuste, novo_salario))

salario_antigo = float(input("\nSalário Antigo: R$ "))
salario_novo = float(input("Novo Salário: R$ "))
novo_salario = ((salario_novo - salario_antigo) / salario_antigo) * 100
print("\nO valor de reajuste foi de \033[0;32m{:.2f}%\033[m.\n".format(novo_salario))