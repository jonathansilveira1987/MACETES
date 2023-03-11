# Contando vogais em Tupla.

palavras = ("aprender", "programar", "linguagem", "python",
            "curso", "gratis", "estudar", "praticar",
            "trabalhar", "mercado", "programador", "futuro",
            "anticonstitucionalissimamente", "Oftalmotorrinolaringologista",
            "Inconstitucionalissimamente", "Otorrinolaringologista")

for p in palavras:
    print(f"\nNa palavra {p.upper()} temos as vogais ->", end=" ")
    for letra in p:
        if letra.lower() in "aeiou":
            print(letra, end=" ")