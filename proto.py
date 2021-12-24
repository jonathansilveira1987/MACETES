import datetime as dt
from datetime import datetime

h1 = dt.datetime.now()

h2 = input('Informe a hora final do evento (Exemplo - 14:25:30): ')

s1 = h1
s2 = h2 # for example

FMT = '%H:%M:%S'
tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
print(tdelta)
















































'''


distância = float(input("\nDigite a distância em km: "))
velocidade_média = float(input("Digite a velocidade média em km/h: "))
tempo = distância / velocidade_média
tempo_s = int(tempo * 3600)  # convertemos de horas para segundos
horas = int(tempo_s / 3600)  # parte inteira
tempo_s = int(tempo_s % 3600)  # o resto
minutos = int(tempo_s / 60)
segundos = int(tempo_s % 60)
milesimosegundos = int(tempo_s % 60)
# Imprimir o tempo em horas, minutos, segundos e milésimos de segundos.
# print("\n\033[0;32mO tempo estimado de viagem é de %04d hora(s) %02d minuto(s) %02d segundo(s) & %02d milésimos de segundo(s).\033[m" % (horas, minutos, segundos, milesimosegundos))
# Imprimir o tempo em horas, minutos, segundos.
print("\n\033[0;33m%04d hora(s) %02d minuto(s) & %02d segundo(s).\033[m\n" % (horas, minutos, segundos))


hora_atual = dt.datetime.now()
hora_final = hora_atual + dt.timedelta(tempo)
hora_atual = hora_atual.strftime("%H:%M:%S")
hora_final = hora_final.strftime("%H:%M:%S")
print(f"\n\033[0;33mA hora atual é {hora_atual}.\033[m")
print(f"\033[0;32mO horário final do processo é {hora_final}.\033[m\n")



# Calcular o intervalo de tempo entre duas seqüências de tempo.
from datetime import datetime

a1 = float(input('Primeiro horário: '))
a2 = float(input('Segundo horário: '))


s1 = a1
s2 = a2 # for example
FMT = '%H:%M:%S'
tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
print(tdelta)


import datetime as dt

start="09:35:23"
end="10:23:00"
start_dt = dt.datetime.strptime(start, '%H:%M:%S')
end_dt = dt.datetime.strptime(end, '%H:%M:%S')
diff = (end_dt - start_dt) 
diff.seconds/60 

print(start_dt)
print(end_dt)















from datetime import datetime
s1 = '10:33:26'
s2 = '11:15:49' # for example
FMT = '%H:%M:%S'
tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
print(tdelta)



'''