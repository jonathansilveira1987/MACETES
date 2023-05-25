# Custo da Viagem

# Utilizando "ESCREVA".
distancia = float(input("Digite a distânica da sua viagem: "))
print("Você está prestes a começar uma viagem de {}km.".format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print("O preço de sua passagem será de R$ {:.2f}".format(preco))


# Utilizando "SE" simplificado / hífen line / operador ternário.
distancia = float(input("Digite a distânica da sua viagem: "))
print("Você está prestes a começar uma viagem de {}km.".format(distancia))
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print("O preço de sua passagem será de R$ {:.2f}".format(preco))