


# Lista de fusos horários.
import pytz
print()
for tz in pytz.all_timezones:
    print(f'\033[0;33m{tz}\033[m')
print()

conteudo  = tz

with open('lista01.txt', 'w') as arquivo:
    arquivo.write("\n".join(conteudo))
    arquivo.write(f'\nTotal de arquivos {len(conteudo)}') # Informa total de arquivos.






'''

with open('lista01.txt', 'w') as arquivo:
    arquivo.write(str(conteudo))




# conteudo = [1, 2, 3]
# Primeira solução.
elemento = int(input('\nInforme o número de elementos para a lista: '))
print()
conteudo = [input("Dado: ") for i in range(elemento)]
print(f'\n\033[0;32m{conteudo}\033[m')

'''