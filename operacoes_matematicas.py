# Operações Matemáticas.

from time import sleep
import math
from math import trunc
import datetime as dt

while True:
    # Programa principal!
    print('''\033[0;34m
            OPERAÇÕES MATEMÁTICAS
    Escolha abaixo a ferramenta desejada...

    [ 01 ] - Soma                                                               [ 21 ] - 
    [ 02 ] - Média                                                              [ 22 ] - 
    [ 03 ] - Tabuada                                                            [ 23 ] - 
    [ 04 ] - Calculadora                                                        [ 24 ] - 
    [ 05 ] - Raíz Quadrada                                                      [ 25 ] - 
    [ 06 ] - Dobro, Triplo & Raíz Quadrada                                      [ 26 ] - 
    [ 07 ] - Antecessor & Sucessor                                              [ 27 ] - 
    [ 08 ] - Metros para cm e mm                                                [ 28 ] - 
    [ 09 ] - Porção inteira                                                     [ 29 ] - 
    [ 10 ] -                                                                    [ 30 ] - 
    [ 11 ] - Aumento de salário                                                 [ 31 ] - 
    [ 12 ] - Calcular desconto                                                  [ 32 ] - 
    [ 13 ] - Calcular pintura                                                   [ 33 ] - 
    [ 14 ] - Calcular tempo de percurso                                         [ 34 ] - 
    [ 15 ] - Calcular IMC - Índice de Massa Corporal                            [ 35 ] - 
    [ 16 ] - Calcular troco                                                     [ 36 ] - 
    [ 17 ] - Fluxo Sequencial - Conversão de medidas (aplicação da regra de 3)  [ 37 ] - 
    [ 18 ] - Calcular área                                                      [ 38 ] - 
    [ 19 ] - Calcular tempo de uma viagem                                       [ 39 ] - 
    [ 20 ] -                                                                    [ 40 ] - Análise de dados
    \033[0m''')

    opcao = input("Informe sua escolha desejada (0 para encerrar): ")
    
    # Encerrar aplicação.
    if opcao in '0':
        break
    # Soma.
    elif opcao == '01':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        a = int(input("\nDigite um valor: "))
        b = int(input("Digite outro valor: "))
        soma = a + b
        print("\nA soma entre {} e {} é {}.".format(a, b, soma))
    # Média.
    elif opcao == '02':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        n1 = float(input("\nDigite a 1ª nota do aluno: "))
        n2 = float(input("Digite a 2ª nota do aluno:  "))
        media = (n1 + n2) / 2
        print("\nA média entre {:.1f} e {:.1f} é {:.1f}.".format(n1, n2, media))
    # Tabuada.
    elif opcao == '03':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Programa principal!
            print('''
Escolha o modo de confecção da tabuada. 
[ 1 ] - Modo Manual
[ 2 ] - Modo Automático
            ''')
            modo = input("\033[0;32mInforme o modo desejado (0 para encerrar): \033[m")
            # Encerrar aplicação.
            if modo in '0':
                break
            elif modo == '1':
                # Modo Manual
                num = int(input("\nDigite um número para visualizar sua tabuada: "))
                print("-" * 15, "|")
                print("{} x {:2} = {}".format(num, 1, num*1))
                print("{} x {:2} = {}".format(num, 2, num*2))
                print("{} x {:2} = {}".format(num, 3, num*3))
                print("{} x {:2} = {}".format(num, 4, num*4))
                print("{} x {:2} = {}".format(num, 5, num*5))
                print("{} x {:2} = {}".format(num, 6, num*6))
                print("{} x {:2} = {}".format(num, 7, num*7))
                print("{} x {:2} = {}".format(num, 8, num*8))
                print("{} x {:2} = {}".format(num, 9, num*9))
                print("{} x {:2} = {}".format(num, 10, num*10))
                print("-" * 15, "|")
            elif modo == '2':
                # Modo automático
                j = int(input("\nDigite o número o qual deseja obter a tabuada correspondente: "))
                x = 0
                print("-" * 15)  
                print("Tabuada de {}".format(j))  
                print("-" * 15)  
                while (x <= 10):
                    print("{1} X {0:2} = {2}".format(x, j, (x * j)))
                    x = x + 1
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\n\033[0;32mContinuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Calculadora.
    elif opcao == '04':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Programa principal!
            print('''
Escolha a versão para uso da calculadora.
[ 1 ] - Versão 1.0
[ 2 ] - Versão 2.0
    ''')
            modo = input("\033[0;32mInforme o modo desejado (0 para encerrar): \033[m")
            # Encerrar aplicação.
            if modo == '0':
                break
            elif modo == '1':
                # Versão 1.0
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
                    print('\n{} + {} = {}.'.format(n1, n2, r))
                elif operacao == '-':
                    r = n1 - n2
                    print('\n{} - {} = {}.'.format(n1, n2, r))
                elif operacao == '*':
                    r = n1 * n2
                    print('\n{} * {} = {}.'.format(n1, n2, r))
                elif operacao == '/':
                    r = n1 / n2
                    print('\n{} / {} = {}.'.format(n1, n2, r))
                else:
                    # Aqui vai o "Tente novamente!"
                    operacao != '+' '-' '*' '/'
                    print("\n\033[0;31mOperação matemática incorreta, tente novamente.\033[m\n", end=" ")
                    continue
            elif modo == '2':
                operador = input('''
+   para Adição
-   para Subtração
*   para Multiplicação
/   para Divisão
Informe a operação matemática desejada (0 para encerrar): ''')
                if operador == "+":
                    num1 = float(input('Valor 1: '))
                    num2 = float(input('Valor 2: '))
                    soma = num1 + num2
                    print(f'\n\033[0;32m{num1} + {num2} = {soma}.\033[m')
                elif operador == "-":
                    num1 = float(input('Valor 1: '))
                    num2 = float(input('Valor 2: '))
                    diferenca = num1 - num2
                    print(f'\n\033[0;32m{num1} - {num2} = {diferenca}.\033[m')
                elif operador == "*":
                    num1 = float(input('Valor 1: '))
                    num2 = float(input('Valor 2: '))
                    produto = num1 * num2
                    print(f'\n\033[0;32m{num1} * {num2} = {produto}.\033[m')
                elif operador == "/":
                    num1 = float(input('Valor 1: '))
                    num2 = float(input('Valor 2: '))
                    if num2 == 0:
                        print("Divisor não pode ser zero")
                        continue
                    produto = num1 / num2
                    print(f'\n\033[0;32m{num1} / {num2} = {produto}.\033[m')
                else:
                    # Aqui vai o "Tente novamente!"
                    operador != '+, -, *, /'
                    print("\n\033[0;31mOperação matemática incorreta, tente novamente.\033[m\n", end=" ")
                    continue
            else:
                modo != '1, 2'
                print('\n\033[0;31mOpção inválida, tente novamente!\033[m')
                continue
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\n\033[0;33mDeseja continuar na calculadora [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break
        print("\033[0;36;1;4m\nVocê optou por finalizar a calculadora!\033[m")
    # Raíz Quadrada.
    elif opcao == '05':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        num = float(input('\nNúmero: '))
        raiz = math.sqrt(num)
        print(f'\nA Raíz Quadrada de {num} é {raiz}.')
    # Dobro, Triplo & Raíz Quadrada.
    elif opcao == '06':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        n = int(input("\nDigite um número: "))
        d = n * 2
        t = n * 3
        r = n ** (1/2)
        rp = pow(n, (1/2)) # Usando função potência.
        print("\nO dobro de {} é: {}.".format(n, d))
        print("O triplo de {} é {}.".format(n, t))
        print("A raiz quadrada de {} é {:.2f}.".format(n, r))
        print("A raiz quadrada de {} é {:.2f}.".format(n, rp))
    # Antecessor & Sucessor.
    elif opcao == '07':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        n = int(input("\nDigite um número inteiro: "))
        a = n - 1
        s = n + 1
        print("Analisando o valor {}, seu antecessor é {} e o sucessor é {}.".format(n, (n-1), (n+1)))
    # Metros para cm e mm.
    elif opcao == '08':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        medida = float(input("\nMetro(s): "))
        cm = medida * 100
        mm = medida * 1000
        print("\nA medida de {} metros corresponde a {:.0f} cm e {:.0f} mm.".format(medida, cm, mm))
    # Porção inteira.
    elif opcao == '09':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Programa principal!
            print('''
Escolha o modo de confecção da porção inteira. 
[ 1 ] - Sem importar módulo
[ 2 ] - Usando função interna "int"
            ''')

            modo = input("\n\033[0;32mInforme o modo desejado (0 para encerrar): \033[m")

            # Encerrar aplicação.
            if modo in '0':
                break
            elif modo == '1':
                # Sem importar módulo.
                num = float(input("\nDigite um valor: "))
                print("O valor digitado foi {} e sua porção inteira é {}.".format(num, trunc(num)))

            elif modo == '2':
                # Usando função interna "int".
                num = float(input("\nDigite um valor: "))
                print("O valor digitado foi {} e sua porção inteira é {}.".format(num, int(num)))
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\n\033[0;32mContinuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # 
    elif opcao == '10':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
    # Aumento de salário.
    elif opcao == '11':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        salario = float(input("\nQual é o valor atual do salário: R$ "))
        reajuste = float(input("Informe o valor de reajuste % : "))
        novo_salario = salario + (salario * reajuste / 100)
        print("\nO salário atual do funcionário é R$ {:.2f}, após {:.0f}% de aumento, passará a receber R$ {:.2f}.".format(salario, reajuste, novo_salario))
    # Calcular desconto.
    elif opcao == '12':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        preco = float(input("\nQual é o preço do produto: R$ "))
        desc = float(input('Desconto % : '))
        novo = preco - (preco * desc / 100)
        valor_desconto = preco - novo
        print("\nO produto que custava R$ {:.2f}, na promoção com desconto de {:.0f}% vai custar R$ {:.2f}.".format(preco, desc, novo))
        print("Você obteve um desconto de R$ {:.2f}.".format(valor_desconto))
    # Calcular pintura.
    elif opcao == '13':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        largura = float(input("\nLargura da parede: "))
        altura = float(input("Altura da parede: "))
        lata = float(input("Quantidade em LITROS da lata de tinta: "))
        area = largura * altura
        print("\nSua parede tem a dimensão de {} x {} e sua área é de {} m².".format(largura, altura, area))
        tinta = area / lata
        print("Para pintar essa parede você precisará de {} litro(s) de tinta.".format(tinta))
    # # Calcular tempo de percurso.
    elif opcao == '14':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Programa principal!
            print('''
        CALCULAR TEMPO DE PERCURSO
[ 1 ] - Informar horário de chegada
[ 2 ] - Informar horário de saída e chegada
            ''')
            opcao = input('Informe a modalidade desejada (0 para encerrar): ')
            # Encerrar aplicação.
            if opcao in '0':
                break
            elif opcao == '1':
                # Calcular tempo de percurso.
                inicio = dt.datetime.now()
                inicio = inicio.strftime('%H:%M:%S')
                fim = input('\nInforme o horário de chegada (exemplo 13:10:20): ')
                horario_inicio = dt.datetime.strptime(inicio, '%H:%M:%S')
                horario_fim = dt.datetime.strptime(fim, '%H:%M:%S')
                diferenca = (horario_fim - horario_inicio) 
                diferenca.seconds/60
                print(f'\n\033[0;33mAgora são {inicio}.\033[m')
                print(f'\033[0;32mO tempo de percurso será de {diferenca}.\033[m')
            elif opcao == '2':
                # Calcular o intervalo de tempo entre duas seqüências de tempo.
                inicio = input('\nInforme o horário de saída (exemplo 13:10:20): ')
                fim = input('Informe o horário de chegada (exemplo 13:10:20): ')
                horario_inicio = dt.datetime.strptime(inicio, '%H:%M:%S')
                horario_fim = dt.datetime.strptime(fim, '%H:%M:%S')
                diferenca = (horario_fim - horario_inicio) 
                diferenca.seconds/60
                print(f'\nO trajeto terá duração de {diferenca}.')
            else:
                # Aqui vai o "Tente novamente!"
                opcao != '1, 2'
                print("\n\033[0;31mERRO! Informação incorreta, tente novamente.\033[m\n", end=" ")
                continue
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\n\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # IMC - Índice de Massa Corporal.
    elif opcao == '15':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            try:
                # Programa principal!
                print('\nIMC - ìndice de Massa Corporal.')
                peso = float(input("\nInforme seu peso (KG): "))
                altura = float(input("Informe sua altura (M): "))
                imc = peso / (altura ** 2) # altura ao quadrado.
                print("\n\033[0;32mO IMC dessa pessoa é de {:.1f}.\033[m".format(imc))
                if imc < 18.5:
                    print("\nVocê está ABAIXO do peso normal.\n")
                elif 18.5 <= imc < 25:
                    print("\nParabéns! Você está na faixa de peso NORMAL.\n")
                elif 25 <= imc < 30:
                    print("\nVocê está com SOBREPESO.")
                elif 30 <= imc < 40:
                    print("\nVocê está em OBESIDADE.\n")
                elif imc >= 40:
                    print("\n\033[0;31mVocê está em OBESIDADE MÓRBIDA, CUIDADO!\033[m\n")
            except ValueError:
                print("\n\033[0;31mERRO! Informação incorreta, tente novamente.\033[m\n", end=" ")
                continue
        # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Calcular troco.
    elif opcao == '16':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Programa principal!
            x = int(input('\nInsira o valor em dinheiro: '))
            print('\nA quantidade de notas de R$ 100,00 é: ', x / 100)
            print('A quantidade de notas de R$ 50,00 é: ', x / 50)
            print('A quantidade de notas de R$ 20,00 é: ', x / 20)
            print('A quantidade de notas de R$ 10,00 é: ', x / 10)
            print('A quantidade de notas de R$ 5,00 é: ', x / 5)
            print('A quantidade de notas de R$ 2,00 é: ', x / 2)
            print('A quantidade de moedas de R$ 0,50 é: ', x / 0.5)
            print('A quantidade de moedas de R$ 0,25 é: ', x / 0.25)
            print('A quantidade de moedas de R$ 0,10 é: ', x / 0.10)
            print('A quantidade de moedas de R$ 0,05 é: ', x / 0.05)
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\n\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Fluxo Sequencial - Conversão de medidas (aplicação da regra de 3)
    elif opcao == '17':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            m = float(input('\nInforme a medida em Metros: '))
            cm = m * 100
            pol = cm / 2.54
            pes = pol / 12
            jar = pes / 3
            mm = m * 1000
            print('\nA medida de \033[0;32m{}\033[m metros, corresponde a...'. format(m))
            print('   - {} centímetros.'.format(round(cm, 2)))
            print('   - {} polegadas.'.format(round(pol, 1)))
            print('   - {} pes.'.format(round(pes, 1)))
            print('   - {} jardas.\n'.format(round(jar, 1)))
            print("   - {:.0f} cm.".format(cm))
            print("   - {:.0f} mm.".format(mm))
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\n\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Calcular área.
    elif opcao == '18':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        def area(larg, comp):
            a = larg * comp
            print(f'\nA área de um terreno {larg} x {comp} é de {a} m².')
        print('\nControle de Terrenos')
        print('-' * 20)
        l = float(input('LARGURA (m): '))
        c = float(input('COMPRIMENTO (m): '))
        area(l, c)
    # Calcular tempo de uma viagem.
    elif opcao == '19':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Programa principal!
            distância = float(input("\nDigite a distância em km: "))
            velocidade_média = float(input("Digite a velocidade média em km/h: "))
            tempo = distância / velocidade_média
            tempo_s = int(tempo * 3600)  # convertemos de horas para segundos
            horas = int(tempo_s / 3600)  # parte inteira
            tempo_s = int(tempo_s % 3600)  # o resto
            minutos = int(tempo_s / 60)
            segundos = int(tempo_s % 60)
            milesimosegundos = int(tempo_s % 60)
            # Imprimir o tempo em horas, minutos, segundos e milésimos de segundos.
            print("\n\033[0;32mO tempo estimado de viagem é de %0d hora(s) %02d minuto(s) %02d segundo(s) & %02d milésimos de segundo(s).\033[m" % (horas, minutos, segundos, milesimosegundos))
            # Imprimir o tempo em horas, minutos, segundos.
            print("\n\033[0;33m%0d hora(s) %02d minuto(s) & %02d segundo(s).\033[m\n" % (horas, minutos, segundos))
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # 
    elif opcao == '20':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
    # 
    elif opcao == '21':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
    # 
    elif opcao == '22':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
    # 
    elif opcao == '23':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
    # 
    elif opcao == '24':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
        # 
    elif opcao == '25':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
        # 
    elif opcao == '26':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
        # 
    elif opcao == '27':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
        # 
    elif opcao == '28':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
        # 
    elif opcao == '29':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
        # 
    elif opcao == '30':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
        # 
    elif opcao == '31':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
        # 
    elif opcao == '32':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
        # 
    elif opcao == '33':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
        # 
    elif opcao == '34':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
        # 
    elif opcao == '35':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
        # 
    elif opcao == '36':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
        # 
    elif opcao == '37':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
        # 
    elif opcao == '38':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
        # 
    elif opcao == '39':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
    # Análise de dados.
    elif opcao == '40':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        a = input("\nDigite algo: ")
        print("O tipo primitivo desse algo é: ", type(a))
        print("Só tem espaços?", a.isspace())
        print("É um número? ", a.isnumeric())
        print("É alfabético? ", a.isalpha())
        print("É alfanumérico? ", a.isalnum())
        print("Está em maiúsculas? ", a.isupper())
        print("Está em minúsculas? ", a.islower())
        print("Está capitalizada? ", a.istitle())






















        
    else:
        # Aqui vai o "Tente novamente!"
        opcao != '01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20'
        print("\n\033[0;31mInformação incorreta, tente novamente.\033[m\n", end=" ")
        continue
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\n\033[0;34mDeseja continuar no programa principal [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")