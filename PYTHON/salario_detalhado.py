# Salário.
valor = float(input('\nInforme um valor: '))
dias_trabalhados = int(input('Dias trabalhados: '))
carga_horaria = int(input('Horas trabalhadas ao dia: '))
valor_real = "\033[0;32mR$ {:,.2f}\033[m".format(valor).replace(",", "X").replace(".", ",").replace("X", ".")
print(f'\nSalário: {valor_real}')

# Valor por dia.
valor_diario = valor / dias_trabalhados
valor_real = "\033[0;33mR$ {:,.2f}\033[m".format(valor_diario).replace(",", "X").replace(".", ",").replace("X", ".")
print(f'\nValor Diário: {valor_real}')

# Valor por hora.
valor_hora = valor_diario / carga_horaria
valor_real = "\033[0;34mR$ {:,.2f}\033[m".format(valor_hora).replace(",", "X").replace(".", ",").replace("X", ".")
print(f'\nValor Hora: {valor_real}\n')