# Operações Matemáticas 2.0.

from time import sleep
from math import radians, sin, cos, tan
import datetime as dt
from math import factorial
import datetime

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
    [ 08 ] - Bháskara                                                        [ 21 ] - 
    [ 09 ] - Prefixo binário                                                 [ 21 ] - 
    [ 10 ] - Boletim com listas compostas                                    [ 21 ] - 
    [ 11 ] - Simulador de caixa eletrônico                                   [ 21 ] - 
    [ 12 ] - Calcular atmosferas                                             [ 21 ] - 
    [ 13 ] - Calcular segundos                                               [ 21 ] - 
    [ 14 ] - Calcular circunferência                                         [ 21 ] - 
    [ 15 ] - Calcular densidade                                              [ 21 ] - 
    [ 16 ] - Calcular duração de um processo                                 [ 21 ] - 
    [ 17 ] - Calcular Fatorial                                               [ 21 ] - 
    [ 18 ] - Calcular empréstimo habitacional                                [ 21 ] - 
    [ 19 ] - Contar data                                                     [ 21 ] - 
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
    # Bháskara.
    elif opcao == '08':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        a = float(input('\nEntre com o valor de a: '))
        b = float(input('Entre com o valor de b: '))
        c = float(input('Entre com o valor de c: '))

        delta = (b ** 2) - 4 * a * c

        print("\n**************************\n")

        if a == 0:
            print("\nO valor de a, deve ser diferente de 0\n")
        elif delta < 0:
            print("Sem raízes reais.")
        else:
            x1 = (-b + delta ** (1 / 2)) / (2 * a)
            x2 = (-b - delta ** (1 / 2)) / (2 * a)

            print("X1: {}".format(x1))
            print("X2: {}".format(x2))
    # Prefixo Binário.
    elif opcao == '09':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)

        a = 2 ** 0
        b = 2 ** 10
        c = 2 ** 20
        d = 2 ** 30
        e = 2 ** 40
        f = 2 ** 50
        g = 2 ** 60
        h = 2 ** 70
        i = 2 ** 80
        print("\nPrefixo Binário.")
        print("{0:,}".format(a).replace(",", "."))
        print("{0:,}".format(b).replace(",", "."))
        print("{0:,}".format(c).replace(",", "."))
        print("{0:,}".format(d).replace(",", "."))
        print("{0:,}".format(e).replace(",", "."))
        print("{0:,}".format(f).replace(",", "."))
        print("{0:,}".format(g).replace(",", "."))
        print("{0:,}".format(h).replace(",", "."))
        print("{0:,}\n".format(i).replace(",", "."))

        a = 10 ** 0
        b = 10 ** 3
        c = 10 ** 6
        d = 10 ** 9
        e = 10 ** 12
        f = 10 ** 15
        g = 10 ** 18
        h = 10 ** 21
        i = 10 ** 24
        print("Prefixo do Sistema Internacional de Unidades.")
        print("{0:,}".format(a).replace(",", "."))
        print("{0:,}".format(b).replace(",", "."))
        print("{0:,}".format(c).replace(",", "."))
        print("{0:,}".format(d).replace(",", "."))
        print("{0:,}".format(e).replace(",", "."))
        print("{0:,}".format(f).replace(",", "."))
        print("{0:,}".format(g).replace(",", "."))
        print("{0:,}".format(h).replace(",", "."))
        print("{0:,}\n".format(i).replace(",", "."))

        a = (2 ** 0) * 8
        b = (2 ** 10) * 8
        c = (2 ** 20) * 8
        d = (2 ** 30) * 8
        e = (2 ** 40) * 8
        f = (2 ** 50) * 8
        g = (2 ** 60) * 8
        h = (2 ** 70) * 8
        i = (2 ** 80) * 8
        print("Valor de BITS em cada unidade de medida computacional:")
        print("{0:,}".format(a).replace(",", "."))
        print("{0:,}".format(b).replace(",", "."))
        print("{0:,}".format(c).replace(",", "."))
        print("{0:,}".format(d).replace(",", "."))
        print("{0:,}".format(e).replace(",", "."))
        print("{0:,}".format(f).replace(",", "."))
        print("{0:,}".format(g).replace(",", "."))
        print("{0:,}".format(h).replace(",", "."))
        print("{0:,}".format(i).replace(",", "."))
    # Boletim com listas compostas.
    elif opcao == '10':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
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
    # Simulador de Caixa Eletrônico.
    elif opcao == '11':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print("=" * 30)
        print("{:^30}".format("BANCO DO DESENVOLVEDOR"))
        print("=" * 30)

        valor = int(input("\nQue valor você deseja sacar? R$ "))

        total = valor
        cedula = 50
        totcedula = 0

        while True:
            if total >= cedula:
                total = total - cedula
                totcedula = totcedula + 1

            else:
                if totcedula > 0:
                    print(f"Total de {totcedula} cédulas de R$ {cedula}.")
                if cedula == 50:
                    cedula = 20
                elif cedula == 20:
                    cedula = 10
                elif cedula == 10:
                    cedula = 2
                totcedula = 0
                if total == 0:
                    break
                
        print("=" * 30)
        print("\nVOLTE SEMPRE AO BANCO DO DESENVOLVEDOR.")
        print("Tenha um excelente dia!")
    # Calcular Atmosferas.
    elif opcao == '12':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Programa principal!
            atm = 101.325 # A pressão atmosférica ao nível do mar é equivalente a uma força de 101.325 N a cada m² de superfície.
            n = float(input('\nInforme o número de atmosferas: '))
            pa = n * atm
            print(f'\n\033[0;32m{n}\033[m atmosferas equivalem a \033[0;32m{pa} kg\033[m de pressão para cada m².\n')
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Calcular Segundos.
    elif opcao == '13':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
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
                result = '{0:,}'.format(resultado).replace(',','.') #Aqui coloca os pontos
                print(f'{horas} hora(s) tem {result} segundos.')
            elif escolha == '2':
                dias = int(input('Informe o número de dias: '))
                resultado = dias * dia
                # print('{} dias tem {} segundos.'.format(dias, resultado))
                result = '{0:,}'.format(resultado).replace(',','.') #Aqui coloca os pontos
                print(f'{dias} dia(s) tem {result} segundos.')
            elif escolha == '3':
                meses = int(input('Informe o número de meses: '))
                resultado = meses * mes
                # print('{} meses tem {} segundos.'.format(meses, resultado))
                result = '{0:,}'.format(resultado).replace(',','.') #Aqui coloca os pontos
                print(f'{meses} mes(es) tem {result} segundos.')
            elif escolha == '4':
                anos = int(input('Informe o número de anos: '))
                resultado = anos * ano
                # ('{} anos tem {} segundos.'.format(anos, resultado))
                result = '{0:,}'.format(resultado).replace(',','.') #Aqui coloca os pontos
                print(f'{anos} ano(s) tem {result} segundos.')
            else:
                # Aqui vai o "Tente novamente!"
                escolha != '1, 2, 3, 4'
                print("\n\033[0;31mInformação incorreta, tente novamente.\033[m\n", end=" ")
                continue
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\n\033[0;34mDeseja continuar no programa de contagem de segundos [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Calcular circunferência.
    elif opcao == '14':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        raio = float(input('\nEntre com o valor do raio, para obter a circuferência do círculo: '))
        circunferencia = 2 * 3.14 * raio
        print('\nA circunferência do círculo é {:.2f}.'.format(circunferencia))
        print(f'Um círculo com raio de {raio} tem circunferência de {circunferencia}.')
    # Calcular Densidade.
    elif opcao == '15':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
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
\033[m''')

            unidade = int(input("\033[0;32mInforme a opção desejada (0 para encerrar) >\033[m "))

            # Encerrar aplicação.
            if unidade == 0:
                break
            # Densidade em g/mL?
            elif unidade == 1:
                print('\nDensidade em g/mL...')
                soluto = float(input('Massa do soluto: '))
                solvente = float(input('Massa do solvente: '))
                solucao = float(input('Solução: '))
                m = ((soluto + solvente) / solucao)
                print('\nA densidade é: \033[0;31m{:.1f}\033[m g/mL'.format(m))
            # Massa em KG?
            elif unidade == 2:
                print('\nMassa em KG...')
                d = float(input('Densidade: '))
                v = float(input('Volume: '))
                m = ((d * v) / 1000)
                print('\nA densidade é: \033[0;31m{:.4f}\033[m KG'.format(m))
            # Volume em cm³?
            elif unidade == 3:
                print('\nVolume em cm³...')
                d = float(input('Densidade: '))
                m = float(input('Massa: '))
                v = m / d
                print('\nA densidade é: \033[0;31m{:.3f}\033[m cm³'.format(v))
            resp = " "
            while resp not in "10":
                resp = str(input("\nDeseja continuar [1 - SIM / 0 - NÃO]? ")).strip().upper()[0]
            if resp == "0":
                break
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Calcular duração de um processo.
    elif opcao == '16':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Programa principal!
            qpd = int(input('\nQuantidade produzida: '))  # qpd = Quantidade Produzida
            qpg = int(input('Quantidade programada: '))  # qpg = Quantidade Programada
            qrs = qpg - qpd  # qrs = Quantidade Restante
            qpc = qrs / 550  # qpc = Quantidade por Carro
            mrs = int(qpc * 18)  # mrs = Minutos Restantes
            if mrs > 60:
                hora = mrs // 60  # hora = Horas até o término da solução
                minuto = mrs % 60  # minuto = Minuto até o término da solução
                print(f'Faltam, aproximadamente, {hora} horas e {minuto} minutos para'
                    ' o término da solução.')
            else:
                print(f'Faltam, aproximadamente, {mrs} minutos para'
                    ' o término da solução.')
            hora_atual = dt.datetime.now()
            hora_final = hora_atual + dt.timedelta(minutes = mrs)
            hora_atual = hora_atual.strftime("%H:%M:%S")
            hora_final = hora_final.strftime("%H:%M:%S")
            print(f"\n\033[0;33mA hora atual é {hora_atual}.\033[m")
            print(f"\033[0;32mO horário final do processo é {hora_final}.\033[m\n")
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")
    # Calcular Fatorial.
    elif opcao == '17':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\nUtilizando Módulo')
        n = int(input("Digite um número para calcular seu Fatorial: "))
        f = factorial(n)
        # print("O Fatorial de {} é {}.".format(n, f))
        result = '{0:,}'.format(f).replace(',','.') #Aqui coloca os pontos
        print(f'\nO Fatorial de {n} é \033[0;32m{result}\033[m.')

        print('\nModo Tradicional')
        n = int(input("Digite um número para calcular seu Fatorial: "))
        c = n
        f = 1
        print()
        print("Calculando {}! = ".format(n), end=" ")
        while c > 0:
            print("{}".format(c), end=" ")
            print("X" if c > 1 else "=", end=" ")
            f *= c
            c -= 1
        # print("{}.".format(f))
        resultado = '\n\033[0;33m{0:,}\033[m'.format(f).replace(',','.') #Aqui coloca os pontos
        print(resultado)
    # Calcular Empréstimo Habitacional.
    elif opcao == '18':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        valor_casa = float(input("\nInforme o valor do imóvel: R$ "))
        salario_comprador = float(input("Informe o salário do comprador: R$ "))
        anos = int(input("Infome em quantos anos o imóvel será pago: "))
        prestacao = valor_casa / (anos * 12)
        minimo = salario_comprador * 30 / 100
        print("\nPara pagar uma casa de R$ {:.2f} em {:.0f} anos.".format(valor_casa, anos))
        print("O valor da prestação será de R$ {:.2f}.".format(prestacao))
        if prestacao <= minimo:
            print("\n\033[0;32mEmpréstimo pode ser CONCEDIDO!\033[m")
        else:
            print("\n\033[0;31mEmpréstimo NEGADO!\033[m")
            print("\n\033[0;33mCOMPARANDO: Tem que pagar R$ {:.2f} e o mínimo é de R$ {:.2f}.\033[m".format(prestacao, minimo))
    # Contar Data.
    elif opcao == '19':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Aqui vai o programa principal!
            a1 = int(input('\n\033[0;32mDia de Nascimento: \033[m'))
            a2 = int(input('\033[0;32mMês de Nascimento: \033[m'))
            a3 = int(input('\033[0;32mAno de Nascimento: \033[m'))
            a4 = datetime.datetime(a3,a2,a1)
            a5 = datetime.datetime.now()

            diff = a5 - a4

            days = diff.days
            years, days = days // 365, days % 365
            months, days = days // 30, days % 30

            seconds = diff.seconds
            hours, seconds = seconds // 3600, seconds % 3600
            minutes, seconds = seconds // 60, seconds % 60
            print("\n\033[0;31mDesde {}/{}/{} passaram-se {} anos, {} meses, {} dias, {} horas, {} minutos e {} segundos.\033[0m".format(a1, a2, a3, years, months, days, hours, minutes, seconds))
            # Aqui vai o "Deseja continuar?"
            resp = " "
            while resp not in "10":
                resp = str(input("\n\033[0;33mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
            if resp == "0":
                break    
        print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")





    # 
    elif opcao == '20':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
































    # 
    elif opcao == '21':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;31mA ferramenta escolhida não possui algoritmo!\033[m')
    # 
    elif opcao == '22':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;31mA ferramenta escolhida não possui algoritmo!\033[m')
    # 
    elif opcao == '23':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;31mA ferramenta escolhida não possui algoritmo!\033[m')
    # 
    elif opcao == '24':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;31mA ferramenta escolhida não possui algoritmo!\033[m')
    # 
    elif opcao == '25':
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