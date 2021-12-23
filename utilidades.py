# Utilidades.

from time import sleep
from math import trunc
import math

while True:
    # Programa principal!
    print('''
    Pacote de Ferramentas!
    Escolha abaixo a ferramenta desejada...\n 
    [ 01 ] - Apresentação                    [ 11 ] - Aumento de salário
    [ 02 ] - Soma                            [ 12 ] - Porção inteira
    [ 03 ] - Análise de dados                [ 13 ] - Operações matemáticas
    [ 04 ] - Antecessor & Sucessor           [ 14 ] - Imprimir na tela
    [ 05 ] - Dobro, Triplo & Raíz Quadrada   [ 15 ] - 
    [ 06 ] - Média                           [ 16 ] - 
    [ 07 ] - Metros para cm e mm             [ 17 ] - 
    [ 08 ] - Tabuada                         [ 18 ] - 
    [ 09 ] - Calcular pintura                [ 19 ] - 
    [ 10 ] - Calcular desconto               [ 20 ] - 
    ''')

    opcao = input("Informe sua escolha desejada (0 para encerrar): ")

    # Encerrar aplicação.
    if opcao in '0':
        break
    # Apresentação.
    elif opcao == '01':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        nome = input("\nDigite seu nome: ")
        print("\nÉ um prazer te conhecer, {}!".format(nome))
    # Soma.
    elif opcao == '02':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        a = int(input("\nDigite um valor: "))
        b = int(input("Digite outro valor: "))
        soma = a + b
        print("\nA soma entre {} e {} é: {}.".format(a, b, soma))
    # Análise de dados.
    elif opcao == '03':
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
    # Antecessor & Sucessor.
    elif opcao == '04':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        n = int(input("\nDigite um número inteiro: "))
        a = n - 1
        s = n + 1
        print("Analisando o valor {}, seu antecessor é {} e o sucessor é {}.".format(n, (n-1), (n+1)))
    # Dobro, Triplo & Raíz Quadrada.
    elif opcao == '05':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        n = int(input("\nDigite um número: "))
        d = n * 2
        t = n * 3
        r = n ** (1/2)
        rp = pow(n, (1/2)) # Usando função potência.
        print("\nO dobro de {} é: {}.".format(n, d))
        print("O triplo de {} é: {}.".format(n, t))
        print("A raiz quadrada de {} é: {:.2f}.".format(n, r))
        print("A raiz quadrada de {} é: {:.2f}.".format(n, rp))
    # Média.
    elif opcao == '06':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        n1 = float(input("\nDigite a 1ª nota do aluno: "))
        n2 = float(input("Digite a 2ª nota do aluno:  "))
        media = (n1 + n2) / 2
        print("\nA média entre {:.1f} e {:.1f} é: {:.1f}!".format(n1, n2, media))
    # Metros para cm e mm.
    elif opcao == '07':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        medida = float(input("\nMetro(s): "))
        cm = medida * 100
        mm = medida * 1000
        print("\nA medida de {} metros corresponde a {:.0f} cm e {:.0f} mm.".format(medida, cm, mm))
    # Tabuada.
    elif opcao == '08':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:
            # Programa principal!
            print('''
        Escolha o modo de confecção da tabuada. 
        [ 1 ] - Modo Manual
        [ 2 ] - Modo Automático
            ''')

            modo = input("\n\033[0;32mInforme o modo desejado (0 para encerrar): \033[m")

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
    # Calcular pintura.
    elif opcao == '09':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        largura = float(input("\nLargura da parede: "))
        altura = float(input("Altura da parede: "))
        lata = float(input("Quantidade em LITROS da lata de tinta: "))
        area = largura * altura
        print("\nSua parede tem a dimensão de {} x {} e sua área é de {} m².".format(largura, altura, area))
        tinta = area / lata
        print("Para pintar essa parede você precisará de {} litro(s) de tinta.".format(tinta))
    # Calcular desconto.
    elif opcao == '10':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        preco = float(input("\nQual é o preço do produto: R$ "))
        desc = float(input('Desconto % : '))
        novo = preco - (preco * desc / 100)
        valor_desconto = preco - novo
        print("\nO produto que custava R$ {:.2f}, na promoção com desconto de {:.0f}% vai custar R$ {:.2f}.".format(preco, desc, novo))
        print("Você obteve um desconto de R$ {:.2f}.".format(valor_desconto))
    # Aumento de salário.
    elif opcao == '11':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        salario = float(input("\nQual é o valor atual do salário: R$ "))
        reajuste = float(input("Informe o valor de reajuste % : "))
        novo_salario = salario + (salario * reajuste / 100)
        print("\nO salário atual do funcionário é R$ {:.2f}, após {:.0f}% de aumento, passará a receber R$ {:.2f}.".format(salario, reajuste, novo_salario))
    # Porção inteira.
    elif opcao == '12':
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
    # Operações matemáticas.
    elif opcao == '13':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        while True:

            operador = input('''
+   para Adição
-   para Subtração
*   para Multiplicação
/   para Divisão
rq  para Raíz quadrada
bh  para Bhaskara

Informe a operação matemática desejada (0 para encerrar): ''')

            if operador == "+":
                num1 = float(input('Valor 1: '))
                num2 = float(input('Valor 2: '))
                soma = num1 + num2
                print('Resultado = ', soma)
            elif operador == "-":
                num1 = float(input('Valor 1: '))
                num2 = float(input('Valor 2: '))
                diferenca = num1 - num2
                print('Resultado = ', diferenca)
            elif operador == "*":
                num1 = float(input('Valor 1: '))
                num2 = float(input('Valor 2: '))
                produto = num1 * num2
                print('Resultado = ', produto)
            elif operador == "/":
                num1 = float(input('Valor 1: '))
                num2 = float(input('Valor 2: '))
                if num2 == 0:
                    print("Divisor não pode ser zero")
                    continue
                produto = num1 / num2
                print('Resultado = ', produto)
            # Raíz Quadrada.
            elif operador == "rq":
                num = float(input('Número: '))
                raiz = math.sqrt(num)
                print('Resultado = ', raiz)
            # Bhaskara.
            elif operador == "bh":
                a = float(input('Delta 1: '))
                b = float(input('Delta 2: '))
                c = float(input('Delta 3: '))
                delta = b * b - 4 * a * c
                if delta < 0:
                    print("Não há raízes reais")
                    continue
                elif delta == 0:
                    print("Há uma raiz distinta apenas")
                else:
                    print("Há duas raízes distintas")
                x1 = (-b + math.sqrt(delta)) / (2 * a)
                x2 = (-b - math.sqrt(delta)) / (2 * a)
                print(f"As raízes são {x1} e {x2}")
            elif operador == "0":
                break
            else:
                print("\n\033[0;31mOperação inválida, tente novamente!\033[m")
    # Imprimir na tela.
    elif opcao == '14':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        # print("Hello world")
        a = input('\nDigite o que você deseja imprimir na tela: ')
        print('Você digitou: ', a)




    # 
    elif opcao == '15':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
    # 
    elif opcao == '16':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
    # 
    elif opcao == '17':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
    # 
    elif opcao == '18':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
    # 
    elif opcao == '19':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')
    # 
    elif opcao == '20':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        print('\n\033[0;32mDesculpe, ainda não há algoritmo disponível para essa opção.\033[m')


















































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






































'''

Modelo de formatação!!

    # MegaByte.
    elif opcao == '3':
        megabyte = 1 * 1024
        byte = 2 ** 20
        bit = (2 ** 20) * 8
        print('Calculando...')
        sleep(3)
        print("\033[0;32m\n-> 1 Megabyte possui {0:,} Kilobytes.\033[m".format(megabyte).replace(",", "."))
        sleep(3)
        print("\033[0;33m-> 1 Megabyte possui {0:,} Bytes.\033[m".format(byte).replace(",", "."))
        sleep(3)
        print("\033[0;34m-> 1 Megabyte possui {0:,} Bits.\033[m\n".format(bit).replace(",", "."))
        sleep(3)
        print("Abaixo segue número lido por extenso...")
        sleep(3)
        print("\033[0;31m8 milhões .388 mil .608 bits.\033[m\n")




'''