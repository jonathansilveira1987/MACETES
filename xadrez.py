rows = int(input('\nEnter number of rows: '))
print('\n')
for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if i == j or i + j == rows + 1:
            print('X', end=' ')
        else:
            print('O', end=' ')
    print()
print('\n')