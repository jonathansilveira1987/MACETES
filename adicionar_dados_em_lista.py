# Primeira solução.
num = int(input('\nInforme o número de dados para a lista: '))
print()
lista = [input("Dado: ") for i in range(num)]
print(f'\n\033[0;32m{lista}\033[m')

# Segunda solução.
nums = []
num = int(input("\nQuantos números deseja inserir na lista: "))
print()
while len(nums) < num:
    user_input = int(input("Insira um número inteiro: "))
    nums.append(user_input)
print(f'\n\033[0;33m{nums}\033[m\n')