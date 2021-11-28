# Análise de dados.

from time import sleep

n = input("\n\033[0;33mDigite algo: \033[m").strip()

print("\n\033[0;36mAnalisando informações...\033[m")
sleep(3)
print(f"\nInformação digitada = \033[0;32m{n}\033[m")
print(f"\nTotal de caracteres com espaços = \033[0;32m{len(n)}\033[m")
print("\nTotal de caracteres sem espaços = \033[0;32m{}\033[m".format(len(n)-n.count(" ")))
# print("\nEspaços = \033[0;32m{}\033[m".format(len(" ")-n.count(" ")))
totpalavras = n.split()
print(f"\nTotal de palavras = \033[0;32m{len(totpalavras)}\033[m")
palavras = n.upper()
print(f"\nMaiúsculas = \033[0;32m{palavras}\033[m")
print("\nMaiúsculas: \033[0;32m{}\033[m".format(n.upper()))
print("\nMinúsculas: \033[0;32m{}\033[m".format(n.lower()))
print("\nA primeira composição tem \033[0;32m{}\033[m caractere(s)".format(n.find(" ")))
separa = n.split()
print("\nA primeira composição de caracteres é \033[0;32m{}\033[m e tem \033[0;32m{}\033[m caracteres\n".format(separa[0], len(separa[0])))