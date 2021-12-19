# Função de Contador.

from time import sleep

def contador(i, f, p):
    # Validando P zerado e P negativo.
    if p < 0:
            p = p * - 1
    if p == 0:
        p = 1

    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}:')
    sleep(2.5)
    
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}',end=' ', flush=True)
            sleep(0.5)
            cont = cont + p
        print('\nFim!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont = cont - p
        print('\nFim!')
        
# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)