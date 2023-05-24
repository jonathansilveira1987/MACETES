# 15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o 
# Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# Salário bruto.
# Quanto pagou ao INSS.
# Quanto pagou ao sindicato.
# Salário líquido.
# Calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.
# Desenvolvido por Jonathan Silveira - Instagram: @jonathandev01

valor_hora = float(input("Digite o valor recebido por hora: "))
horas_trabalhadas = int(input("Digite o número de horas trabalhadas durante o mês: "))
salario = valor_hora * horas_trabalhadas
ir = (11/100.0 * salario)
print ("Imposto de renda: ",ir)
inss = (8/100.0 * salario)
print ("INSS: ",inss)
sind = (5/100.0 * salario)
print ("Sindicato: ",sind)
desc = ir + inss + sind
salarioL = salario - desc
print ("O desconto total do salario bruto(",salario,"R$)",
       "foi",desc,"\nO salario liquido ficou,",salarioL)