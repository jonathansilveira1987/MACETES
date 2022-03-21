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

