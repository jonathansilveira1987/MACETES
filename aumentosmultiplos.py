# Aumentos múltiplos.

salario = float(input("Digite o salário atual do funcionário: R$ "))
if salario > 1250:
    reajuste = salario * 0.10
    novo_salario = salario + reajuste
else:
    salario <= 1250
    reajuste = salario * 0.15
    novo_salario = salario + reajuste
print("O valor de reajuste foi de R$ {:.2f}, portanto o salário após o reajuste é de R$ {:.2f}.".format(reajuste, novo_salario))