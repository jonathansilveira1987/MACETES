elemento = int(input('\nInforme o número de elementos para o arquivo: '))
print()
palavras = [input("Dado: ") for i in range(elemento)]
print(f'\n\033[0;32m{palavras}\033[m')
print('\n\033[0;36mOs dados informados foram salvos no arquivo => a1!\033[m\n')
with open('a1.txt', 'a') as arquivo:
    for palavras in palavras:
        arquivo.write(palavras + '\n')