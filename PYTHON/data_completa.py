# Importa o módulo datetime.
import datetime
# Exibe a data atual.
x = datetime.datetime.now()
# print(f'\n{x}')

print(f'\nHoje é o {x.strftime("%j")}º dia do ano.') # Número do dia do ano

print(f'\nEstamos na {x.strftime("%U")}ª semana do ano de {x.strftime("%Y")}.') # Número da semana do ano, domingo como primeiro dia da semana
# print(f'\nEstamos na {x.strftime("%W")}ª semana do ano de {x.strftime("%Y")}.') # Número da semana do ano, segunda-feira como o primeiro dia da semana

periodo = x.strftime("%p") # AM/PM
if periodo == 'AM':
    print(f'\nO período agora é {periodo} (Ante Meridiem) que significa "antes do meio-dia".')
else:
    periodo == 'PM'
    print(f'\nO período agora é {periodo} (Post Meridiem) que significa "após o meio-dia".')

print(f'\nO número do dia da semana é {x.strftime("%w")}.') # Dia da semana

print(f'\nHoje é dia {x.strftime("%d")}/{x.strftime("%m")}/{x.strftime("%Y")}.') # Dia, mês e ano

print(f'\nSão {x.strftime("%H")} hora(s) {x.strftime("%M")} minuto(s) e {x.strftime("%S")} segundo(s).') # Hora





print()
'''








print(f'\n{x.strftime("%c")}') # Versão local de data e hora
print(f'\n{x.strftime("%C")}') # Século
print(f'\n{x.strftime("%X")}') # Versão local da hora


































































# Importa o módulo datetime.
import datetime
# Exibe a data atual.
x = datetime.datetime.now()
print(f'\n{x}')
print(f'\n{x.strftime("%A")}') # Dia da semana
print(f'\n{x.strftime("%w")}') # Número do dia da semana
print(f'\n{x.strftime("%d")}') # Dia
print(f'\n{x.strftime("%B")}') # Mês
print(f'\n{x.strftime("%m")}') # Número do mês
print(f'\n{x.strftime("%Y")}') # Ano
print(f'\n{x.strftime("%H")}') # Hora
print(f'\n{x.strftime("%p")}') # AM/PM
print(f'\n{x.strftime("%M")}') # Minutos
print(f'\n{x.strftime("%S")}') # Segundos
print(f'\n{x.strftime("%f")}') # Microssegundo
print(f'\n{x.strftime("%j")}') # Número do dia do ano
print(f'\n{x.strftime("%U")}') # Número da semana do ano, domingo como primeiro dia da semana
print(f'\n{x.strftime("%W")}') # Número da semana do ano, segunda-feira como o primeiro dia da semana
print(f'\n{x.strftime("%c")}') # Versão local de data e hora
print(f'\n{x.strftime("%C")}') # Século
print(f'\n{x.strftime("%X")}') # Versão local da hora
print(f'\n{x.strftime("%G")}') # Ano ISO 8601
print(f'\n{x.strftime("%u")}') # Dia da semana ISO 8601
print(f'\n{x.strftime("%V")}') # Número da semana ISO 8601
print()






'''