a = float(input('\nVetor A: '))
b = float(input('Vetor B: '))
result1 = a - b
result2 = result1 - 100
print(f'\nDo valor \033[0;32m{a}\033[m retirando \033[0;32m{b}\033[m ainda teremos \033[0;33m{result1:.2f}%\033[m')
print(f'\n\033[0;32m{b}\033[m retirado de \033[0;32m{a}\033[m equivale a \033[0;33m{result2:.2f}%\033[m\n')






# print(f'\nO percentual de \033[0;32m{a}\033[m - \033[0;32m{b}\033[m é \033[0;33m{result:.2f}%\033[m')
# print(f'\nO percentual obtido é de \033[0;33m{result:.2f}%\033[m')