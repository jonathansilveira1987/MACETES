# Inverter Número.
while True:
    try:
        texto = input('\nInforme um número de 3 dígitos: ')
        if texto.isnumeric() and len(texto) == 3: # é um "número" de 3 dígitos
            break # sai do loop
        print('\nO número deve ter 3 dígitos')
    except ValueError:
        print('\nNão foi digitado um número')
print('Segue número invertido:', texto[::-1]) # imprime invertido


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
        continua = input('\nDeseja sair? [1 - SIM / 2 - NÂO]: ')
        if (continua == '1'):
            break






















































































































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