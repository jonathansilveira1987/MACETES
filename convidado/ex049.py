# Tabuada v.2.0.

# Modo Manual
num = int(input("\nDigite um número para visualizar sua tabuada: "))
print("-" * 15, "|")

for c in range(1, 11):
    print("{} x {:2} = {}".format(num, c, num*c))

print("-" * 15, "|")