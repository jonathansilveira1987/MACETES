# 3. Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';
# Desenvolvido por Jonathan Silveira - Instagram: @jonathandev01

# nome
nome = str(input("\nDigite o nome: "))
while (len(nome) <= 3):
    print("O nome deve ter no mínimo 3 caracteres")
    nome = str(input("Digite seu nome: "))
# idade
idade = int(input("Digite a idade: "))
while (idade == 0 or idade > 150):
    print("A idade deve ser maior que zero e menor que 150")
    idade = int(input("Digite a idade: "))
# salário
salario = float(input("Digite o valor de salário R$ "))
while (salario == 0):
    print("O valor do salário deve ser maior que 0")
    salario = float(input("Digite o valor de salário: "))
# sexo
sexo = str(input("Digite sexo: \n Masculino \n Feminino\n\n"))
while (sexo != "Masculino") and (sexo != "Feminino") and (sexo != "masculino") and (sexo != "feminino"):
    print("O sexo digitado deve ser Masculino ou Feminino")
    sexo = str(input("Digite o sexo: "))
# estado civil
estado_civil = str(input("Digite seu estado civil: \n Solteiro \n Casado \n Viúvo \n Divorciado\n\n"))
while (estado_civil != "Solteiro") and (estado_civil != "Casado") and (estado_civil != "Viúvo") and (estado_civil != "Divorciado") and (estado_civil != "solteiro") and (estado_civil != "casado") and (estado_civil != "viúvo") and (estado_civil != "divorciado"):
    print("O estado civil informado está incorreto")
    estado_civil = str(input("Digite: \n Solteiro \n Casado \n Viúvo \n Divorciado\n\n"))

print("\nSegue suas informações\n")
print("Seu nome é:", nome)
print("Sua idade é de:", idade, "anos")
print("Seu salário é de R$", salario)
print("Seu sexo é:", sexo)
print("Seu atual estado civil é:", estado_civil)
print()