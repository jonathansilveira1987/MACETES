# 11. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram 
# para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado 
# no salário atual:
# Após o aumento ser realizado, informe na tela: O salário antes do reajuste, o percentual de aumento 
# aplicado, o valor do aumento e o novo salário, após o aumento.
# Desenvolvido por Jonathan Silveira - Instagram: @ jonathandev01

salario = float(input("\nDigite o valor atual do salário do colaborador: "))
# salários até R$ 280,00 (incluindo) : aumento de 20%
if salario <= 280:
    print()
    print ("O valor do salário antes do reajuste:", salario)
    print ("O valor de percentual de aumento aplicado foi 20%")
    print ("O valor do aumento foi de: ", salario * 0.2)
    print ("O valor do novo salário com reajuste é: ", salario * 0.2 + salario)
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
elif salario > 280 and salario < 700:
    print()
    print ("O valor do salário antes do reajuste:", salario)
    print ("O valor de percentual de aumento aplicado foi 15%")
    print ("O valor do aumento foi de: ", salario * 0.15)
    print ("O valor do novo salário com reajuste é: ", salario * 0.15 + salario)
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
elif salario > 700 and salario < 1500:
    print()
    print ("O valor do salário antes do reajuste:", salario)
    print ("O valor de percentual de aumento aplicado foi 10%")
    print ("O valor do aumento foi de: ", salario * 0.10)
    print ("O valor do novo salário com reajuste é: ", salario * 0.10 + salario)
# salários de R$ 1500,00 em diante : aumento de 5%
elif salario >= 1500:
    print()
    print ("O valor do salário antes do reajuste:", salario)
    print ("O valor de percentual de aumento aplicado foi 5%")
    print ("O valor do aumento foi de: ", salario * 0.05)
    print ("O valor do novo salário com reajuste é: ", salario * 0.05 + salario)
print()