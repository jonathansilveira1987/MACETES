# 5. Altere o programa anterior permitindo ao usuário informar as populações e as taxas de 
# crescimento iniciais. Valide a entrada e permita repetir a operação.
# Desenvolvido por Jonathan Silveira - Instagram: @jonathandev01

print("\nSolução desenvolvida por Jonathan Silveira\n")
popA = float(input("Digite atual população da cidade A: "))
popB = float(input("Digite atual população da cidade B: "))
ano = 0
taxa_crescA = float(input("Digite a taxa de crescimento anual da população da cidade A: "))
taxa_crescB = float(input("Digite a taxa de crescimento anual da população da cidade B: "))
while popA < popB:
    popA += round((popA * taxa_crescA) / 100)
while popA > popB:
    popB += round((popB * taxa_crescB) / 100)
    ano = ano + 1

print("Em",ano,"ano(s) a população da cidade A será maior que a população da cidade B")
print("População cidade B -> ",popB,"habitantes")
print("População cidade A -> ",popA,"habitantes")