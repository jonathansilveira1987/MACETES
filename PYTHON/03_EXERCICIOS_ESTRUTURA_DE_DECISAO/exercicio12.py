# 12. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do 
# Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e 
# que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
# O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao 
# usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o 
# exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        # Salário Bruto: (5 * 220)        : R$ 1100,00
        # (-) IR (5%)                     : R$   55,00  
        # (-) INSS ( 10%)                 : R$  110,00
        # FGTS (11%)                      : R$  121,00
        # Total de descontos              : R$  165,00
        # Salário Liquido                 : R$  935,00
# Desenvolvido por Jonathan Silveira - Instagram: @ jonathandev01

valor_hora_trabalhada = float(input("Digite o valor da hora de trabalho: "))
valor_horas_mes = float(input("Digite o valor de horas trabalhadas no mês: "))

salario_bruto = valor_hora_trabalhada * valor_horas_mes
fgts = (salario_bruto * 11) / 100
sindicato = (salario_bruto * 3) / 100

if salario_bruto <= 900:
    salario_liquido = salario_bruto - sindicato

elif salario_bruto > 900 and salario_bruto <= 1500:
    ir = (salario_bruto * 5) / 100
    salario_liquido = salario_bruto - ir - sindicato

elif salario_bruto > 1500 and salario_bruto <= 2500:
    ir = (salario_bruto * 10) / 100
    salario_liquido = salario_bruto - ir - sindicato

else:
    ir = (salario_bruto * 20) / 100
    salario_liquido = salario_bruto - ir - sindicato

print("Seu salário bruto é de: ", salario_bruto)
print("O valor de seu FGTS é: ", fgts)
print("O valor para o sindicato é de: ", sindicato)
print("O valor de seu salário líquidom é de: ", salario_liquido)

# print("Seu salario bruto e : %7.2f" % salariob)
# print("O valor de seu FGTS e de: %7.2f" % fgts)
# print("O sindicato vai te levar: %7.2f" % sind)
# print("Seu salario liquido e de: %7.2f" % salariol)