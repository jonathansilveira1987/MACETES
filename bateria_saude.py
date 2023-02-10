# pip install psutil
import psutil
# Captura o sensor da bateria
battery = psutil.sensors_battery()
# Captura o percentual da bateria
percent = int(battery.percent)
if percent <= 20:
    # Mostra o resultado
    print(f'\n\033[0;31mAtenção! Seu computador está operando com {percent}% de bateria. Conecte o carregador!\033[m\n')
else:
    # Mostra o resultado
    print(f'\n\033[0;32mNo momento seu computador está operando com {percent}% de bateria.\033[m\n')