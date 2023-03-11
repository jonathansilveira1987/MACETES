#  Índice de Massa Corporal.

peso = float(input("Informe seu peso: (kg) "))
altura = float(input("Informe sua aultura: (m) "))
imc = peso / (altura ** 2) # altura ao quadrado.
print("O IMC dessa pessoa é de {:.1f}.".format(imc))
if imc < 18.5:
    print("Você está ABAIXO do peso normal.")
elif 18.5 <= imc < 25:
    print("Parabéns! Você está na faixa de peso NORMAL.")
elif 25 <= imc < 30:
    print("Você está com SOBREPESO.")
elif 30 <= imc < 40:
    print("Você está em OBESIDADE.")
elif imc >= 40:
    print("Você está em OBESIDADE MÓRBIDA, CUIDADO!")