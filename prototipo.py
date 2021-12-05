ordens = [0]
soma = cont = 0



print('\nOrdens de Manutenção:')
print('\n')

while True:
    ordens = int(input("\nDigite a ordem (999 para parar a execução): "))
    if ordens == 999:
        break
    cont = cont + 1
    soma = soma + ordens

for ordem in ordens:
    if ordem [0] == '2':
        print(f'Ordem {ordem} - \033[0;31mManutenção Preventiva.\033[m')
    if ordem [0] == '3':
        print(f'Ordem {ordem} - \033[0;33mManutenção Corretiva.\033[m')
    else:
        print(f'Ordem {ordem} - \033[0;32mManutenção Preditiva.\033[m')
print('\n')




'''
'20565285',
            '30565285',
            '10565285',
            '30565285',
            '50565285',
            '20565285',
            '30565285',
            '90565285'
'''