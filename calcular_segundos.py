# Calcular segundos.
('''
Veja abaixo uma tabela mostrando a divisão completa de cada unidade de tempo comum em segundos:

Unidades de tempo habituais 	Segundos
1 minuto                        60 segundos
1 hora                          3600 segundos
1 dia                       	86400 segundos
1 mês                           (30.44 dias)    2.629.743 segundos
1 ano                           (365.24 dias)   31.556.926 segundos
''')
nanosegundo, microsegundo, milissegundo, segundo, minuto = 1000000000, 1000000, 1000, 9192631770, 60 # 60 segundos.
hora = minuto * 60 # 3.600
dia = hora * 24 # 86.400
mes = dia * 30.44
ano = dia * 365.24
print("\nUm minuto tem \033[0;32m{0:,}\033[m segundos.".format(minuto).replace(",", "."))
print("Uma hora tem \033[0;32m{0:,}\033[m segundos.".format(hora).replace(",", "."))
print("Um dia tem \033[0;32m{0:,}\033[m segundos.".format(dia).replace(",", "."))
print("Um mês tem aproximadamente \033[0;32m{0:,}\033[m segundos.".format(mes).replace(",", "."))
print("Um ano tem aproximadamente \033[0;32m{0:,}\033[m segundos.".format(ano).replace(",", "."))

while True:
    print('''
    Para qual unidade você deseja converter:
    [ 1 ] - Hora
    [ 2 ] - Dia
    [ 3 ] - Mês
    [ 4 ] - Ano
    ''')
    escolha = input('Sua escolha (0 para encerrar): ')
    # Encerrar aplicação.
    if escolha in '0':
        break
    elif escolha == '1':
        horas = float(input('Informe o número de horas: '))
        resultado = horas * hora
        print('{} horas tem {} segundos.'.format(horas, resultado))
    elif escolha == '2':
        dias = int(input('Informe o número de dias: '))
        resultado = dias * dia
        print('{} dias tem {} segundos.'.format(dias, resultado))
    elif escolha == '3':
        meses = int(input('Informe o número de meses: '))
        resultado = meses * mes
        print('{} meses tem {} segundos.'.format(meses, resultado))
    elif escolha == '4':
        anos = int(input('Informe o número de anos: '))
        resultado = anos * ano
        print('{} anos tem {} segundos.'.format(anos, resultado))
    else:
        # Aqui vai o "Tente novamente!"
        escolha != '1, 2, 3, 4'
        print("\n\033[0;31mInformação incorreta, tente novamente.\033[m\n", end=" ")
        continue
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\n\033[0;34mDeseja continuar no programa principal [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")

















