a = int(input('\nValor: '))
print()
for i in range(a+1): 
    print(f'\033[0;31m{i}\033[m')

b = int(input('\nValor: '))
c = int(input('Passo: '))
print()
for j in range(b):
    print(f'\033[0;32m{j * c}\033[m')

d = int(input('\nNúmero de repetições: '))
mensagem = input('Mensagem: ')
print()
for num in range(d):
    print(f'\033[0;33m{mensagem * num}\033[m')
print()

