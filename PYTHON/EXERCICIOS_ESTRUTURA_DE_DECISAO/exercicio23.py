# 23. Faça um Programa que peça um número e informe se o número é inteiro ou decimal. 
# Dica: utilize uma função de arredondamento.
# Desenvolvido por Jonathan Silveira - Instagram: @ jonathandev01

# Função de Arredondamento
# numero = float(input("Numero original: "))
# print("Arredondado :", round(numero))

numero = float(input('\nDigite um número: '))

if numero == round(numero):
    print(f'\nO número {numero:.0f} é inteiro\n')
else:
    print(f'\nO número {numero} é decimal')
    print(f'Arredondado para baixo: {round(numero-0.5)}')
    print(f'Arredondado para cima:  {round(numero+0.5)}\n')
    # print("Arredondado pra baixo: ", round(numero-0.5))
    # print("Arredondado pra cima : ", round(numero+0.5))