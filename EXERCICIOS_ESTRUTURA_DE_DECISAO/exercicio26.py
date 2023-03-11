# 26. Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro. 
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível 
# (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a 
# ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço 
# do litro do álcool é R$ 1,90.
# Desenvolvido por Jonathan Silveira - Instagram: @ jonathandev01

combustivel = input("Escolha o combustível desejado sendo G - Gasolina ou A - Álcool: ")
litros = float(input("Digite a quantidade de litros do combustível escolhido: "))
valor = 0

if combustivel == "A" or combustivel == "a":
    valor = litros * 1.9
    if litros <= 20:
        valor -= 1.9 * litros * 3 / 100
    else:
        valor -= 1.9 * litros * 5 / 100

elif combustivel == "G" or combustivel == "g":
    valor = litros * 2.5
    if litros <= 20:
        valor -= 2.5 * litros * 4 / 100
    else:
        valor -= 2.5 * litros * 6 / 100
        
print("O valor a ser pago é R$: ", valor)