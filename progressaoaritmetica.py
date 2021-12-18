# Progressão Aritmética v1.0.

primeiro = int(input("\nPrimeiro termo: "))
razao = int(input("\nRazão: "))
decimo = primeiro + (10 - 1) * razao # Fórmula de N-ésimo (ou enésimo) termo de uma PA.
for c in range(primeiro, decimo + razao, razao):
    print("{}".format(c), end=" -> ")
print("ACABOU!\n")


# Progressão Aritmética v2.0.

print("Gerador de PA")
print("-=" * 15)
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))
termo = primeiro
cont = 1
while cont<= 10:
    print("{} -> ".format(termo), end=" ")
    termo += razao
    cont += 1
print("FIM!")


# Super Progressão Aritmética v3.0.

print("Gerador de PA")
print("-=" * 15)
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont<= total:
        print("{} -> ".format(termo), end=" ")
        termo += razao
        cont += 1
    print("PAUSA")
    mais = int(input("Quantos termos você deseja mostrar a mais? "))
print("Progressão finalizada com {} termos mostrados.".format(total))