a = 2 ** 80

print('\n')
# print(f'{0:.}').format(a).replace(',', '.')
resultado = '{0:,}'.format(a).replace(',','.') #Aqui coloca os pontos
print(resultado)
print('\n')