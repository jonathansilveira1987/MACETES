a = float(input('\nEntre com o valor de a: '))
b = float(input('Entre com o valor de b: '))
c = float(input('Entre com o valor de c: '))

delta = (b ** 2) - 4 * a * c

print("\n**************************\n")

if a == 0:
    print("\nO valor de a, deve ser diferente de 0\n")
elif delta < 0:
    print("Sem raízes reais\n")
else:
    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    x2 = (-b - delta ** (1 / 2)) / (2 * a)

    print("x1: {}, x2: {}\n".format(x1, x2))