# 16. Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
# O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas 
# seguintes situações:
# 1. Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não 
# deve fazer pedir os demais valores, sendo encerrado;
# 2. Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre 
# o programa;
# 3. Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# 4. Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
# Desenvolvido por Siegrfried
# https://gist.github.com/Siegrfried/6f7459b909735738f940be9673ca099a

a = float(input("\nDigite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

delta = 0
raiz1 = 0
raiz2 = 0

if a == 0:
	print("\nA equação apresentada não é do segundo grau. O programa será encerrado!")

else:
	print("\nCalculando delta...")
	delta = (((b**2) - (4*a*c)))
	
	if delta == 0:
		print("\nA equação possui apenas uma raiz que é: ")
		raiz1 = ((-b)+(delta**(1/2))/(2*a))
		print(raiz1)
	else:
		raiz1 = ((-b)+(delta**(1/2))/(2*a))
		raiz2 = ((-b)-(delta**(1/2))/(2*a))
		print("\nA equação possui duas raizes que são:", raiz1, "e", raiz2)
print()