# 4. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual 
# de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento 
# de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população 
# do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
# Desenvolvido por Jonathan Silveira - Instagram: @jonathandev01

print("\nSolução desenvolvida por Jonathan Silveira")
paisa = 80000
paisb = 200000
anos = 0

while paisa <= paisb:
    paisa += paisa * 0.03
    paisb += paisb * 0.015
    anos += 1

print("O país A vai igualar ou ultrapassar o país B em número populacional daqui a", anos, "anos")


print("\nSolução desenvolvida por Sérgio Luiz Araújo Silva")
# Desenvolvido por Sérgio Luiz Araújo Silva
# Fonte: https://gist.github.com/voyeg3r/357452
popA, popB, anos = 80000, 200000, 0
cresA, cresB = 0.03, 0.015 # Crescimentos de 3% e 1,5% ao ano
while (popA < popB):
    anos += 1
    popA = popA + (popA * cresA)
    popB = popB + (popB * cresB)
print("Após %i anos o país A ultrapassou o país B em número de habitantes." % anos)
print("País A: %.0f" % popA)
print("País B: %.0f" % popB)