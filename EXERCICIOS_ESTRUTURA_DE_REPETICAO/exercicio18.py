# 18. Faça um programa que, dado um conjunto de N números, determine 
# o menor valor, o maior valor e a soma dos valores.
# Desenvolvido por Jonathan Silveira - Instagram: @jonathandev01

condition = True
num = []
soma = 0

while condition:
    print("Pressione 0 a qualquer momento para finalizar a operação.")
    numero = int(input("Digite o numero: "))    
    if numero != 0:
        soma = soma + numero
        num.append(numero)
    else:
        break

print('O menor valor é: ', min(num))
print('O maior valor é: ', max(num))
print('A soma dos valores é: ', soma)