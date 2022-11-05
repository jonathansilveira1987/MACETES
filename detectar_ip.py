import socket
ip_local = socket.gethostbyname(socket.gethostname())
print(f'\nIP Local: \033[0;31m{ip_local}\033[m\n')

# Salvar em um arquivo de texto:
log = 'log_ip.txt'
with open(log, 'w') as fileObj:
    fileObj.write(f'IP Address = {ip_local}')
print('\033[0;34mSalvo em ' + log)
print('\033[m')