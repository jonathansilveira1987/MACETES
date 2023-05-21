import pandas as pd
import numpy as np
import pandas as pd
import datetime as dt

pnad = pd.read_csv("https://github.com/neylsoncrepalde/introducao_ao_r/blob/master/dados/pes_2012.csv?raw=true")
print('\033[34m')
# pnad.head()

print(pnad)
print()
print(pnad['UF'])
print()
print(pnad.V0302)
print()
print(pnad.describe())

















































print('\033[m')