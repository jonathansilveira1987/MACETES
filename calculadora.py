# Calculadora.

while True:
    # Programa principal!
    operacao = input('''
                [ CALCULADORA ]

Informe a operação matemática que deseja realizar:

+ para Adição
- para Subtração
* para Multiplicação
/ para Divisão

\033[0;32m>\033[m ''')

    n1 = int(input('\nDigite o 1º número: '))
    n2 = int(input('Digite o 2º número: '))

    if operacao == '+':
        r = n1 + n2
        print('\n{} + {} = {}.\n'.format(n1, n2, r))
    elif operacao == '-':
        r = n1 - n2
        print('\n{} - {} = {}.\n'.format(n1, n2, r))
    elif operacao == '*':
        r = n1 * n2
        print('\n{} * {} = {}.\n'.format(n1, n2, r))
    elif operacao == '/':
        r = n1 / n2
        print('\n{} / {} = {}.\n'.format(n1, n2, r))
    else:
        # Aqui vai o "Tente novamente!"
        operacao != '+, -, *, /'
        print("\n\033[0;31mOperação matemática incorreta, tente novamente.\033[m\n", end=" ")
        continue
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break    
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")