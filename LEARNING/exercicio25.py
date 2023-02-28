from time import sleep

nome = str(input("\nDigite seu nome completo: ")).strip()
print("\nAnalisando seu nome...")
sleep(5)
print("\nSeu nome em letras maiúsculas é {}".format(nome.upper()))
print("Seu nome em letras minúsculas é {}".format(nome.lower()))
print("Seu nome tem ao todo {} letras".format(len(nome) - nome.count(" ")))
print("Seu primeiro nome tem {} letras\n".format(nome.find(" ")))