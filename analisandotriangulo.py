# Analisando Triângulo v1.0.

print("\nAnalisador de Triângulos")
r1 = float(input("\nDigite o primeiro segmento: "))
r2 = float(input("Digite a segundo segmento: "))
r3 = float(input("Digite o terceiro segmento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("\nOs segmentos acima \033[0;32mPODEM FORMAR\033[m um triângulo!\n")
else:
    print("\nOs segmentos \033[0;31mNÃO PODEM FORMAR\033[m triângulo!\n")




# Analisando Triângulos v2.0.

print("-=" * 20)
print("Analisador de Triângulos\n")
r1 = float(input("Digite o primeiro segmento: "))
r2 = float(input("Digite a segundo segmento: "))
r3 = float(input("Digite o terceiro segmento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima PODEM FORMAR um triângulo. ", end="")
    if r1 == r2 == r3:
        print("EQUILÁTERO!")
    elif r1 != r2 != r3 != r1:
        print("ESCALENO!")
    else:
        print("ISÓSCELES!")
else:
    print("Os segmentos NÃO PODEM FORMAR triângulo!")