a = lambda a: print(a)
a('Olá')
x = type(a)
print(x)

b = lambda a: lambda b: print(a, b)
b('Oi')('Tchau')
z = type(b)
print(z)