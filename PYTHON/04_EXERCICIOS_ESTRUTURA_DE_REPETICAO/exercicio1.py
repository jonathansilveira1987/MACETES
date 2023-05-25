# 1. Faça um programa que peça uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido e continue 
# pedindo até que o usuário informe um valor válido.
# Desenvolvido por Jonathan Silveira - Instagram: @jonathandev01

nota = float(input("Digite uma nota entre 0 e 10: "))

while (nota>10) or (nota<0):
    nota = float(input("O valor digitado está incorreto, digite apenas uma nota de 0 a 10, por favor, tente novamente: "))
    
print("A nota digitada é: ",round(nota))