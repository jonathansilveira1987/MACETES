# Tuplas com Times de Futebol.

times = ("Corinthians", "Palmeiras", "Santos", "Grêmio",
         "Cruzeiro", "Flamengo", "Vasco", "Chapecoense",
          "Atlético", "Botafogo", "Atlético-PR", "Bahia", 
        "São Paulo", "Fluminense", "Sport Recife",
         "EC Vitória", "Coritiba", "Avaí", "Ponte Preta",
          "Atlético-GO")

print("-=" * 15)
print(f"Lista de Times: {times}")
print("-=" * 15)
print(f"Os 5 primeiros são {times[0:5]}")
print("-=" * 15)
print(f"Os 4 útlimos são: {times[-4:]}")
print("-=" * 15)
print(f"Times em ordem alfabética: {sorted(times)}")
print("-=" * 15)
print(f'Posição do Chapecoense: {times.index("Chapecoense")+1}ª posição.')
print("-=" * 15)