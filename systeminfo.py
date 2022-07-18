import os
for line in os.popen('systeminfo'): print(line.rstrip())