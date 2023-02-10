# pip install psutil
import psutil
# Captura o sensor da bateria
battery = psutil.sensors_battery()
# Captura o percentual da bateria
percent = str(battery.percent)
# Mostra o resultado
print(f'\nNo momento você tem {percent}% de bateria.\n')