# Validação de Dados.

sexo = str(input("\nInforme seu sexo [M/F]: ")).strip().upper()[0]
while sexo not in "MmFf":
    print("\n\033[0;31mERRO! Dados inválidos, tente novamente!\033[m")
    sexo = str(input("Informe seu sexo [M/F]: ")).strip().upper()[0]
print("\n\033[0;32mSexo {} registrado com sucesso!\033[m\n".format(sexo))