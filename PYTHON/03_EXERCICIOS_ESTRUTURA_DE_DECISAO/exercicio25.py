# 25. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre
# 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
# Desenvolvido por Jonathan Silveira - Instagram: @ jonathandev01 com auxílio de:
# Messias Ferreira & Fernanda Campagnucci Pereira
# Fonte: https://cursos.alura.com.br/forum/topico-a-resposta-do-terminal-esta-saindo-diferente-do-debug-67135

print("Vamos a um breve interrogatório sobre um crime")
print("Digite 1 para SIM ou 2 para NÃO")

classificacao = ("Suspeita",
                "Cúmplice",
                "Assassino",
                "Inocente")

perguntas = ['Telefonou para a vítima?',
            'Esteve no local do crime?',
            'Mora perto da vítima?',
            'Devia para a vítima?',
            'Já trabalhou com a vítima?']

count = 0

respostas = False
for i in range(len(perguntas)):
    respostas = input('{}\n'.format(perguntas[i]))
    if(respostas =='1'):
        count+=1

if(count == 2):
    print(classificacao[0])
elif(count == 3 or count == 4):
    print(classificacao[1])
elif (count == 5):
    print(classificacao[2])
else:
    print(classificacao[3])