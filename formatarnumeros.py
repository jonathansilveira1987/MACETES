a = 2 ** 80

print('\n')
# print(f'{0:.}').format(a).replace(',', '.')
resultado = '{0:,}'.format(a).replace(',','.') #Aqui coloca os pontos
print(resultado)
print('\n')



n = int(input('\nNúmero/Base: '))
p = int(input('Potência/Expoente: '))
resultado = n ** p
result = resultado = '{0:,}'.format(resultado).replace(',','.') #Aqui coloca os pontos
print('\n')
print(result)
print('\n')