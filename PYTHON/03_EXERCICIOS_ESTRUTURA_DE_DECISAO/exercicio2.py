# 2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
# Desenvolvido por Jonathan Silveira - Instagram: @ jonathandev01

# Simples
numero = int(input('\nInforme um número: '))
if numero >= 0:
  print(f'\nO número {numero} é positivo.'.format(numero))
else:
  print(f'\nO número {numero} é negativo.'.format(numero))

# Detalhado
num = int(input('\nInforme um número: '))
if num > 0 :
    print("\nPositivo.\n")
else:
    if num == 0 :
        print("\nNem positivo nem negativo, é 0\n")
    else:
        print("\nNegativo.\n")