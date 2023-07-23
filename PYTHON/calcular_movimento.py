tonelada = input('\nDigite o valor em tonelada a ser convertido: ')
resp = float(tonelada) * 1000

resultado_kilo = f'{resp:_.2f}'
resultado_kilo = resultado_kilo.replace('.','.').replace('_','.')
print(f'\n{tonelada} tonelada(s) equivalem a {resultado_kilo} kilo(s)\n')