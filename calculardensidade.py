# Calcular Densidade.
# cm³.
# Densidade Absoluta ou Massa Específica.
# Medimos essa grandeza medida em gramas = g/cm³
# densidade = g/cm³
# massa = gramas
# volume = cm³
# Fórmula: d = m/v

while True:    
    print('''\n\033[0;33m
          - CALCULAR DENSIDADE -
    Escolha abaixo a operação desejada!

    [ 1 ] - DENSIDADE EM g/mL - Será informado massa do soluto + massa do solvente + solução.
    [ 2 ] - MASSA EM KG - Será informado densidade + volume.
    [ 3 ] - VOLUME EM CM³ - Será informado densidade + massa.
    \033[m
    ''')

    unidade = int(input("\033[0;32mInforme a opção desejada >\033[m "))

    # Densidade em g/mL?
    if unidade == 1:
        print('\nDensidade em g/mL...')
        soluto = float(input('Massa do soluto: '))
        solvente = float(input('Massa do solvente: '))
        solucao = float(input('Solução: '))
        m = ((soluto + solvente) / solucao)
        print('A densidade é: \033[0;31m{:.1f}\033[m g/mL\n'.format(m))
    # Massa em KG?
    if unidade == 2:
        print('\nMassa em KG...')
        d = float(input('Densidade: '))
        v = float(input('Volume: '))
        m = ((d * v) / 1000)
        print('A densidade é: \033[0;31m{:.4f}\033[m KG\n'.format(m))
    # Volume em cm³?
    if unidade == 3:
        print('\nVolume em cm³...')
        d = float(input('Densidade: '))
        m = float(input('Massa: '))
        v = m / d
        print('A densidade é: \033[0;31m{:.3f}\033[m cm³\n'.format(v))
    resp = " "
    while resp not in "10":
        resp = str(input("\nDeseja continuar [1 - SIM / 0 - NÃO]? ")).strip().upper()[0]
    if resp == "0":
        break
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")