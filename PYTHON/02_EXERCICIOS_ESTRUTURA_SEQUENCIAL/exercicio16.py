# 16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados 
# da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados 
# e  que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades 
# de latas de tinta a serem compradas e o preço total.
# Desenvolvido por Jonathan Silveira - Instagram: @jonathandev01

import math

area = int(input("Digite a área de pintura em metros quadrados: "))
litros = area / 3
valor_lata = 80
capacidade_lata = 18
qtd_latas = litros / capacidade_lata
total = qtd_latas * valor_lata
print("Você usará: ", qtd_latas, "latas")
print("O preço a pagar é de R$: ", total)