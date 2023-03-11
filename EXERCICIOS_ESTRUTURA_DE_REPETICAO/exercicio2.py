# 2. Faça um programa que leia um nome de usuário e a sua senha 
# e não aceite a senha igual ao nome do usuário, mostrando uma mensagem 
# de erro e voltando a pedir as informações.
# Desenvolvido por Jonathan Silveira - Instagram: @jonathandev01

nome = input("Digite um nome de usuário: ")
senha = input("Digite uma senha: ")
while (nome == senha):
    print("\nO nome de usuário e a senha não podem ser iguais\n")
    nome = input("Digite um nome de usuário: ")
    senha = input("Digite uma senha: ")
print("O nome de usuário escolhido é: ",nome)
print("A senha escolhida é: ",senha)