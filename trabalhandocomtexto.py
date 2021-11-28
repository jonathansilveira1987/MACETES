# Primeiro Nome e Último Sobrenome.
n = str(input("Digite seu nome completo: ")).strip()
n = n.split()
print("Prazer em te conhecer {}!".format(n[0]))
print("Seu primeiro nome é {}.".format(n[0]))
print("Seu último nome é: {}\n".format(n[len(n)-1]))


# Análise de Letra Específica.
frase = str(input("Digite uma frase: ")).upper().strip()
print("A letra A aparece {} vezes na frase.".format(frase.count("A")))
print("A primeira letra A apareceu na posição {}".format(frase.find("A")+1))
print("A útima letra A apareceu na posição {}\n".format(frase.rfind("A")+1))

arquivo = open("bancodedados.txt", "a")
file = input('Digite algo: ')
arquivo.write(file)

# Lendo o arquivo criado:
arquivo = open('arq01.txt','r')
for linha in arquivo:
    linha = linha.rstrip()
    print (linha)
arquivo.close()

# Acrescentando texto ao arquivo criado, usando o modo de acesso 'a'
print("\n")
texto = input("Digite uma frase para acrescentar ao arquivo:\n")
arquivo = open('arq01.txt','a')
arquivo.write(texto + "\n")
print("Opera��o conclu�da no arquivo " + arquivo.name + " usando o modo de acesso " + arquivo.mode)
arquivo.close()

print("\nTexto alterado:")
arquivo = open('arq01.txt','r')
for linha in arquivo:
    linha = linha.rstrip()
    print (linha)
arquivo.close()

# Acrescentando texto ao in�cio do arquivo, usando o modo 'r+'
print("\n")
texto = input("Digite um titulo para acrescentar ao arquivo:\n")
arquivo = open('arq01.txt','r+')
arquivo.seek(0)
arquivo.write(texto + '\n')
arquivo.close()

print("\nTexto alterado:")
arquivo = open('arq01.txt','r')
for linha in arquivo:
    linha = linha.rstrip()
    print (linha)
arquivo.close()

arquivo = open("bancodedados.txt", "a")
file = input('Digite algo: ')
arquivo.write(file)


# solution...?
arquivo = open("texto.txt", "a")

frases = list()
frases.append("TreinaWeb \n")
frases.append("Python \n")
frases.append("Arquivos \n")
frases.append("Django \n")

arquivo.writelines(frases)