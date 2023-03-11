# 19. Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
# Desenvolvido por Jonathan Silveira - Instagram: @jonathandev01

l = []
c = 0
f = 1

q = int(input("Digite a quantidade de números desejada: "))
while q != c:
    n = float(input(f"Digite o {f}º número: "))
    while n > 1000 or n < 0:
        n = float(input("Favor digitar um número entre 0 e 1000: "))

    l.append(n)
    c += 1
    s = sum(l)

print('O menor valor é: ', min(l))
print('O maior valor é: ', max(l))
print('A soma dos valores é: ', s)