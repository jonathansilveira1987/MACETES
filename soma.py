nums = []
num = float(input("\nQuantos valores deseja inserir na lista: "))
print()
while len(nums) < num:
    user_input = float(input("Valor: "))
    nums.append(user_input)
listSum = sum(nums)
print(f"\nA soma dos valores \033[0;33m{nums}\033[m = \033[0;34m{listSum}\033[m\n")