# 20. Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular 
# a média alcançada por aluno e apresentar:
# 1. A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
# 2. A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
# 3. A mensagem "Aprovado com Distinção", se a média for igual a 10.
# Autor desconhecido
# Fonte: http://python-iniciantes.blogspot.com/2012/08/exercicios-36-estrutura-de-decisao.html

def entraNota(quantidade_nota):
    notas = []
    int = 1
    print()
    for num in range(quantidade_nota):
        nota = (float(input("Digite a {0}ª nota: ".format(int))))
        if nota < 0 or nota > 10:
            raise ValueError('Erro na {0}ª nota. Digite uma nota entre 0 e 10.'.format(int))
        notas.append(nota)
        int += 1
    print()
    return notas

def mediaAluno(notas):
    soma = sum(notas)
    print(soma)
    media = soma/len(notas)
    
    if media > 7.0 and media < 10:
        print('\nAprovado com média: {0:.1f}\n'.format(media))
    
    elif media < 7.0:
        print('\nReprovado com média: {0:.1f}\n'.format(media))
    
    else:
        print('\nAprovado com distinção: 10!\n')

notas = entraNota(3)
mediaAluno(notas)