# Calculadora.
a = int(input('\nValor 1: '))
b = int(input('Valor 2: '))

print('''
Escolha a operação desejada:
1 +
2 -
3 *
4 /
''')
operacao = input('> ')

if operacao == '1':
    result1 = a + b
    print(a, '+', b, '=', result1)
    print('O resultado de', a, '+', b, 'é', result1)
    print(f'O resultado de {a} + {b} é {result1}')
elif operacao == '2':
    result2 = a - b
    print(f'O resultado de {a} - {b} é {result2}')
elif operacao == '3':
    result3 = a * b
    print(f'O resultado de {a} * {b} é {result3}')
elif operacao == '4':
    result4 = a / b
    print(f'O resultado de {a} / {b} é {result4}')
else:
    operacao != '1, 2, 3, 4'
    print('Você digitou uma operação inválida!')
    print('A calculadora foi encerrada!')