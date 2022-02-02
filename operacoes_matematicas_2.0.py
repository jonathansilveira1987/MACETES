# Operações Matemáticas 2.0.

from time import sleep
from math import radians, sin, cos, tan

while True:
    # Programa principal!
    print('''\033[0;33m
            OPERAÇÕES MATEMÁTICAS
    Escolha abaixo a ferramenta desejada...

    [ 01 ] - Custo de viagem                                                 [ 21 ] - 
    [ 02 ] - Cotação de moeda                                                [ 21 ] - 
    [ 03 ] - Contagem de pares                                               [ 21 ] - 
    [ 04 ] - Contador simples                                                [ 21 ] - 
    [ 05 ] - Comparando números                                              [ 21 ] - 
    [ 06 ] - Ângulo / Seno / Cosseno e Tangente                              [ 21 ] - 
    [ 07 ] - Aumentos múltiplos                                              [ 21 ] - 
    [ 08 ] -                                                                 [ 21 ] - 
    [ 09 ] -                                                                 [ 21 ] - 
    [ 10 ] -                                                                 [ 21 ] - 
    [ 11 ] -                                                                 [ 21 ] - 
    [ 12 ] -                                                                 [ 21 ] - 
    [ 13 ] -                                                                 [ 21 ] - 
    [ 14 ] -                                                                 [ 21 ] - 
    [ 15 ] -                                                                 [ 21 ] - 
    [ 16 ] -                                                                 [ 21 ] - 
    [ 17 ] -                                                                 [ 21 ] - 
    [ 18 ] -                                                                 [ 21 ] - 
    [ 19 ] -                                                                 [ 21 ] - 
    [ 20 ] -                                                                 [ 21 ] - 
    [ 21 ] -                                                                 [ 21 ] - 
    [ 22 ] -                                                                 [ 21 ] - 
    [ 23 ] -                                                                 [ 21 ] - 
    [ 24 ] -                                                                 [ 21 ] - 
    [ 25 ] -                                                                 [ 21 ] - 
    \033[0m''')

    opcao = input("Informe sua escolha desejada (0 para encerrar): ")
    
    # Encerrar aplicação.
    if opcao in '0':
        break
    # Custo de Viagem.
    elif opcao == '01':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Programa principal!
            print('''
Escolha o modo de confecção da porção inteira. 
[ 1 ] - Utilizando "ESCREVA"
[ 2 ] - Utilizando "SE" simplificado / hífen line / operador ternário
''')

            modo = input("Informe o modo desejado (0 para encerrar): ")

            # Encerrar aplicação.
            if modo in '0':
                break
            elif modo == '1':
                # Utilizando "ESCREVA".
                distancia = float(input("\n\033[0;32mDigite a distância da sua viagem: "))
                print("\nVocê está prestes a começar uma viagem de {} km.".format(distancia))
                if distancia <= 200:
                    preco = distancia * 0.50
                else:
                    preco = distancia * 0.45
                print("O preço de sua passagem será de R$ {:.2f}\033[m".format(preco))

            elif modo == '2':
                # Utilizando "SE" simplificado / hífen line / operador ternário.
                distancia = float(input("\n\033[0;33mDigite a distânica da sua viagem: "))
                print("\nVocê está prestes a começar uma viagem de {} km.".format(distancia))
                preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
                print("O preço de sua passagem será de R$ {:.2f}\033[m".format(preco))
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\nContinuar [1 - SIM / 0 - NÃO]? ")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Cotação de moeda.
    elif opcao == '02':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        real = float(input("\nQuanto dinheiro você tem na carteira? R$ "))
        # Atenção, é necessário alterar a cotação de moeda antes de executar o programa.
        dolar = real / 5.25     # Moeda Americana
        euro = real / 6.19      # Moeda Européia
        renminbi = real / 0.81  # Moeda chinesa
        print("Na cotação de hoje com R$ {:.2f} reais você pode comprar: \n".format(real))
        print("-> U$$ {:.2f} Dólares".format(dolar))
        print("-> € {:.2f} Euros".format(euro))
        print("-> ¥ {:.2f} Renminbi Chineses.".format(renminbi))
    # Contagem de pares.
    elif opcao == '03':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        a1 = int(input('\nPonto Inicial: '))
        a2 = int(input('Ponto Final: '))
        for n in range(a1, a2, 2):
            print(n, end=" ")
        print("Acabou!")
    # Contador simples.
    elif opcao == '04':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:  
            c = int(input('\nInforme a quantidade que deseja contar: ')) # Aqui você define até que número será contado.
            count = 0
            for count in range(c + 1):
                print(count)
            resp = " "
            while resp not in "10":
                resp = str(input("\nDeseja continuar [1 - SIM / 0 - NÃO]? ")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Comparando números.
    elif opcao == '05':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        n1 = int(input("\n1º número: "))
        n2 = int(input("2º número: "))

        if n1 > n2:
            print("\nO PRIMEIRO valor é o maior.")
        elif n2 > n1:
            print("\nO SEGUNDO valor é o maior.")
        else:
            print("\nOs dois valores são iguais.")
    # Ângulo / Seno / Cosseno e Tangente.
    elif opcao == '06':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Aqui vai o programa principal!
            angulo = float(input("\nDigite o ângulo que você deseja: "))
            seno = sin(radians(angulo))
            print("\nO ângulo de {:.0f} tem o SENO de {:.2f}.".format(angulo, seno))
            cosseno = cos(radians(angulo))
            print("O ângulo de {:.0f} tem o COSSENO de {:.2f}".format(angulo, cosseno))
            tangente = tan(radians(angulo))
            print("O ângulo de {:.0f} tem a tangente de {:.2f}.".format(angulo, tangente))
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\n\033[0;33mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Aumentos múltiplos.
    elif opcao == '07':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        salario = float(input("\nDigite o salário atual do funcionário: R$ "))
        if salario > 1250:
            reajuste = salario * 0.10
            novo_salario = salario + reajuste
        else:
            salario <= 1250
            reajuste = salario * 0.15
            novo_salario = salario + reajuste
        print("\nO valor de reajuste foi de R$ {:.2f}, portanto o salário após o reajuste é de R$ {:.2f}.".format(reajuste, novo_salario))












    # 
    elif opcao == '08':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;31mA ferramenta escolhida não possui algoritmo!\033[m')
    # 
    elif opcao == '09':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;31mA ferramenta escolhida não possui algoritmo!\033[m')
    # 
    elif opcao == '10':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;31mA ferramenta escolhida não possui algoritmo!\033[m')











    else:
        # Aqui vai o "Tente novamente!"
        opcao != '01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40'
        print("\n\033[0;31mInformação incorreta, tente novamente.\033[m\n", end=" ")
        continue
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\n\033[0;34mDeseja continuar no programa principal [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")