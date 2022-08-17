# Contador Infinito.
from time import sleep
i = 1
print()
while i > 0:
    sleep(0.5)
    print(f'\033[0;31m{i}\033[m')
    i += 1