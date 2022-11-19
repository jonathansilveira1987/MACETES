# pip install phonenumbers
import phonenumbers
#Ajuste do telefone para usar o phonenumbers
phone = input('\nNúmero de telefone com DDD: ')
telefone = ("+55" + phone)
telefone_ajustado = phonenumbers.parse(telefone)
print(f'\n{telefone_ajustado}')
#Descobrir a localização do telefone
from phonenumbers import geocoder
local = geocoder.description_for_number(telefone_ajustado, 'pt-br')
print(f'\nEstado: {local}')
#Formatando um telefone que foi inserido em um formulário
telefone_formulario = phone
telefone_formulario_ajustado = phonenumbers.parse(telefone_formulario, "BR")
telefone_formatado = phonenumbers.format_number(telefone_formulario_ajustado,phonenumbers.PhoneNumberFormat.NATIONAL)
telefone_internacional = phonenumbers.format_number(telefone_formulario_ajustado,phonenumbers.PhoneNumberFormat.INTERNATIONAL)
print(f'\nPadrão Nacional: {telefone_formatado}')
print(f'\nPadrão Internacional: {telefone_internacional}\n')