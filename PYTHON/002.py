# Validação de dados

nome = input("Digite o seu nome: ")
if nome.isalpha():
    print(nome)
else:
    print("É permitofo apenas digitação de letras")


while True:
    nome = input("Digite o seu nome: ")
    if nome.isalpha():
        print(nome)
        break
    else:
        print("É permitido apenas digitação de letras")
    

while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        print('O número digitado foi: ', numero)
        break
    except ValueError:
        print("Por favor, digite um número inteiro válido.")