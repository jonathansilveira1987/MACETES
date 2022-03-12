

# Valor numérico
while True:
    try:
        n = int(input('\ndigite um número de 3 dígitos: '))
        if 100 <= n <= 999: # é um número de 3 dígitos
            break # sai do loop
        print('\nO número deve ter 3 dígitos')
    except ValueError:
        print('\nNão foi digitado um número')



while True:
    try:
        texto = input('\ndigite um número de 3 dígitos: ')
        if texto.isnumeric() and len(texto) == 3: # é um "número" de 3 dígitos
            break # sai do loop
        print('\nO número deve ter 3 dígitos')
    except ValueError:
        print('\nNão foi digitado um número')
print(texto[::-1]) # imprime invertido




# invertendo
inverso = 0
while n > 0:
    inverso = inverso * 10 + n % 10
    n //= 10
    print(inverso)

#Número negativo
x = abs(n)
inverso = 0
while x > 0:
    inverso = inverso * 10 + x % 10
    x //= 10
    if n < 0:
        inverso *= -1

# isnumeric
print('½'.isnumeric()) # True
print(int('½')) # ValueError


















































































































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