texto = '  Juros Simples '
print(f'\n\033[0;34m{texto:.^50}\033[m') # Centralizado.
aplicacao = float(input('\nAplicação R$ '))
juros = float(input('Juro Mensal % '))
periodo = float(input('Período em Meses: '))
resultado = (((juros * aplicacao) / 100) * periodo) + aplicacao
print(f'\n{periodo:.0f} meses a {juros:.2f}% de juros ao mês somará um montande de {resultado}\n')