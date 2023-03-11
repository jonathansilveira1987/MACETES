# 10. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou 
# V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou 
# "Valor Inválido!", conforme o caso.
# Desenvolvido por Jonathan Silveira - Instagram: @ jonathandev01

turno = input("Digite M para Matutino ou V para Vespertino ou N para Noturno: ")

if turno == "M":
    print("Bom Dia")
elif turno == "V":
    print("Boa Tarde")
elif turno == "N":
    print("Boa Noite")
else:
    print("Valor Inválido")