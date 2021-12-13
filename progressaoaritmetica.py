# Progressão Aritmética.

primeiro = int(input("\nPrimeiro termo: "))
razao = int(input("\nRazão: "))
decimo = primeiro + (10 - 1) * razao # Fórmula de N-ésimo (ou enésimo) termo de uma PA.
for c in range(primeiro, decimo + razao, razao):
    print("{}".format(c), end=" -> ")
print("ACABOU!\n")