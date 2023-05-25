dias = int(input("\nQuantos dias alugado? "))
km = float(input("Quantos kilômetros rodados? "))
pago = (dias * 60) + (km * 0.15)
print("\n-> O total a pagar pelo aluguel do veículo é de R$ {:.2f}\n".format(pago))