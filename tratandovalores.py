# Tratando vários valores v1.0.

num = cont = soma = 0
num = int(input("\nDigite um número [999 para parar]: "))
while num != 999:    
    soma += num
    cont += 1
    num = int(input("\nDigite um número [999 para parar]: "))
print("\nVocê digitou {} números e a soma entre eles foi \033[0;31m{:.2f}\033[m.\n".format(cont, soma))