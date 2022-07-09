texto = str(input('\nDigite seu texto: '))
# Aprendendo Python na disciplina de linguagem de programação.
print(f"\nO texto informado possui \033[0;31m{len(texto)}\033[m caracteres.")
print(f"\nPython in texto = \033[0;31m{'Python' in texto}\033[m")
print(f"\nQuantidade de y no texto = \033[0;31m{texto.count('y')}\033[m")
print(f"\nAs 3 primeiras letras são: \033[0;31m{texto[0:3]}\033[m\n")