# Fórmula matemática.
co = float(input("Informe o comprimento do Cateto Oposto: "))
ca = float(input("Informe o comprimento do Cateto Adjacente: "))
hi = (co ** 2 + ca ** 2) ** (1/2)
print("A hipotenusa vai medir -> {:.2f}.".format(hi))




# Fórmula com módulo.
import math
co = float(input("Informe o comprimento do Cateto Oposto: "))
ca = float(input("Informe o comprimento do Cateto Adjacente: "))
hi = math.hypot(co, ca)
print("A hipotenusa vai medir -> {:.2f}.".format(hi))