# 23. Faça um Programa que peça um número e informe se o número é inteiro ou decimal. 
# Dica: utilize uma função de arredondamento.
# Desenvolvido por Jonathan Silveira - Instagram: @ jonathandev01

# Função de Arredondamento
# numero = float(input("Numero original: "))
# print("Arredondado :", round(numero))

numero = float(input("Digite um número: "))

if numero == round(numero):
    print("O número digitado é inteiro")
else:
    print("O número digitado é decimal")
    # print("Arredondado pra baixo: ", round(numero-0.5))
    # print("Arredondado pra cima : ", round(numero+0.5))