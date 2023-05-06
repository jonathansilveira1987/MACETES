# solution...?
arquivo = open("texto.txt", "a")
frases = list()
frases.append("TreinaWeb \n")
frases.append("Python \n")
frases.append("Arquivos \n")
frases.append("Django \n")
arquivo.writelines(frases)
print(frases)