n = int(input("Insira o número de linhas: "))

for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print(i+1, end=" ")
        else:
            print(" ", end=" ")
    print()