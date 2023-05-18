# Faça um programa para a leitura de duas notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.
# Desenvolvido por Jonathan Silveira - Instagram: @ jonathandev01

n1 = int(input('\nDigite sua 1ª nota: '))
n2 = int(input('Digite sua 2ª nota: '))

# nota = (n1 + n2) / 2
nota = n1 + n2
media = nota / 2
print(f'\nMédia = {media}')

if media >= 7 and media < 10:    
    print ('\nVocê foi Aprovado!\n') 
elif media >= 10:
    print ('\nVocê foi Aprovado com Distinção!\n')
else:
    print ('\nInfelizmente você foi reprovado!\n')