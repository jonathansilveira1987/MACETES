# 18. Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
# Desenvolvido por Thiago Moreira de Souza Arrais
# Fonte: https://github.com/ThiagoMSArrais/python-exercise/blob/master/Q18.py

def validarData():
    
    #obter data dd/mm/aaaa
    obterData = input("\nInforme uma data: ")

    #verificar formatação.
    if len(obterData) == 10:
        if obterData[2] == '/' and obterData[5] == '/':    
            #tratar data obtida.
            dataFatiada = obterData.split('/')
            #verificar dia.
            if int(dataFatiada[0]) <= 31 and int(dataFatiada[0]) >= 1:
                #verificar mês.
                if int(dataFatiada[1]) <= 12 and int(dataFatiada[1]) >= 1:
                    #verificar ano.
                    if len(dataFatiada[2]) == 4 and int(dataFatiada[2]) != 0000:
                        print ("\nData válida!")
                    else:
                        print ("\nFormato ano errado.")
                        validarData()
                else:
                    print ("\nFormato mês errado, tem que ser entre 1 e 12.")
                    validarData()
            else:
                print ("\nFormato dia errado, tem que ser entre 1 e 31.")
                validarData()
        else:
            print ("\nFormato errado da data, o correto seria \"dd/mm/aaaa\"")
            validarData()
    else:
        print ("\nQuantidade de caracteres errado, formato correto \"dd/mm/aaaa\".")
        validarData()

validarData()