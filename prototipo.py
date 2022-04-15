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















