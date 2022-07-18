import platform

print(f'\nSistema Operacional: \033[0;31m{platform.system()}\033[m')
print(f'Versão: \033[0;31m{platform.release()}\033[m')
print(f'Arquitetura do Processador: \033[0;31m{platform.machine()}\033[m')
print(f'Nome do Computador: \033[0;31m{platform.node()}\033[m')
print(f'Informações da Distribuição: \033[0;31m{platform.platform()}\033[m\n')




