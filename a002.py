from time import sleep

s = {1, 2, 2, 3, 4, 4}
x = list(s)
print(x[2])

x = {1, 2, 3}
y = {4, 5}
print(x^y)
print()

print('\n')
sleep(1)
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s1.update(s2)
print(s1)

print('\n')
sleep(1)
x, y = "12"
y, z = "34"
print(x, y, z)

print('\n')
sleep(1)
for num in range(-2, -5, -1):
    print(num, end=",")

print('\n')
sleep(1)
n = [1, 34, 55, 4, 8]
x = n[-3: : -1]
print(x)

print('\n')
sleep(2)
a = True
b = False
print(a or a and b)

print('\n')
sleep(2)
dict1 = {'key1':1, "key2":2}
dict2 = {'key2':2, "key1":1}
print(dict1 == dict2)

print('\n')
sleep(2)
a, b, c = 20, 5, 4
print(a-a*b/a//c)

print('\n')
sleep(2)
Dict = {'x':10, 'y':20}
print(20 in Dict)

print('\n')
sleep(2)
l = [1, 2, 3]
l.extend((3, 4, 5))
print(l)

print('\n')
sleep(2)
p = (2, 3)
print(2 * p)

print('\n')
sleep(2)
print(4 + 3 % 5)

print('\n')
sleep(2)
i = 0
while i < 5:
    print(i, end=" ")
    i += 1
    if i == 3:
        break
else:
    print(0)

print('\n')
sleep(2)
x = {1, 2, 3}
y = {4, 5, 6}
print(x|y)

print('\n')
sleep(2)
a = 1|2
b = 2|3
print(a == b)

print('\n')
sleep(2)
tup = (0, 1, 2, 3)
print(tup[::-1])

print('\n')
sleep(2)
print('Fim!\n')
print('\033[m')