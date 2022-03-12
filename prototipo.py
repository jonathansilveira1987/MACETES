

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
print(f'A raiz quadrada de {num} em cálculo complexo é \033[0;32m{raiz:.2f}\033[m\n')


















































































































'''


num = float(input('\nNumero original: '))
if num == round(num):
    print("\nO valor informado é INTEIRO.")
else:
    print("\nO valor informado é DECIMAL.")
    print("\nArredondado pra baixo: ", round(num-0.5))
    print("Arredondado pra cima : ", round(num+0.5))










a = 100/5
b = 20//3
print(a * b)

c = 5 / 5.5
d = 5 * 5.5
print(c//d)



v = sm = nv = 0
while True:
    v = int(input("\nDigite um valor (\033[0;32m000\033[m para executar a operação): "))
    if v == 000:
        break
    sm += v
    nv += 1
print(f"\nO total de valores digitados foi de {nv}.")
print(f"A soma entre eles é {sm}.")




v = sm = nv = 0
while v != 999:
    v = int(input("\nDigite um valor (\033[0;32m000\033[m para executar a operação): "))
    if v == 000:
        break
    sm += v
    nv += 1
print(f"\nO total de valores digitados foi de {nv}.")
print(f"A soma entre eles é {sm}.")









while True:
    # Aqui vai o programa principal!
    n = int(input('\nNúmero/Base: '))
    p = int(input('Potência/Expoente: '))
    a = n ** p
    print()
    resultado = '{0:,}'.format(a).replace(',','.') #Aqui coloca os pontos
    print(f'\033[0;31m{n}\033[m elevado a \033[0;31m{p}\033[m é \033[0;31m{resultado}\033[m.')
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\n\033[0;33mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")













'''