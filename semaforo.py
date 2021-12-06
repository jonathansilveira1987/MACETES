# Semáforo.

# Programa principal!
print('\nSemáforo.')

cor = input('\nCor: ')

if cor == 'verde':
    print('\n\033[0;32mAcelerar!\033[m\n')
elif cor == 'amarelo':
    print('\n\033[0;33mAtenção!\033[m\n')
else:
    print('\n\033[0;31mParar!\033[m\n')