# Capturando o IP Local.
import socket
ip_local = socket.gethostbyname(socket.gethostname())
print(f'\nIP Local: \033[0;31m{ip_local}\033[m\n')
# Capturando o IP Público.
import requests
ip_publico = requests.get('https://api.ipify.org/').text
print(f'IP Público: \033[0;31m{ip_publico}\033[m\n')
# Salvar em um arquivo de texto:
log = 'log_ip.txt'
with open(log, 'w') as fileObj:
    fileObj.write(f'Local IP Address = {ip_local}\nPublic IP Address = {ip_publico}')
print('\033[0;34mSalvo em ' + log)
print('\033[m')