# Calcular Potenciação.
n = int(input('\nNúmero/Base: '))
p = int(input('Potência/Expoente: '))
resultado = n ** p
result = resultado = '{0:,}'.format(resultado).replace(',','.') #Aqui coloca os pontos
print('\n', result, '\n')