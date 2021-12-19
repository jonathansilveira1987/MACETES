# Validação de Dados.

sexo = str(input("Informe seu sexo [M/F]: ")).strip().upper()[0]
while sexo not in "MmFf":
    sexo = str(input("\033[0;31mDados inválidos.\033[m Por favor informe seu sexo [M/F]: ")).strip().upper()[0]
print("\nSexo {} registrado com sucesso!\n".format(sexo))