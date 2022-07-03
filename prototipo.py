
















print('''


escala	escala		notação	prefixo	símbolo
curta	longa		científica	SI*	SI*
um	um	1	100		
mil	mil	1000	103	quilo	k
milhão	milhão	1 000 000	106	mega	M
bilhão	mil milhões	1 000 000 000	109	giga	G
trilião	bilião	1 000 000 000 000	1012	tera	T
quatrilhão	mil biliões	1 000 000 000 000 000	1015	peta	p
quintilhão	trilião	1 000 000 000 000 000 000	1018	exa	E
sextilhão	mil triliões	1 000 000 000 000 000 000 000	1021	zetta	Z
setilhão	quatrilião	1 000 000 000 000 000 000 000 000	1024	yota	Y
octilhão	mil quatriliões	1 000 000 000 000 000 000 000 000 000	1027		
nonilhão	quintilião	1 000 000 000 000 000 000 000 000 000 000	1030		
decilhão	mil quintiliões	1 000 000 000 000 000 000 000 000 000 000 000	1033		
undecilhão	sextilião	1 000 000 000 000 000 000 000 000 000 000 000 000	1036		
dodecilhão	mil sextiliões	1 000 000 000 000 000 000 000 000 000 000 000 000 000	1039		
tredecilhão	septilião	1 000 000 000 000 000 000 000 000 000 000 000 000 000 000	1042		
''')




# Calcular Potenciação.
while True:
    # Programa principal.
    n = int(input('\nNúmero/Base: '))
    p = int(input('Potência/Expoente: '))
    resultado = n ** p
    result = resultado = '\n\033[0;31m{0:,}\033[m\n'.format(resultado).replace(',','.') #Aqui coloca os pontos
    print(result)
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
            resp = str(input("\033[0;33mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")


# Conversor de Bases Numéricas.
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


# Calcular Percentual
a = float(input('\nVetor A: '))
b = float(input('Vetor B: '))
c = b * 100
result = c / a
print(f'\nO percentual de \033[0;32m{a}\033[m - \033[0;32m{b}\033[m é \033[0;33m{result:.2f}%\033[m')
print(f'\nO percentual obtido é de \033[0;33m{result:.2f}%\033[m')

# Calcular Percentual Dinheiro.
valor = float(input('\nValor R$ '))
percentual = float(input('Percentual desejado % '))
resultado = valor * percentual / 100
print(f'\n\033[0;31m{percentual}%\033[m de \033[0;32m{valor:.2f}\033[m é \033[0;33m{resultado:.2f}\033[m')

valor_real = "\033[0;31m{}%\033[m de \033[0;32mR$ {:,.2f}\033[m é \033[0;33mR$ {:,.2f}\033[m".format(percentual, valor, resultado).replace(",", "X").replace(".", ",").replace("X", ".")
print()
print(valor_real)
print()

# Faça um Programa que leia uma lista de 5 números inteiros e mostre-os.
print()
vetorList = [1, 4, 9, 22, 18]
i = 0
while i < len(vetorList):
    print(vetorList[i])
    i = i + 1

# Faça um Programa que leia uma lista de 5 números inteiros e mostre-os.
listaNumeros = []
print ('\nINFORME 5 NÚMEROS!')
for i in range(5):
    listaNumeros.append(input('Número '+ str(i+1) + ': '))
print('\033[0;31m')
print(listaNumeros, '\033[0m')

# Faça um Programa que leia uma lista de 10 números reais e mostre-os na ordem inversa.
listaNumerosReais = []
print ('\nINFORME 10 NÚMEROS REAIS!')
for i in range(10):
	listaNumerosReais.append(float(input('Número '+ str(i+1) + ': ')))
listaNumerosReais.reverse()
print('\033[0;31m')
print(listaNumerosReais, '\033[0m')

# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
listaNotas = []
media = 0
print ('\nINFORME 4 NOTAS!')
for i in range(4):
	listaNotas.append(float(input('Nota '+ str(i+1) + ': ')))
	media += listaNotas[i]
media = media / 4
print()
print(f'Segue lista de notas = \033[0;32m{listaNotas}\033[m') 
print(f'Segue média entre as notas = \033[0;32m{media}\033[m')

# Faça um Programa que leia uma lista de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
listaChar = []
consoantes = 0
print ('\nINFORME 10 CARACTERES!')
for i in range(10):
	listaChar.append((input('Caracter  '+ str(i+1) + ': ')))
	char = listaChar[i]
	if(char not in ('a','e','i','o','u')):
		consoantes += 1
print(f'Foram informadas {consoantes} consoantes!')

# Faça um Programa que leia 20 números inteiros e armazene-os numa lista. Armazene os números
# pares na listar PAR e os números IMPARES na lista impar. Imprima os três vetores.
listaPar = []
listaImpar = []
listaNumeros = []
numero = 0
print('\nINFORME 10 NÚMEROS!')
for i in range(10):
	listaNumeros.append((int(input('Número '+ str(i+1) + ': '))))
	numero = listaNumeros[i]
	# print (numero)
	if(numero % 2 == 0):
		listaPar.append(numero)
	else:
		listaImpar.append(numero)
print(f'''
Segue lista completa de números \033[0;31m{listaNumeros}\033[m
Segue lista de números pares 	\033[0;32m{listaPar}\033[m
Segue lista de números ímpares 	\033[0;33m{listaImpar}\033[m
''')

# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene numa lista a média
# de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
listaNotas = []
notasAluno = []
print ('\nNOTAS DOS ALUNOS!')
for i in range(3):
    media = 0
    notasAluno = []
    print ('\n\033[0;31mAluno: ' + str(i + 1))
    for j in range(4):
        notasAluno.append(float(input('\033[mNota ' + str(j+1) + ': ')))
        media += notasAluno[j]
        print(f'\033[m\033[0;32m{media:.2f}\033[m')
        media = media / 4
        listaNotas.append(media)
print(f'\nMédia Final = \033[0;33m{listaNotas}\033[m')

