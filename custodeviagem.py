# Custo da Viagem.

# Utilizando "ESCREVA".
distancia = float(input("\n\033[0;32mDigite a distância da sua viagem:\033[m "))
print("\033[0;32mVocê está prestes a começar uma viagem de {} km.\033[m".format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print("\033[0;32mO preço de sua passagem será de R$ {:.2f}\033[m\n".format(preco))

# Utilizando "SE" simplificado / hífen line / operador ternário.
distancia = float(input("\n\033[0;33mDigite a distânica da sua viagem:\033[m "))
print("\033[0;33mVocê está prestes a começar uma viagem de {} km.\033[m".format(distancia))
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print("\033[0;33mO preço de sua passagem será de R$ {:.2f}\033[m\n".format(preco))