# Faça um programa para a leitura de duas notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.
# Desenvolvido por Jonathan Silveira - Instagram: @ jonathandev01

n1 = input("Digite sua 1ª nota: ")
n2 = input("Digite sua 2ª nota: ")

nota = (n1 + n2) / 2

if nota >= 7 and nota < 10:    
    print ("Você foi Aprovado!!") 
elif nota >= 10:
    print ("Você foi Aprovado com Distinção!!")
else:
    print ("Infelizmente você foi reprovado")