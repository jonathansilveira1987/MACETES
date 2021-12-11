# Vários números com flag.

# Primeira Solução.
soma = cont = 0
while True:
    num = int(input("Digite um valor (999 para parar a execução): "))
    if num == 999:
        break
    cont = cont + 1
    soma = soma + num
print("A soma dos {} valores foi {}!.".format(cont, soma))



# Segunda Solução.
v = sm = nv = 0
while v != 999:
    v = int(input("Digite um valor: "))
    if v != 999:
        sm += v
        nv += 1
print(f"O total de valores digitados foi de {nv}.")
print(f"E a soma entre eles deu {sm}.")