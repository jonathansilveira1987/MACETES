#-*- coding: cp1252 -*-                     #
            # ------------------------------------------#
            # Agenda eletronica em Python.              #
            # @autor: Jhonathan Paulo Banczek           #
            # data:05/09/2010                           #
            # ------------------------------------------#

#------------------------------------------------------------------------------#


#--------------------GLOBAL--------------------#
lista = [] #define uma variavel para a lista

#le os dados do arquivo e joga pra lista

arq2 = open("agenda.csv","a+")
lista = arq2.readlines()
arq2.close()
#-----------------------------------------------#
    

#------------------------------------------------------------------------------#

#fun��o: menu, constroi o menu

def menu():
    print("\n", "=" * 50)
    print("""\nAGENDA ELETRÔNICA\n\n
                Escolha a opção: \n
                1 -  INSERIR CONTATO\n
                2 -  DELETAR\n
                3 -  MOSTRAR AGENDA\n
                4 -  FINALIZAR PROGRAMA\n""")
    
#fim da fun��o menu



#------------------------------------------------------------------------------#
    
#fun��o: lista_agenda, adiciona, remove e mostra a lista
    
def lista_agenda(nome, data, opc):

    if( opc == 1):
        contato = nome + " - " + data + "\n" #concatenao o 'nome' ';' e 'data'
        lista.append(contato)
        lista.sort() #ordena a lista por prioridade

    elif (opc == 2):
        print("=" * 30)
        if ( lista == []): #se lista for vazia
            print("Lista Vazia\n")
        else:
            lista.pop(0)#remove o elemento de maior prioridade, ou seja, indice 0 da lista
            print("Removido o elemento de maior prioridade")
        print("=" * 30)

    elif (opc == 3):
        print("=" * 30)
        if (lista == []):
            print("Lista vazia!")
        else:
            print("Nome & Data de Nascimento: \n")
            for i in lista:
                print(i)
        print("=" * 30)

    elif (opc == 4):
        arq = open("agenda.csv","w") #escreve por cima do arquivo antigo (atualiza lista)
        tam = len(lista) #recebe o tamanho da lista
        #for que insere os valores no arquivo separado por ';' sendo nome = indice par e data = impar

        for i in range(tam):
            arq.write(lista[i])

        arq.close()

#fim da fun��o lista_agenda


        
#------------------------------------------------------------------------------#
#funcao principal


opc = 0 #variavel pro menu

while (opc != 4 ):

    menu() #chama o menu

    while True:
        try:
            opc = int(input('> ')) #recebe a op��o
            break
        except:
            print("ERRO, digite só números válidos!")

    if ( opc == 1 ):
        print("\nInforme o nome do contato.")
        nome = input('> ')

        print("\ninforme a data de nascimento.")
        data = input('> ')

        lista_agenda(nome, data, 1) #chama a fun��o para inserir na lista

    elif ( opc == 2):
        lista_agenda(0,0,2) #chama a fun��o para deletar o nome na lista

    elif (opc == 3): #chama a fun��o para mostrar na tela
        print("Lista de contatos: ")
        lista_agenda(0,0,3)
                

lista_agenda(0,0,4) #grava a lista na agenda
print("\nFIM DO PROGRAMA! ")

#------------------------------------------------------------------------------#
#fim