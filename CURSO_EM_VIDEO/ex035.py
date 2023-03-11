# Analisando Triângulo v1.0.

print("-=" * 20)
print("Analisador de Triângulos\n")
r1 = float(input("Digite o primeiro segmento: "))
r2 = float(input("Digite a segundo segmento: "))
r3 = float(input("Digite o terceiro segmento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima PODEM FORMAR um triângulo!")
else:
    print("Os segmentos NÃO PODEM FORMAR triângulo!")