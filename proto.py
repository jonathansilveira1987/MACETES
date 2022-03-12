# Inverter Número.
while True:
    try:
        texto = input('\nInforme um número de 3 dígitos: ')
        if texto.isnumeric() and len(texto) == 3: # é um "número" de 3 dígitos
            break # sai do loop
        print('\nO número deve ter 3 dígitos')
    except ValueError:
        print('\nNão foi digitado um número')
print('\nSegue número invertido:', texto[::-1]) # imprime invertido

# Raíz Quadrada.
import math
num = float(input("\nInforme um número: "))
raiz = math.pow(num, 1/2)
print(f'\nA raiz quadrada de {num} é {raiz}')
print(f'A raiz quadrada de {num} é {raiz:.4f}')
print(f'A raiz quadrada de {num} é {round(raiz, 2)}')
# Raíz Quadrada - Cálculo Complexo.
import cmath
num = float(input("\nInforme um número: "))
raiz = cmath.sqrt(num)
print(f'\nA raiz quadrada de {num} é {raiz:.2f}')






