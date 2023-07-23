velocidade = input('\nVelocidade em KM: ')
atrito = input('μ Atrito em segundos: ')
distancia = (int(velocidade) ** 2) / (250 * float(atrito))
print(f'\n\033[0;32mA distância para frenagem será de {distancia:.1f} metro(s)\033[m')


tonelada = input('\nDigite o valor em tonelada a ser convertido: ')
resp = float(tonelada) * 1000

resultado_kilo = f'{resp:_.2f}'
resultado_kilo = resultado_kilo.replace('.','.').replace('_','.')
print(f'\n\033[0;31m{tonelada} tonelada(s) equivalem a {resultado_kilo} kilo(s)\033[m\n')