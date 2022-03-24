









































































'''

nome = str(input('\nNome: '))
while (len(nome) <= 3):
    print('\n\033[0;31mO nome digitado deve conter mais de 3 caracteres!\033[m')
    nome = str(input('Nome: '))
idade = int(input('\nIdade: '))
while ((idade < 0) or (idade > 150)):
    print('\n\033[0;31mA idade informada deve ser entre 0 e 150 anos!\033[m')
    idade = int(input('Idade: '))
salario = float(input('\nSalário: '))
while (salario <= 0):
    print('\n\033[0;31mO salário deve ser superior a 0!\033[m')
    salario = float(input('Salário: '))
sexo = input('\nSexo [M - Masculino / F - Feminino]: ')
while (sexo != 'M') and (sexo != 'F'):
    print('\n\033[0;31mInformação inválida, tente novamente!\033[m')
    sexo = str(input('Sexo [M - Masculino / F - Feminino]: '))
ecivil = input('\nEstado Civil (S, C, V, D): ')
while (ecivil != 'S') and (ecivil != 'C') and (ecivil != 'V') and (ecivil != 'D'):
    print('\n\033[0;31mInformação inválida, tente novamente!\033[m')
    ecivil = str(input('\nEstado Civil (S, C, V, D): '))
print(f'\nO nome informado foi \033[0;32m{nome}\033[m.')
print(f'A idade informada foi \033[0;32m{idade}\033[m.')
print(f'O salário informado foi R$ \033[0;32m{salario:.2f}\033[m.')
print(f'O sexo informado foi \033[0;32m{sexo}\033[m.')
print(f'O estado civil informado foi \033[0;32m{ecivil}\033[m.')


nome = input("Qual seu nome [mínimo 4 caracteres]: ")
idade = int(input("Sua idade: "))
salario = float(input("Salário: "))
sexo = input("Sexo ('f' para feminino ou 'm' para masculino): ")
civil = input("Estado civil (s, c, v ou d): ")
while len(nome) <= 3:
    nome = input("Seu nome deve ter mais que 3 caracteres: ")
while (idade < 0) or (idade > 150):
    idade = int(input("Voce deve ter entre 0 e 150 anos: "))
while (salario < 0):
    salario = float(input("A coisa ta difícil, mas não tem salário negativo: "))
while (sexo!= 'f') and (sexo!='m'):
    sexo = input("Biologicamente, você deve ser 'f' ou 'm': ")
while (civil != 's') and (civil != 'c') and (civil != 'v') and (civil != 'd'):
    print("Nao tem estado civil 'confuso'")
    civil = input("Deve ser s, c, v ou d: ")


while True:
    usuario = input('\nUsuário: ')
    senha = input('Senha: ')
    if usuario == senha:
        print("\n\033[0;31mO usuário e a senha não podem ser iguais, tente novamente!\033[m")
    else:
        print(f'\nO usuário informado foi {usuario}.')
        print(f'A senha informada foi {senha}.')
        break
while True:
    nota = int(input('\nInforme uma nota entre 0 e 10: '))
    if nota > 10:
        print(f'\n{nota} é um valor inválido, tente novamente!')
    else:
        print(f'\nVocê digitou a nota {nota}.')
        break

login = input("Login: ")
senha = input("Senha: ")
while login == senha:
    print("Sua senha deve ser diferente do login: ")
    senha = input("Senha: ")
print("Cadastro aprovado")












































num = float(input('\nNumero original: '))
if num == round(num):
    print("\nO valor informado é INTEIRO.")
else:
    print("\nO valor informado é DECIMAL.")
    print("\nArredondado pra baixo: ", round(num-0.5))
    print("Arredondado pra cima : ", round(num+0.5))










a = 100/5
b = 20//3
print(a * b)

c = 5 / 5.5
d = 5 * 5.5
print(c//d)



v = sm = nv = 0
while True:
    v = int(input("\nDigite um valor (\033[0;32m000\033[m para executar a operação): "))
    if v == 000:
        break
    sm += v
    nv += 1
print(f"\nO total de valores digitados foi de {nv}.")
print(f"A soma entre eles é {sm}.")




v = sm = nv = 0
while v != 999:
    v = int(input("\nDigite um valor (\033[0;32m000\033[m para executar a operação): "))
    if v == 000:
        break
    sm += v
    nv += 1
print(f"\nO total de valores digitados foi de {nv}.")
print(f"A soma entre eles é {sm}.")









while True:
    # Aqui vai o programa principal!
    n = int(input('\nNúmero/Base: '))
    p = int(input('Potência/Expoente: '))
    a = n ** p
    print()
    resultado = '{0:,}'.format(a).replace(',','.') #Aqui coloca os pontos
    print(f'\033[0;31m{n}\033[m elevado a \033[0;31m{p}\033[m é \033[0;31m{resultado}\033[m.')
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\n\033[0;33mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m")













'''