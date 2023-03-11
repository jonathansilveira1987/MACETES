# 3. Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
# Desenvolvido por Jonathan Silveira - Instagram: @ jonathandev01

r = input("M ou F: ")
if r == "M":
    print("Masculina")
else:
    if r == "F":
          print("Feminina")
    else:
        print("Você não digitou M ou F")