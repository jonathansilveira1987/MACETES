# Detector de Palíndromo.

frase = str(input("Digite uma frase: ")).strip().upper() # Espaços eliminados antes e depois / Letras todas em Maiúsculas.
palavras = frase.split() # Frase separada em um vetor, em uma lista.
junto = "".join(palavras) # Juntei a lista em uma string só para eliminar os espaços.
print("Você digitou a frase {}.".format(junto))
inverso = ""
for letra in range(len(junto) - 1, -1, -1,):
    inverso += junto[letra] # Realizei o inverso da lista.
print("O inverso de {} é {}.".format(junto, inverso))
if inverso == junto:
    print("Temos um PALÍNDROMO!")
else:
    print("A frase digitada NÃO É UM PALÍNDROMO!")