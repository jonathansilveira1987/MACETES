# 6. Faça um Programa que leia três números e mostre o maior deles.
# Desenvolvido por Jonathan Silveira - Instagram: @ jonathandev01

def menu():
    num1 = int(input('\nNúmero um: '))
    num2 = int(input('\nNúmero dois: '))
    num3 = int(input('\nNúmero três: '))

    if num1 > num2 and num1 > num3:
        print('\nO número um é o maior: ', num1)
    elif num2 > num1 and num2 > num3:
        print('\nO número dois é o maior: ', num2)
    else:
        print('\nO número três é o maior: ', num3)

while True:
    menu()






'''


def maior(x,y,z):
    max = x

    if y > max:
        max = y
    if z > max:
        max = z

    return max

def menor(x,y,z):
    min = x

    if y < min:
        min = y
    if z < min:
        min = z

    return min

def menu():
    x = int(input('Primeiro numero: '))
    y = int(input('Segundo numero : '))
    z = int(input('Terceiro: numero: '))

    print("Maior: ", maior(x,y,z))
    print("Menor: ", menor(x,y,z))
    print()
    
while True:
    menu()

'''