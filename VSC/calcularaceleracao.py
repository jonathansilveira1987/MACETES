# Calcular aceleração.

from datetime import datetime
from datetime import date

while True:
    print('''
    Calcular aceleração.
    [ 1 ] - Fornecer velocidade e tempo.
    [ 2 ] - Fornecer velocidade inicial, velocidade atual e tempo.
    [ 3 ] - Calcular tempo de viagem
    [ 4 ] - 
    [ 5 ] - 
    ''')
    # Programa principal!
    opcao = input('Sua escolha (0 para encerrar): ')

    if opcao in "0":
        break
    elif opcao == '1':
        print('Calcular aceleração com velocidade e tempo.')
        vi = 0
        vf = float(input('Velocidade: '))
        # Transformação de km/h para m/s.
        fator = vf * 1000 / 3600
        ti = 0
        tf = float(input('Tempo: '))
        a = fator / tf
        print(f'A aceleração é de {a} m/s.')
    elif opcao == '2':
        print('\nCalcular aceleração com velocidade inicial, velocidade atual e tempo.')
        vi = float(input('Velocidade inicial: '))
        fatorvi = vi / 3.6
        vf = float(input('Velocidade final: '))
        fatorvf = vf / 3.6
        ti = 0
        tf = float(input('Tempo: '))
        a = (fatorvf - fatorvi) / (tf - 0)
        print(f'A aceleração é de {a} m/s.')








        
    elif opcao == '3':
        print('\nCalcular tempo de viagem.')
        d = float(input('Distância (km): '))
        v = float(input('Velocidade (km/h): '))
        h = d / v
        print(f'O tempo de duração de sua viagem será de {h}.')
        print ('O valor de teste formatado é {:.2f}.'.format(h))
        h = h.strftime("%H:%M")
        print(h)



    elif opcao == '4':
        print('\n\033[0;32mDesculpe, ainda não há algoritmo desenvolvido para essa opção.')
    elif opcao == '5':
        print('\n\033[0;32mDesculpe, ainda não há algoritmo desenvolvido para essa opção.')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    else:
        # Aqui vai o "Tente novamente!"
        opcao != '1, 2, 3, 4, 5'
        print("\n\033[0;31mERRO! Informação incorreta, tente novamente.\033[m\n", end=" ")
        continue
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\n\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break    
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")