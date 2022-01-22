n1 = str(input("\nOrdem 1: "))
n2 = str(input("Ordem 2: "))
n3 = str(input("Ordem 3: "))
n4 = str(input("Ordem 4: "))
ordens = [n1, n2, n3, n4]
print('\nOrdens de Manutenção:')
print()
for ordem in ordens:
    if ordem [0] == '2':
        print(f'Ordem {ordem} - \033[0;31mManutenção Preventiva.\033[m')
    if ordem [0] == '3':
        print(f'Ordem {ordem} - \033[0;33mManutenção Corretiva.\033[m')
    else:
        print(f'Ordem {ordem} - \033[0;32mManutenção Preditiva.\033[m')