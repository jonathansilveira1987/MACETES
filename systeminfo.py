import os
print('\033[0;32m')
for line in os.popen('systeminfo'): print(line.rstrip())
print('\033[m')