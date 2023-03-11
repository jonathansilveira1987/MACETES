# 2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
# Desenvolvido por Jonathan Silveira - Instagram: @ jonathandev01

# Simples
numero = int(input("digite um numero: "))
if numero >= 0:
  print(f"O numero {numero} é positivo".format(numero))
else:
  print(f"O numero {numero} é negativo".format(numero))


# Detalhado
num = int(input("Digite um numero: "))
if num > 0 :
    print("Positivo")
else:
    if num == 0 :
        print("Nem positivo nem negativo, é 0")
    else:
        print("Negativo")