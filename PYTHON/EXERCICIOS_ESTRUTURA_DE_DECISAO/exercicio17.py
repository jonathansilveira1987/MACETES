# 17. Faça um Programa que peça um número correspondente a um determinado ano e em 
# seguida informe se este ano é ou não bissexto.
# Desenvolvido por https://www.pythonprogressivo.net/2018/02/Descobrir-Ano-Bissexto.html

ano = int(input("Digite o ano desejado: "))
if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print("Bissexto")
else:
    print("Não é bissexto")