real = float(input("\nQuanto dinheiro você tem na carteira? R$ "))

# Atenção, é necessário alterar a cotação de moeda antes de executar o programa.
dolar = real / 5.25     # Moeda Americana
euro = real / 6.19      # Moeda Européia
renminbi = real / 0.81  # Moeda chinesa

print("Na cotação de hoje com R$ {:.2f} reais você pode comprar: \n".format(real))
print("-> U$$ {:.2f} Dólares".format(dolar))
print("-> € {:.2f} Euros".format(euro))
print("-> ¥ {:.2f} Renminbi Chineses.\n".format(renminbi))