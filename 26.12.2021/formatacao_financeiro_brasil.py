# Formatação de valores financeiros padrão Brasil.
def real(valor):
    a = "{:,.2f}".format(float(valor))
    b = a.replace(',','v')
    c = b.replace('.',',')
    return c.replace('v','.')
moeda=float(input('\nDigite o valor: '))
print(f'\nVocê digitou o valor de R$ {real(moeda)} reais.\n')
# SAÍDA DO RESULTADO:
# DIGITE O VALOR: 24568795
# VOCÊ DIGITOU O VALOR DE R$ 24.568.795,00 REAIS..