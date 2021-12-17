# Python - Fluxo Sequencial - Conversão de medidas (aplicação da regra de 3)

m = float(input('\nInforme a medida em Metros: '))
cm = m * 100
pol = cm / 2.54
pes = pol / 12
jar = pes / 3

print('\nA medida de \033[0;32m{}\033[m metros, corresponde a...'. format(m))
print('   - {} centímetros.'.format(round(cm, 2)))
print('   - {} polegadas.'.format(round(pol, 1)))
print('   - {} pes.'.format(round(pes, 1)))
print('   - {} jardas.\n'.format(round(jar, 1)))