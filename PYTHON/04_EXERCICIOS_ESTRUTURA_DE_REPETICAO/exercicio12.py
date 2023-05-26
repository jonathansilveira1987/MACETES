# 12. Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer 
# número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja 
# ver a tabuada. A saída deve ser conforme o exemplo abaixo:
# Tabuada de 5:
# 5 X 1 = 5
# 5 X 2 = 10
# ...
# 5 X 10 = 50
# Desenvolvido por Jonathan Silveira - Instagram: @jonathandev01

j = int(input('\nDigite o número o qual deseja obter a tabuada correspondente: '))
x = 0

print('\033[34m')
print("-" * 15)  
print("Tabuada de {}".format(j))  
print("-" * 15)  

while (x <= 10):
    print("{1} X {0} = {2}".format(x, j, (x * j)))
    x = x + 1
print('\033[m')