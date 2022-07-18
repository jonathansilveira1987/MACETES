import platform
import psutil # pip install psutil
import wmi # Usando o módulo WMI (apenas para Windows) pode ser instalado usando o comando: pip install wmi
c = wmi.WMI()    
my_system = c.Win32_ComputerSystem()[0]

print(f'\nNome do Computador: \033[0;31m{platform.node()}\033[m')
print(f'Sistema Operacional: \033[0;31m{platform.system()}\033[m')
print(f'Lançamento: \033[0;31m{platform.release()}\033[m')
print(f'Versão: \033[0;31m{platform.version()}\033[m')
print(f'Informações da Distribuição: \033[0;31m{platform.platform()}\033[m')
print(f"Tipo de Sistema: \033[0;31m{my_system.SystemType}\033[m")
print(f'Arquitetura do Processador: \033[0;31m{platform.machine()}\033[m')
print(f'Processador: \033[0;31m{platform.processor()}\033[m')
print(f"Quantidade de Núcleos do Processador: \033[0;31m{psutil.cpu_count()}\033[m")
print(f"Número de Processadores: \033[0;31m{my_system.NumberOfProcessors}\033[m")
print(f"Memória: \033[0;31m{psutil.virtual_memory()}\033[m")
print(f"Fabricante do Equipamento: \033[0;31m{my_system.Manufacturer}\033[m")
print(f"Modelo do Equipamento / Placa Mãe: \033[0;31m{my_system. Model}\033[m")
print(f"Família do Equipamento: \033[0;31m{my_system.SystemFamily}\033[m\n")