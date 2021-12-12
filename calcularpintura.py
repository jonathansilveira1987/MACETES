largura = float(input("\nLargura da parede: "))
altura = float(input("Altura da parede: "))
area = largura * altura
print("\nSua parede tem a dimensão de {} x {} e sua área é de {} m².\n".format(largura, altura, area))
tinta = area / 2
print("Para pintar essa parede você precisará de {} litros de tinta.\n".format(tinta))