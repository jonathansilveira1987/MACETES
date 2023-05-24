# Calculadora.
def menu():
    a = int(input('\nValor 1: '))
    b = int(input('Valor 2: '))

    print('''
Escolha a operação desejada:
+
-
*
/
    ''')
    operacao = input('> ')

    if operacao == '+':
        result1 = a + b
        print()
        print(a, '+', b, '=', result1)
        print('\nO resultado de', a, '+', b, 'é', result1)
        print(f'O resultado de {a} + {b} é {result1}')
    elif operacao == '-':
        result2 = a - b
        print(f'\nO resultado de {a} - {b} é {result2}')
    elif operacao == '*':
        result3 = a * b
        print(f'\nO resultado de {a} * {b} é {result3}')
    elif operacao == '/':
        result4 = a / b
        print(f'\nO resultado de {a} / {b} é {result4}')
    else:
        operacao != '+, -, *, /'
        print('\nVocê digitou uma operação inválida!')
        # print('A calculadora foi encerrada!')
while True:
    menu()