from time import sleep

pi = int(input('\nInforme o ponto inicial: '))
pf = int(input('Informe o ponto final: '))
print('\033[0;32m')
for x in range(pf, pi, -1):
    for y in range(1, x):
        print(y, end="")
    sleep(0.5)
    print('\033[m')







'''

for x in range(6, 1, -1):
    for y in range(1, x):
        print(y, end="")
    print()


'''