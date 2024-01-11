nums = []
num = int(input("\nQuantos números deseja inserir na lista: "))
print()
while len(nums) < num:
    user_input = int(input("Insira um número inteiro: "))
    nums.append(user_input)
# print(f'\n\033[0;33m{nums}\033[m\n')


# a = [1, 2, 3, 4]
a = nums
b = [sum(a[0:x+1]) for x in range(0, len(a))]
print(f'\n{b}\n')