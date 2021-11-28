# Tamanho do texto.

texto = str(input('\nDigite seu texto: '))
# "Aprendendo Python na disciplina de linguagem de programação."

print(f"\nTamanho do texto = {len(texto)}")
print(f"\nPython in texto = {'Python' in texto}")
print(f"\nQuantidade de y no texto = {texto.count('y')}")
print(f"\nAs 3 primeiras letras são: {texto[0:3]}\n")