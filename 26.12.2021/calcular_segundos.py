# Calcular segundos.
('''
Veja abaixo uma tabela mostrando a divisão completa de cada unidade de tempo comum em segundos:

Unidades de tempo habituais 	Segundos
1 minuto                        60 segundos
1 hora                          3600 segundos
1 dia                       	86400 segundos
1 mês                           (30.44 dias)    2.629.743 segundos
1 ano                           (365.24 dias)   31.556.926 segundos

''')
nanosegundo = 1000000000
microsegundo = 1000000
milissegundo = 1000
segundo = 9192631770
minuto = 60 # 60 segundos.
hora = minuto * 60 # 3.600
dia = hora * 24 # 86.400
mes = dia * 30.44
ano = dia * 365.24
print("\nUm minuto tem \033[0;32m{0:,}\033[m segundos.".format(minuto).replace(",", "."))
print("Uma hora tem \033[0;32m{0:,}\033[m segundos.".format(hora).replace(",", "."))
print("Um dia tem \033[0;32m{0:,}\033[m segundos.".format(dia).replace(",", "."))
print("Um mês tem aproximadamente \033[0;32m{0:,}\033[m segundos.".format(mes).replace(",", "."))
print("Um ano tem aproximadamente \033[0;32m{0:,}\033[m segundos.\n".format(ano).replace(",", "."))