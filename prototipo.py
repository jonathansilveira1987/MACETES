import math

# Raíz quadrada.
num = float(input('Número: '))
raiz = math.sqrt(num)
print('Resultado = ', raiz)



# Bhaskara.

a = float(input('Delta 1: '))
b = float(input('Delta 2: '))
c = float(input('Delta 3: '))
delta = b * b - 4 * a * c
if delta < 0:
    print("Não há raízes reais")
elif delta == 0:
    print("Há uma raiz distinta apenas")
else:
    print("Há duas raízes distintas")
x1 = (-b + math.sqrt(delta)) / (2 * a)
x2 = (-b - math.sqrt(delta)) / (2 * a)
print(f"As raízes são {x1} e {x2}")