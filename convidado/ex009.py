# Modo Manual
num = int(input("\nDigite um número para visualizar sua tabuada: "))
print("-" * 15, "|")
print("{} x {:2} = {}".format(num, 1, num*1))
print("{} x {:2} = {}".format(num, 2, num*2))
print("{} x {:2} = {}".format(num, 3, num*3))
print("{} x {:2} = {}".format(num, 4, num*4))
print("{} x {:2} = {}".format(num, 5, num*5))
print("{} x {:2} = {}".format(num, 6, num*6))
print("{} x {:2} = {}".format(num, 7, num*7))
print("{} x {:2} = {}".format(num, 8, num*8))
print("{} x {:2} = {}".format(num, 9, num*9))
print("{} x {:2} = {}".format(num, 10, num*10))
print("-" * 15, "|")




# Modo automático
j = int(input("Digite o número o qual deseja obter a tabuada correspondente: "))
x = 0

print("-" * 15)  
print("Tabuada de {}".format(j))  
print("-" * 15)  

while (x <= 10):
    print("{1} X {0:2} = {2}".format(x, j, (x * j)))
    x = x + 1