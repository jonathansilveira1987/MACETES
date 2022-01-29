# Função para Fatorial.

def fatorial(n, show=False):
    '''
    --> Calcula o fatorial de um numero.
    Parametro n: O número a ser calculado.
    Parametro show: (opcional) Mostrar ou não a conta.
    Return: O valor de um fatorial de um número n.
    '''
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f = f * c
    return f
# Programa principal
# print(fatorial(5))
print(fatorial(5, show=True))
help(fatorial)