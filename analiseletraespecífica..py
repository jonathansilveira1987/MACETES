# Análise de Letra Específica.

frase = str(input("\nDigite uma frase: ")).upper().strip()
print("\nA letra A aparece {} vezes na frase.".format(frase.count("A")))
print("A primeira letra A apareceu na posição {}".format(frase.find("A")+1))
print("A útima letra A apareceu na posição {}\n".format(frase.rfind("A")+1))