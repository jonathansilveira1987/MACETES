# 4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
# Desenvolvido por Jonathan Silveira - Instagram: @ jonathandev01

letra = (input("Digite a letra que deseja descobrir : "))
if letra in "a,e,i,o,u,A,E,I,O,U":
    print("É vogal")
else:
    print("É consoante")