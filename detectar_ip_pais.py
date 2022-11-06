# Descobrir o pais de origem de um endereço IP.
# Capturando o IP Público.
import requests
ip_publico = requests.get('https://api.ipify.org/').text
print(f'\nIP Público: \033[0;31m{ip_publico}\033[m')
# Solução 1.
request = requests.get(f'https://ip2c.org/?ip={ip_publico}')
country = request.text.split(';')[-1]
print(f'\nPaís de origem do IP = \033[0;32m{country}\033[m')
# Solução 2.
y = 'https://ip2c.org/?ip=' + (ip_publico)
# print(y)
request = requests.get(y)
request.text
country = request.text.split(';')[-1]
print(f'\nPaís de origem do IP = \033[0;33m{country}\033[m\n')