ficha = list()
while True:
    nome = str(input("\nNome: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input("Quer continuar? [S/N] "))
    if resp in "Nn":
        break
print("-=" * 30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print("-=" * 26)
for i, a in enumerate(ficha):
    print(f"{i:<4}{a[0]:<10}{a[2]:>8.1f}")
while True:
    print("-" * 35)
    opc = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if opc == 999:
        print("Finalizando...")
        break
    if opc <= len(ficha) - 1:
        print(f"\nNotas de {ficha[opc][0]} são {ficha[opc][1]}")
print("<<< VOLTE SEMPRE >>>")


ordens = [  '20565285',
            '30565285',
            '10565285',
            '30565285',
            '50565285',
            '20565285',
            '30565285',
            '90565285'
]
print('\nOrdens de Manutenção:')
print()
for ordem in ordens:
    if ordem [0] == '2':
        print(f'Ordem {ordem} - \033[0;31mManutenção Preventiva.\033[m')
    if ordem [0] == '3':
        print(f'Ordem {ordem} - \033[0;33mManutenção Corretiva.\033[m')
    else:
        print(f'Ordem {ordem} - \033[0;32mManutenção Preditiva.\033[m')