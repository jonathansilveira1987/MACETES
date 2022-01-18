# Operações Matemáticas.

from time import sleep
import math
from math import trunc
from datetime import date
import datetime as dt
from random import randint

while True:
    # Programa principal!
    print('''\033[0;33m
            OPERAÇÕES MATEMÁTICAS
    Escolha abaixo a ferramenta desejada...

    [ 01 ] - Soma                                                               [ 21 ] - Calcular potenciação
    [ 02 ] - Média                                                              [ 22 ] - Calcular temperaturas
    [ 03 ] - Tabuada                                                            [ 23 ] - Conversor de Bases Numéricas
    [ 04 ] - Calculadora                                                        [ 24 ] - Calcular dias desde nascimento
    [ 05 ] - Raíz Quadrada                                                      [ 25 ] - Calcular idade
    [ 06 ] - Dobro, Triplo & Raíz Quadrada                                      [ 26 ] - Soma sequencial
    [ 07 ] - Antecessor & Sucessor                                              [ 27 ] - 
    [ 08 ] - Metros para cm e mm                                                [ 28 ] - 
    [ 09 ] - Porção inteira                                                     [ 29 ] - Tratando vários valores
    [ 10 ] - Aprovado ou Reprovado                                              [ 30 ] - PAR ou ÍMPAR
    [ 11 ] - Aumento de salário                                                 [ 31 ] - Números primos
    [ 12 ] - Calcular desconto                                                  [ 32 ] - Somar ímpares múltiplos de três
    [ 13 ] - Calcular pintura                                                   [ 33 ] - Soma de pares
    [ 14 ] - Calcular tempo de percurso                                         [ 34 ] - 
    [ 15 ] - Calcular IMC - Índice de Massa Corporal                            [ 35 ] - 
    [ 16 ] - Calcular troco                                                     [ 36 ] - 
    [ 17 ] - Fluxo Sequencial - Conversão de medidas (aplicação da regra de 3)  [ 37 ] - 
    [ 18 ] - Calcular área                                                      [ 38 ] - 
    [ 19 ] - Calcular tempo de uma viagem                                       [ 39 ] - Jogo da Adivinhação
    [ 20 ] - Calcular aluguel de veículo                                        [ 40 ] - Análise de dados
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
[ 1 ] - Versão 1.0
[ 2 ] - Versão 2.0
[ 3 ] - Versão 3.0
[ 4 ] - Versão 4.0
            ''')
            modo = input("\033[0;32mInforme o modo desejado (0 para encerrar): \033[m")
            # Encerrar aplicação.
            if modo in '0':
                break
            elif modo == '1':
                # Versão 1.0
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
                # Versão 2.0
                j = int(input("\nDigite o número o qual deseja obter a tabuada correspondente: "))
                x = 0
                print("-" * 15)  
                print("Tabuada de {}".format(j))  
                print("-" * 15)  
                while (x <= 10):
                    print("{1} X {0:2} = {2}".format(x, j, (x * j)))
                    x = x + 1
            elif modo == '3':
                # Versão 3.0
                while True:
                    n = int(input("\nQuer ver a tabuada de qual valor: "))
                    if n < 0:
                        break
                    print("-" * 30)
                    for c in range(1, 11):
                        print(f"{n} X {c:2} = {n*c}")
                    print("-" * 30)
                    break
            elif modo == '4':
                # Versão 4.0
                try:
                    # Programa principal!
                    num = int(input("\nDigite um número para visualizar sua tabuada: "))
                    print("-" * 15, "|")
                    for c in range(1, 11):
                        print("{} x {:2} = {}".format(num, c, num * c))
                    print("-" * 15, "|")
                except ValueError:
                    print("\n\033[0;31mERRO! Informação incorreta, tente novamente.\033[m", end=" ")
                    continue
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\n\033[0;32mContinuar na calculadora [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
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

            modo = input("\033[0;32mInforme o modo desejado (0 para encerrar): \033[m")

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
    # Aprovado ou Reprovado.
    elif opcao == '10':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Programa principal!
            nota1 = float(input("\n1ª nota: "))
            nota2 = float(input("2ª nota: "))
            media = (nota1 + nota2) / 2
            print("\nTirando {:.1f} e {:.1f}. a média do aluno é {:.1f}.".format(nota1, nota2, media))
            if 7 > media >= 5:
                print("O aluno está em \033[0;33mRECUPERAÇÃO\033[m.\n")
            elif media < 5:
                print("O aluno está \033[0;31mREPROVADO\033[m.\n")
            elif media >= 7:
                print("O aluno está \033[0;32mAPROVADO\033[m.\n")
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
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
    # Calcular aluguel de veículo.
    elif opcao == '20':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Aqui vai o programa principal!
            dias = int(input("\nQuantos dias alugado? "))
            km = float(input("Quantos kilômetros rodados? "))
            pago = (dias * 60) + (km * 0.15)
            print("\nO total a pagar pelo aluguel do veículo é de R$ {:.2f}".format(pago))
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\n\033[0;33mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Calcular Potenciação.
    elif opcao == '21':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Programa principal!
            n = int(input('\nNúmero/Base: '))
            p = int(input('Potência/Expoente: '))
            resultado = n ** p
            # Fórmulas.
            # print('\n{}'.format(round(resultado, 1)))
            result = resultado = '\n{0:,}\n'.format(resultado).replace(',','.') #Aqui coloca os pontos
            print(result)
            # print("\n{0:.50f}\n".format(round(resultado)))
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Calcular temperaturas.
    elif opcao == '22':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Aqui vai o programa principal!
            def celtokel(C): # Celsius para Kelvin
                K = (C + 273.15)
                return ('\n{K:.2f}K' .format(K = K))

            def celtofah(C): # Celsius para Fahrenheit
                F = (C * 1.8 + 32)
                return('\n{F:.2f}°F' .format(F = F))

            def keltocel(K): # Kelvin para Celsius
                C = (K - 273.15)
                return ('\n{C:.2f}°C' .format(C = C))

            def keltofah(K): # Kelvin para Fahrenheit
                F = (K * 1.8 - 459.7)
                return('\n{F:.2f}°F' .format(F = F))

            def fahtocel(F): # Fahrenheit para Celsius
                C = ((F -32) / 1.8)
                return ('\n{C:.2f}°C' .format(C = C))

            def fahtokel(F): # Fahrenheit para Kelvin
                K = ((F - 32) / 1.8 + 273)
                return ('\n{K:.2f}K' .format(K = K))

            def menu():
                escolha = int(input('''
Menu:
1 - Celsius para Kelvin
2 - Celsius para Fahrenheit
3 - Kelvin para Celsius
4 - Kelvin para Fahrenheit
5 - Fahrenheit para Celsius
6 - Fahrenheit para Kelvin
7 - Sair

Escolha: '''))
                if escolha == 1:
                    print(celtokel(int(input('Valor em °C(celsius) para ser convertido em K(Kelvin): '))))
                elif escolha ==2:
                    print(celtofah(int(input('Valor em °C(Celsius) para ser convertido em °F(Fahrenheit): '))))
                elif escolha == 3:
                    print(keltocel(int(input('Valor em K(Kelvin) para ser convertido em °C(Celsius): '))))
                elif escolha == 4:
                    print(keltofah(int(input('Valor em K(Kelvin) para ser convertido em °F(Fahrenheit): '))))
                elif escolha == 5:
                    print(fahtocel(int(input('Valor em °F(Fahrenheit) para ser convertido em °C(celsius): '))))
                elif escolha == 6:
                    print(fahtokel(int(input('Valor em °F(Fahrenheit) para ser convertido em K(Kelvin): '))))
                elif escolha == 7:
                    exit()
                else:
                    print('\nEscolha Inválida')
                    menu()
            menu()
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\n\033[0;33mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Conversor de Bases Numéricas.
    elif opcao == '23':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Programa principal.
            try:    
                print('\nCONVERSOR DE BASES NUMÉRICAS.')
                num = int(input("Digite um número inteiro: "))

                print('''
Escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')

                opcao = int(input("\nSua opção: "))

                if opcao == 1:
                    print("\n{} convertido para BINÁRIO é igual a \033[0;32m{}\033[m.\n".format(num, bin(num)[2:]))
                elif opcao == 2:
                    print("\n{} convertido para OCTAL é igual a \033[0;32m{}\033[m.\n".format(num, oct(num)[2:]))
                elif opcao == 3:
                    print("\n{} convertido para HEXADECIMAL é igual a \033[0;32m{}\033[m.\n".format(num, hex(num)[2:]))
                else:
                    print("\n\033[0;31mOpção inválida. Tente novamente.\033[m")
                    continue
            except ValueError:
                print("\n\033[0;31mERRO! Informação incorreta, tente novamente.\033[m\n", end=" ")
                continue
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\033[0;33mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Calcular dias desde nascimento.
    elif opcao == '24':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Programa principal!
            dia = int(input('\n\033[0;31mDia de Nascimento: \033[m'))
            mes = int(input('\033[0;31mMês de Nascimento: \033[m'))
            ano = int(input('\033[0;31mAno de Nascimento: \033[m'))

            dias = date.today() - date(ano, mes, dia)

            # print(f'\nJá se passaram \033[0;33m{dias.days}\033[m dias desde seu nascimento.')
            print("\nJá se passaram \033[0;34m{0:,}\033[m dias desde seu nascimento.\n".format(dias.days).replace(",", "."))
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Calcular Idade.
    elif opcao == '25':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Programa principal!
            current_date = date.today()
            data_nascimento= int(input("\nAno de nascimento: "))
            data_actual = current_date.year
            idade = data_actual - data_nascimento
            print('\nNesse ano você completa(ou) \033[0;33m{}\033[m ano(s).\n'.format(idade))
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Soma sequencial.
    elif opcao == '26':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
                    # Programa principal!
                    print('''
    SOMA SEQUENCIAL
[ 1 ] - Versão 1.0
[ 2 ] - Versão 2.0
            ''')

                    modo = input("Informe a versão desejada (0 para encerrar): ")

                    # Encerrar aplicação.
                    if modo in '0':
                        break
                    elif modo == '1':
                        # Versão 1.0
                        soma = cont = 0
                        while True:
                            num = int(input("\nDigite um valor (\033[0;32m999\033[m para executar a operação): "))
                            if num == 999:
                                break
                            cont = cont + 1
                            soma = soma + num
                        print("\nA soma dos {} valores foi {}.".format(cont, soma))
                    elif modo == '2':
                        # Versão 2.0
                        v = sm = nv = 0
                        while v != 999:
                            v = int(input("\nDigite um valor (\033[0;32m999\033[m para executar a operação): "))
                            if v != 999:
                                sm += v
                                nv += 1
                        print(f"\nO total de valores digitados foi de {nv}.")
                        print(f"A soma entre eles é {sm}.")
                    # Aqui vai o "Deseja continuar?"
                    resp = " "
                    while resp not in "10":
                        resp = str(input("\n\033[0;32mContinuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
                    if resp == "0":
                        break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")












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
    # Tratando vários valores.
    elif opcao == '29':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Aqui vai o programa principal!
            num = cont = soma = 0
            num = int(input("\nDigite um número [\033[0;31m999 para TRATAR\033[m]: "))
            while num != 999:    
                soma += num
                cont += 1
                num = int(input("Digite um número [\033[0;31m999 para TRATAR\033[m]: "))
            print("\nVocê digitou {} números e a soma entre eles foi \033[0;32m{:.2f}\033[m.".format(cont, soma))
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\n\033[0;33mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")

















        # PAR ou ÍMPAR.
    elif opcao == '30':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Programa principal!
            print('''
        PAR OU ÍMPAR
[ 1 ] - Verificar se número é PAR ou ÍMPAR
[ 2 ] - Jogar PAR ou ÍMPAR com seu computador
            ''')
            opcao = input('Informe a modalidade desejada (0 para encerrar): ')
            # Encerrar aplicação.
            if opcao in '0':
                break
            elif opcao == '1':
                # Verificar se número é PAR ou ÍMPAR
                while True:
                    try:
                        # Programa principal!
                        n = int(input("\nDigite um número qualquer: "))
                        resultado = n % 2
                        if resultado == 0: # O resto da divisão de qualquer número par por 2 é "0" e qualquer número ímpar por 2 é "1".
                            print("\nO número \033[0;31m{}\033[m é PAR.\n".format(n))
                        else:
                            print("\nO número \033[0;31m{}\033[m é ÍMPAR.\n".format(n))
                    except ValueError:
                        print("\n\033[0;31mERRO! Informação incorreta, tente novamente.\033[m\n", end=" ")
                        continue
                # Aqui vai o "Deseja continuar?"
                    resp = " "
                    while resp not in "10":
                        resp = str(input("\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
                    if resp == "0":
                        break    
                print("\033[0;36;1;4m\nVocê optou por finalizar a consulta PAR ou ÍMPAR!\033[m")
            elif opcao == '2':
                # Jogar PAR ou ÍMPAR com seu computador
                v = 0
                while True:
                    jogador = int(input("Informe um valor: "))
                    computador = randint(0, 10)
                    total = jogador + computador
                    tipo = " "
                    while tipo not in "PI":
                        tipo = str(input("Par ou Ímpar [P para PAR / I para ÍMPAR]? ")).strip().upper()[0]
                    print(f"Você jogou {jogador} e o computador {computador}. Total de {total}.")
                    if tipo == "P":
                        if total % 2 == 0:
                            print("VOCÊ VENCEU!")
                            v = v + 1
                        else:
                            print("VOCÊ PERDEU!")
                            break
                    elif tipo == "I":
                        if total % 2 == 1:
                            print("VOCÊ VENCEU!")
                            v = v + 1
                        else:
                            print("VOCÊ PERDEU!")
                            break
                        print("Vamos jogar novamente...")
                print(f"GAME OVER! Você venceu {v} vezes.")
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
    # Números primos.
    elif opcao == '31':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Programa principal!
            num = int(input("\nDigite um número: "))
            print('\n')
            tot = 0
            for c in range(1, num + 1):
                if num % c == 0:
                    print("\033[33m", end="")
                    tot += 1
                else:
                    print("\033[31m", end="")
                print("{}".format(c), end=" ")
            print('\n')
            print("\n\033[mO número {} foi divisível {} vezes.".format(num, tot))
            if tot == 2:
                print("\nE por isso ele É PRIMO!")
            else:
                print("\nE por isso ele NÃO É PRIMO!")
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\n\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Somar ímpares múltiplos de três.
    elif opcao == '32':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        soma = 0
        cont = 0
        for c in range(1, 501, 2):
            if c % 3 == 0:
                cont += 1
                soma += c
        print("\nA soma de todos os {} valores solicitados é {}.".format(cont, soma))
    # Soma de pares.
    elif opcao == '33':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        soma = 0
        cont = 0
        for c in range(1, 7):
            num = int(input("\nDigite o {}º valor: ".format(c)))
            if num % 2 == 0:
                soma = soma + num
                cont = cont + 1
        print("\n\033[0;35mVocê informou {} números PARES e a soma deles foi {}.\033[m".format(cont, soma))
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
    # Jogo da Adivinhação.
    elif opcao == '39':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Aqui vai o programa principal!
            computador = randint(0, 10)
            print("\nSou seu computador... Acabei de pensar em um número entre 0 e 10.")
            sleep(3)
            print("Será que você consegue adivinhar qual foi? ")
            sleep(3)
            acertou = False
            palpites = 0
            while not acertou:
                jogador = int(input("\nQual é o seu palpite? "))
                palpites += 1
                if jogador == computador:
                    acertou = True
                else:
                    if jogador < computador:
                        print("\nMais... Tente mais uma vez.")
                    elif jogador > computador:
                        print("\nMenos... Tente mais uma vez.")
            print("\n\033[0;32mAcertou com {} tentativas. Parabéns!\033[m".format(palpites))
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\n\033[0;33mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
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