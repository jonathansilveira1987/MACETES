from time import sleep

print('\nDisponibilizando ferramenta, por favor aguarde...')
sleep(2)
# Criar arquivo TXT.
arquivo = open('bancodedados.txt', 'a')
file = input('\nDigite algo: ')
arquivo.write(file)
# Lendo o arquivo criado:
arquivo = open('bancodedados.txt','r')
for linha in arquivo:
    linha = linha.rstrip()
    print (linha)
arquivo.close()
# Acrescentando texto ao arquivo criado, usando o modo de acesso 'a'
print("\n")
texto = input("Digite uma frase para acrescentar ao arquivo:\n")
arquivo = open('arq01.txt','a')
arquivo.write(texto + "\n")
print("Operaçãoo concluída no arquivo " + arquivo.name + " usando o modo de acesso " + arquivo.mode)
arquivo.close()
print("\nTexto alterado:")
arquivo = open('arq01.txt','r')
for linha in arquivo:
    linha = linha.rstrip()
    print (linha)
arquivo.close()
# Acrescentando texto ao início do arquivo, usando o modo 'r+'
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