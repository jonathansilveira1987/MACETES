
# Raíz Quadrada.
import math
num = float(input("\nInforme um número: "))
raiz = math.pow(num, 1/2)
print(f'\nA raiz quadrada de {num} é {raiz}.')
print(f'A raiz quadrada de {num} é {round(raiz, 2)}.')
# Raíz Quadrada - Cálculo Complexo.
import cmath
num = float(input("\nInforme um número: "))
raiz = cmath.sqrt(num)
print(f'\nA raiz quadrada de {num} é {raiz:.2f}.')


# Aqui vai o programa principal!
a = float(input('\nEntre com o valor de A: '))
b = float(input('Entre com o valor de B: '))
c = float(input('Entre com o valor de C: '))
delta = (b ** 2) - 4 * a * c
# print("\n**************************\n")
if a == 0:
    print("\n\033[0;31mO valor de A, deve ser diferente de 0.\033[m")
elif delta < 0:
    print("\n\033[0;34mSem raízes reais.\033[m")
else:
    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    x2 = (-b - delta ** (1 / 2)) / (2 * a)
    print("\nX1: \033[0;32m{}\033[m".format(x1))
    print("X2: \033[0;32m{}\033[m".format(x2))

# Calcular as Raízes de uma Equação do 2º Grau
def raizes(a, b, c):
    D = (b**2 - 4*a*c)
    x1 = (-b + D**(1/2)) / (2*a)
    x2 = (-b - D**(1/2)) / (2*a)
    print('\nValor de x1: \033[0;31m{0}\033[m'.format(x1))
    print('Valor de x2: \033[0;31m{0}\033[m'.format(x2))
if __name__ == '__main__':
    while True:
        print('\nCalculando as raízes de uma equação de 2º grau\n')
        a = float(input('Entre com o valor de a: '))
        b = float(input('Entre com o valor de b: '))
        c = float(input('Entre com o valor de c: '))
        raizes(a,b,c)
        # Aqui vai o "Deseja continuar?"
        resp = " "
        while resp not in "10":
            resp = str(input("\n\033[0;33mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
        if resp == "0":
            break    
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")