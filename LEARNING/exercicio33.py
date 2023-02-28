# 33. Letra U.
# Desenvolvido por Jonathan Silveira - Instagram: @ jonathandev01

# J
for row in range(7):
    for col in range(5):
        if (row == 6) or (col in {0, 4,}):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()