# Primeiro Nome e Último Sobrenome.

n = str(input("\nDigite seu nome completo: \033[0;34m")).strip()
n = n.split()
print("\033[m\nPrazer em te conhecer {}!".format(n[0]))
print("Seu primeiro nome é {}.".format(n[0]))
print("Seu último nome é: {}.\n".format(n[len(n)-1]))