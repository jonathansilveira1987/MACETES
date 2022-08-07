import socket
ip_local = socket.gethostbyname(socket.gethostname())
print(f'\nIP Local: \033[0;31m{ip_local}\033[m\n')