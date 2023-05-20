# 13. Faça um Programa que leia um número e exiba o dia correspondente da semana.
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
# Desenvolvido por Jonathan Silveira - Instagram: @ jonathandev01

def menu():
    dia_da_semana = 1, 2, 3, 4, 5, 6
    dia_da_semana = int(input("\nDigite um número entre 1 & 7: "))
    if dia_da_semana == 1:
        print("\nO número 1 equivale ao dia da semana: Domingo")
    elif dia_da_semana == 2:
        print("\nO número 2 equivale ao dia da semana: Segunda-Feira")
    elif dia_da_semana == 3:
        print("\nO número 3 equivale ao dia da semana: Terça-Feira")
    elif dia_da_semana == 4:
        print("\nO número 4 equivale ao dia da semana: Quarta-Feira")
    elif dia_da_semana == 5:
        print("\nO número 5 equivale ao dia da semana: Quinta-Feira")
    elif dia_da_semana == 6:
        print("\nO número 6 equivale ao dia da semana: Sexta-Feira")
    elif dia_da_semana == 7:
        print("\nO número 7 equivale ao dia da semana: Sábado")
    else:
        print("\nValor Inválido")
while True:
    menu()