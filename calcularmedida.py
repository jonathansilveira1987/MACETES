# Calcular medida.

medida = float(input("\nDigite uma distância em metros: "))
cm = medida * 100
mm = medida * 1000
print("\nA medida de {} metros corresponde a...".format(medida))
print("\n{:.0f} cm.".format(cm))
print("{:.0f} mm.\n".format(mm))