import wmi # Usando o módulo WMI (apenas para Windows) pode ser instalado usando o comando: pip install wmi
c = wmi.WMI()    
my_system = c.Win32_ComputerSystem()[0]
f = open("systeminfo.txt","w");
f.write(str(my_system))
print('Salvo em ' + str(my_system))