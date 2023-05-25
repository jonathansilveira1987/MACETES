# Lista ordenada sem repetições.

lista = []

for c in range(0, 5):
    n = int(input("Digite um valor: "))

    if c == 0 or n > lista[len(lista)-1]:
        lista.append(n)
        print("Adiconado ao final da lista...")
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f"Adiconado na posição {pos} da lista.")
                break
            
            pos = pos + 1
            
print("-=" * 30)
print(f"Os valores digitados em ordem foram {lista}")
print("-=" * 30)