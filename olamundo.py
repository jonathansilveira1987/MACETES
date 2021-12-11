print('''Escolha uma das opções de Olá mundo:
[ 1 ] Verde
[ 2 ] Amarelo
[ 3 ] Vermelho''')

try:
    escolha = int(input("Qual das opções? ").strip())

    if escolha == 1:
        print("\033[1;32mOlá, mundo!\033[m")
    elif escolha == 2:
        print("\033[1;33mOlá, mundo!\033[m")
    elif escolha == 3:
        print("\033[1;31mOlá, mundo!\033[m")

    else:
        print("Opção não aceita! Escolha entre 1, 2 ou 3.")
except ValueError:
    print('COMANDO NÃO ACEITO!')

# (Obs. Esse foi meu codigo usando cores e outras coisas, mas o que vai resolver é 
# colocar o TRY, e o if dentro dele. Caso o usuario digite outra coisa, o EXCEPT VALUEERROR 
# vai resolver mostrando um print.