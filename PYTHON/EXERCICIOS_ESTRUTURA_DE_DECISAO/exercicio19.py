# 19. Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade 
# de centenas, dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades 
# Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
# Desenvolvido por Marco A. Portela
# Fonte: https://github.com/marcoportela/python/blob/master/exercicio2_21.py

lista = [326, 300, 100, 320, 310, 305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 ,16]
#numero =raw_input("Digite um número menor que 1000: ")
#print("Centena = %d" %numero/100)
for numero in lista:
    #print (numero)
    strNumer = str(numero)
    tamNumer = len(strNumer)
    #Tratamento das centenas    
    if tamNumer == 3:
        unidade = strNumer[2]
        dezena =  strNumer[1]
        centena = strNumer[0]
        #Verificar singular ou plural 
        if unidade == "1" or unidade == "0":
            flexaoUnid = "unidade"
        else:
            flexaoUnid = "unidades"
        if dezena == "1" or dezena == "0":
            flexaoDezen = "dezena"
        else:
            flexaoDezen = "dezenas"
        if centena == "1" or centena == "0":
            flexaoCent = "centena"
        else:
            flexaoCent = "centenas"
        #imprimi mensagem
        print("%s = %s %s %s %s e %s %s" %(numero, centena, flexaoCent, dezena, flexaoDezen, unidade, flexaoUnid))
    #Tratamento das dezenas
    elif tamNumer == 2:
        unidade = strNumer[1]
        dezena = strNumer[0]
        #Verificar singular ou plural 
        if unidade == "1" or unidade == "0":
            flexaoUnid = "unidade"
        else:
            flexaoUnid = "unidades"
        if dezena == "1" or dezena == "0":
            flexaoDezen = "dezena"
        else:
            flexaoDezen = "dezenas"
        #imprimi mensagem
        print("%s = %s %s e %s %s" %(numero, dezena, flexaoDezen, unidade, flexaoUnid))
    #Tratamento de unidades    
    elif tamNumer == 1:
        unidade = strNumer[0]
        if centena == "1" or centena == "0":
            flexaoCent = "centena"
        else:
            flexaoCent = "centenas"
        #Verificar singular ou plural 
        if unidade == "1" or unidade == "0":
            flexaoUnid = "unidade"
        else:
            flexaoUnid = "unidades"
        #imprimi mensagem
        print("%s = %s %s" %(numero, unidade, flexaoUnid))