a = 0
b = int(input('\nContagem: '))
print('\033[33m')
while a <= b:
    print(f'Este é o número {a}')
    a = a + 1
print('\033[m')

palavra = str(input('Palavra: '))
print('\033[34m')
x = list(palavra)
for i in enumerate(x):
    print(i, end=' ')
print('\033[m\n')