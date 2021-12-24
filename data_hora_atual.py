import datetime as dt
from datetime import datetime, time
from time import sleep

# Data atual.
print('\nSolução I.')
data_e_hora_atuais = datetime.now()
data_e_hora_em_texto = data_e_hora_atuais.strftime("%d/%m/%Y")
print('Em instantes você verá a data atual...')
sleep(2)
print(f'\033[0;33mA data atual é {data_e_hora_em_texto}.\033[m')
# Hora atual.
hora_atual = dt.datetime.now()
hora_atual = hora_atual.strftime("%H hora(s) %M minuto(s) %S segundo(s) & %M milésimo(s) de segundo(s).")
print('\nem seguida você verá a hora atual...')
sleep(2)
print(f"\033[0;32mA hora atual é {hora_atual}\033[m")


# Data e hora atual.
print('\nSolução II.')
from datetime import datetime, time
data_e_hora_atuais = datetime.now()
data_e_hora_em_texto = data_e_hora_atuais.strftime("\033[0;32mDia %d/%m/%Y - %H hora(s) %M minuto(s) %S segundo(s) & %M milésimo(s) de segundo(s).\033[m\n")
print('Agora você verá a data e hora atual juntas...')
sleep(3)
print('Segue data e hora atual = ', data_e_hora_em_texto)