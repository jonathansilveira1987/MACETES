# 22. Faça um Programa que peça um número inteiro e determine se ele é par ou impar. 
# Dica: utilize o operador módulo (resto da divisão).
# Desenvolvido por Jonathan Silveira - Instagram: @ jonathandev01

def menu():
    num = int(input('\nDigite um número inteiro: '))

    if (num % 2) == 0:
        print(f'\nO número {num} é PAR')
    else:
        print(f'\nO número {num} é ÍMPAR')
while True:
    menu()