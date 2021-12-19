# Função que calcula área.

def area(larg, comp):
    a = larg * comp
    print(f'\nA área de um terreno {larg} x {comp} é de {a}m².\n')


print('\nControle de Terrenos')
print('-' * 20)
l = float(input('\nLARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)