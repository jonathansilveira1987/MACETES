# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene numa lista a média
# de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

listaNotas = []
notasAluno = []
print ('\nNOTAS DOS ALUNOS!')
for i in range(3):
    media = 0
    notasAluno = []
    print ('\n\033[0;31mAluno: ' + str(i + 1))
    for j in range(4):
        notasAluno.append(float(input('\033[mNota ' + str(j+1) + ': ')))
        media += notasAluno[j]
        print(f'\033[m\033[0;32m{media:.2f}\033[m')
        media = media / 4
        listaNotas.append(media)
print(f'\nMédia Final = \033[0;33m{listaNotas}\033[m')