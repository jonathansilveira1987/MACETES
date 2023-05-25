# Extraindo dados de uma Lista.

valores = []
while True:
    valores.append(int(input("Digite um valor: ")))
    resp = str(input("Deseja continuar [S/N]? "))
    if resp in "Nn":
        break
print("-=" * 30)
print(f"Você digitou {len(valores)} elementos.")
valores.sort(reverse=True)
print(f"Os valores em ordem decrescente são: {valores}.")
if 5 in valores:
    print("O valor 5 faz parte da lista!")
else:
    print("O valor 5 não foi encontrado na lista!")





'''
n = [1, 34, 55, 4, 8]
x = n[-3 :: -1]
print(x)
'''