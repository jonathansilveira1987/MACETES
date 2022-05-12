# Calcular Percentual.
valor = float(input('\nValor R$ '))
percentual = float(input('Percentual desejado % '))
resultado = valor * percentual / 100
print(f'\n\033[0;31m{percentual}%\033[m de \033[0;32m{valor:.2f}\033[m é \033[0;33m{resultado:.2f}\033[m\n')

valor_real = "\033[0;31m{}%\033[m de \033[0;32mR$ {:,.2f}\033[m é \033[0;33mR$ {:,.2f}\033[m".format(percentual, valor, resultado).replace(",", "X").replace(".", ",").replace("X", ".")
print()
print(valor_real)
print()






