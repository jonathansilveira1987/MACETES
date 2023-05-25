# 15. Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar 
# se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se 
# o mesmo é: equilátero, isósceles ou escaleno.
# Desenvolvido por Jonathan Silveira - Instagram: @ jonathandev01

lado1 = int(input("Digite o valor do lado 1: "))
lado2 = int(input("Digite o valor do lado 2: "))
lado3 = int(input("Digite o valor do lado 3: "))

# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
if lado1 > lado3 and lado2 > lado3:
    print("De acordo com as informações fornecidas temos um Triângulo")
# Triângulo Equilátero: três lados iguais;
elif lado1 == lado2 == lado3:
    print("De acordo com as informações fornecidas temos um Equilátero")
# Triângulo Isósceles: quaisquer dois lados iguais;
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print("De acordo com as informações fornecidas temos um Isóceles")
# Triângulo Escaleno: três lados diferentes;
elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
    print("De acordo com as informações fornecidas temos um Escaleno")

max_size = 10
spacing = 3

for i in range(1, max_size + 1):

    # Primeiro triângulo
    print("*" * i, end = " " * (max_size - i + spacing))

    # Segundo triângulo
    print("*" * (max_size - i + 1), end = " " * (i - 1 + spacing))

    # Terceiro triângulo
    print(" " * (i - 1) + "*" * (max_size - i + 1), end = " " * spacing)

    # Quarto triângulo
    print(" " * (max_size - i) + "*" * i)