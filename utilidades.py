# Utilidades Gerais.

from time import sleep
from math import trunc

while True:
    # Programa principal!
    print('''
    Pacote de Ferramentas Gerais!
    Escolha abaixo a ferramenta desejada...\n 
    [ 1 ] - Apresentação                    [ 11 ] - Aumento de salário
    [ 2 ] - Soma                            [ 12 ] - Porção inteira
    [ 3 ] - Análise de dados
    [ 4 ] - Antecessor & Sucessor
    [ 5 ] - Dobro, Triplo & Raíz Quadrada
    [ 6 ] - Média
    [ 7 ] - Metros para cm e mm
    [ 8 ] - Tabuada
    [ 9 ] - Calcular pintura
    [ 10] - Calcular desconto
    ''')

    opcao = input("Informe sua escolha desejada (0 para encerrar): ")

    # Encerrar aplicação.
    if opcao in '0':
        break
    # Apresentação.
    elif opcao == '1':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        nome = input("\nDigite seu nome: ")
        print("\nÉ um prazer te conhecer, {}!".format(nome))
    # Soma.
    elif opcao == '2':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        a = int(input("\nDigite um valor: "))
        b = int(input("Digite outro valor: "))
        soma = a + b
        print("\nA soma entre {} e {} é: {}.".format(a, b, soma))
    # Análise de dados.
    elif opcao == '3':
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
    elif opcao == '4':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        n = int(input("\nDigite um número: "))
        a = n - 1
        s = n + 1
        print("Analisando o valor {}, seu antecessor é {} e o sucessor é {}.".format(n, (n-1), (n+1)))
    # Dobro, Triplo & Raíz Quadrada.
    elif opcao == '5':
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
    elif opcao == '6':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        n1 = float(input("\nDigite a 1ª nota do aluno: "))
        n2 = float(input("Digite a 2ª nota do aluno:  "))
        media = (n1 + n2) / 2
        print("\nA média entre {:.1f} e {:.1f} é: {:.1f}!".format(n1, n2, media))
    # Metros para cm e mm.
    elif opcao == '7':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        medida = float(input("\nMetro(s): "))
        cm = medida * 100
        mm = medida * 1000
        print("\nA medida de {} metros corresponde a {:.0f} cm e {:.0f} mm.".format(medida, cm, mm))
    
    # Tabuada.
    elif opcao == '8':
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
    elif opcao == '9':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        largura = float(input("\nLargura da parede: "))
        altura = float(input("Altura da parede: "))
        area = largura * altura
        print("\nSua parede tem a dimensão de {} x {} e sua área é de {} m².".format(largura, altura, area))
        tinta = area / 2
        print("Para pintar essa parede você precisará de {} litros de tinta.".format(tinta))
    # Calcular desconto.
    elif opcao == '10':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        preco = float(input("\nQual é o preço do produto: R$ "))
        novo = preco - (preco * 5 / 100)
        valor_desconto = preco - novo
        print("\nO produto que custava R$ {:.2f}, na promoção com desconto de 5% vai custar R$ {:.2f}.".format(preco, novo))
        print("Você obteve um desconto de R$ {:.2f}.".format(valor_desconto))
    # Aumento de salário.
    elif opcao == '11':
        print('Disponibilizando ferramenta, por favor aguarde...')
        sleep(2)
        salario = float(input("\nQual é o valor atual do salário: R$ "))
        novo_salario = salario + (salario * 15 / 100)
        print("\nO salário atual do funcionário é R$ {:.2f}, após 15% de aumento, passará a receber R$ {:.2f}.".format(salario, novo_salario))
    
    
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

















    
    
    
    
    
    













    else:
        # Aqui vai o "Tente novamente!"
        opcao != '1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12'
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