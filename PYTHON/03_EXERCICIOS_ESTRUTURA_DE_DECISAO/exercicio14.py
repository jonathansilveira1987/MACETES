# 14. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina 
# ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  # Média de Aproveitamento  Conceito
  # Entre 9.0 e 10.0            A
  # Entre 7.5 e 9.0             B
  # Entre 6.0 e 7.5             C
  # Entre 4.0 e 6.0             D
  # Entre 4.0 e zero            E
# Desenvolvido por Jonathan Silveira - Instagram: @ jonathandev01

nota1 = float(input("Digite o valor da primeira nota: "))
nota2 = float(input("Digite o valor da segunda nota: "))
media = nota1 + nota2 / 100
if media > 9.0 and media < 10.0:
    print("A - Sua média foi de: ", "%.2f" % media)
elif media > 7.5 and media < 9.0:
    print("B - Sua média foi de: ", "%.2f" % media)
elif media > 6.0 and media < 7.5:
    print("C - Sua média foi de: ", "%.2f" % media)
elif media > 4.0 and media < 6.0:
    print("D - Sua média foi de: ", "%.2f" % media)
elif media < 4.0:
    print("E - Sua média foi de: ", "%.2f" % media)