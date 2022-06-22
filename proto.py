

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