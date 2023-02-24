texto = ' Título '
print(f'\n\033[0;32m{texto}\033[m') # Normal.
print(f'\n\033[0;33m{texto: ^50}\033[m') # Centralizado.
print(f'\n\033[0;34m{texto:.^50}\033[m') # Centralizado.
print(f'\n\033[0;35m{texto:.<50}\033[m') # Alinhado a direita.
print(f'\n\033[0;36m{texto:.>50}\033[m') # Alinhado a esquerda.
print()

import speedtest
r = speedtest.Speedtest()
print(r)





# import speedtest module 
import speedtest

speed_test = speedtest.teste()

download_speed = speed_test.download()
print("Your Download speed is", download_speed) 

upload_speed = speed_test.upload()
print("Your Upload speed is", upload_speed)