# A

print('\n')
for row in range(7):
    for col in range(5):
        if (row==0) and (col in {1,2,3}):
            print("\033[0;32m*\033[m", end=" ")
        elif (row in {1,2,3,4,5,6}) and (col in {0,4}):
            print("\033[0;32m*\033[m", end=" ")
        elif row==3:
            print("\033[0;32m*\033[m", end=" ")
        else:
            print(" ", end=" ")
    print()
print('\n')