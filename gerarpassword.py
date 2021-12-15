import getpass

username = input('Usuário: ')
password = getpass.getpass('Senha: ')

print(username)
print(password.lenght)

























'''


import getpass

username = input('Usuário: ')
password = getpass.getpass('Senha: ')

print(username)
print(password)




import getpass
username = getpass.getuser()
password = getpass.getpass('Digite sua senha: ')





import getpass
senha = getpass.getpass("Digite sua senha: ")
print(getpass.getpass(senha))




from getpass import getpass
username = input('Usuário: ')
password = getpass.getpass('Senha: ')
print(username)
print(password)






import getpass
print('Agora vamos acessar sua conta')
inputcartao = input('Digite o número do seu cartão: ')
inputuser = input('Digite seu Login: ')
inputpass = getpass.getpass(prompt='Digite sua Senha: ', stream=None)
print(inputcartao)
print(inputuser)
print(inputpass)









import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*;/,_-"
all = lower + upper + numbers + symbols
lenght = 8
password = "".join(random.sample(all, lenght))
print(password)













import getpass

print('=' * 25)
print('Caixa eletrônico')
print('=' * 25)

account_typed = input('Digite sua conta: ')
password_typed = getpass.getpass('Digite sua senha: ')

account_list = {
    '001': {
        'password': 123,
        'name': 'User1',
    },
    '002': {
        'password': 123,
        'name': 'User2',
    }
}

if account_typed in account_list and password_typed == account_list[account_typed]['password']:
    print('A conta {} é valida'.format(account_typed))
else:
    print('A conta {} não existe ou dados inválidos'.format(account_typed))









'''