nums = []
num = float(input("\nQuantos valores deseja inserir na lista: "))
print()
while len(nums) < num:
    user_input = float(input("Valor: "))
    nums.append(user_input)
listSum = sum(nums)
print(f"\nA soma dos valores \033[0;33m{nums}\033[m = \033[0;34m{listSum:.2f}\033[m\n")


def real(valor):
    a = "{:,.2f}".format(float(valor))
    b = a.replace(',','v')
    c = b.replace('.',',')
    return c.replace('v','.')
# moeda = float(input('\nDigite o valor: '))
print(f'\nA soma dos valores ficou em R$ {real(listSum)} reais.\n')