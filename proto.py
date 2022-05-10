# Calcular Percentual.
valor = float(input('\nValor R$ '))
percentual = float(input('Percentual desejado % '))
resultado = valor * percentual / 100
print(f'\n\033[0;31m{percentual}%\033[m de \033[0;32m{valor}\033[m é \033[0;33m{resultado:.2f}\033[m.\n')