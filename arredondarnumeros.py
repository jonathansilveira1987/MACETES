m = float(input('\nInforme a medida em Metros: '))
cm = m * 100

print('\n{}'.format(round(cm, 1)))
print('{}'.format(round(cm, 2)))
print('{}'.format(round(cm, 3)))
print('{}'.format(round(cm, 4)))
print('{}\n'.format(round(cm, 5)))

print("{0:.1f}".format(round(cm)))
print("{0:.2f}".format(round(cm)))
print("{0:.3f}".format(round(cm)))
print("{0:.4f}".format(round(cm)))
print("{0:.5f}".format(round(cm)))
print("{0:.10f}".format(round(cm)))
print("{0:.20f}".format(round(cm)))
print("{0:.30f}".format(round(cm)))
print("{0:.50f}\n".format(round(cm)))

m = '{0:,}'.format(cm).replace(',','.') # Aqui coloca os pontos
print(m)