n = int(input('Digite um número'))
print('- - - - '* 5)
print('[1] BINÁRIO')
print('[2] OCTAL')
print('[3] HEXADECIMAL')

pgnt = str(input('DIGITE A OPÇÃO QUE DESEJA CONVERTER:'))
if pgnt == '1':
    bean = str(bin(n))
    print(bean)
elif pgnt == '2':
    lol = str(oct(n))
    print(lol)
elif pgnt == '3':
    xq = str(hex(n))
    print(xq)