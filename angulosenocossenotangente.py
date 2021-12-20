# import math
from math import radians, sin, cos, tan
angulo = float(input("Digite o ângulo que você deseja: "))
seno = sin(radians(angulo))
print("O ângulo de {:.0f} tem o SENO de {:.2f}.".format(angulo, seno))
cosseno = cos(radians(angulo))
print("O ângulo de {:.0f} tem o COSSENO de {:.2f}".format(angulo, cosseno))
tangente = tan(radians(angulo))
print("O ângulo de {:.0f} tem a tangente de {:.2f}.".format(angulo, tangente))