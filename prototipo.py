# Calcular Percentual.
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














































