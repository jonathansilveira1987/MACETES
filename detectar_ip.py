import socket
ip_local = socket.gethostbyname(socket.gethostname())
print(f'\nIP Local: {ip_local}\n')