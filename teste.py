







# Raíz Quadrada.
import math
import cmath
num = float(input("\nInforme um número: "))
raiz = math.pow(num, 1/2)
print(f'\nA raiz quadrada de {num} é \033[0;32m{round(raiz, 2)}\033[m')
print(f'A raiz quadrada de {num} é \033[0;32m{raiz:.4f}\033[m')
print(f'A raiz quadrada de {num} é \033[0;32m{raiz}\033[m')
# Raíz Quadrada - Cálculo Complexo.
raiz = cmath.sqrt(num)
print(f'A raiz quadrada de {num} em cálculo complexo é  \033[0;32m{raiz:.2f}\033[m')
print(f'A raiz quadrada de {num} em cálculo complexo é \033[0;32m{raiz}\033[m')




# Raíz Quadrada.
import math
import cmath
a = float(input('\nNúmero: '))
# b = int(input('Expoente: '))
# c = a ** b
print('\033[0;34m')
print(f'Raíz quadrada utilizando a função POW ------------> ',pow(a, 0.5))
print(f'Raíz quadrada utilizando o operador ** -----------> ',a ** (0.5))
print(f'Raíz quadrada utilizando math.sqrt ---------------> ',math.sqrt(a))
print(f'Raíz quadrada utilizando cmath.sqrt -------------->',cmath.sqrt(a))
print('\033[m')





