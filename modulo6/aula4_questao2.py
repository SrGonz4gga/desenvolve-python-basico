frase = str(input("Digite a frase: ")).lower().strip()
vogais = [i for i in frase if i in "aeiou"]
print(sorted(vogais))

consoantes = [c for c in frase if c not in "aeiou "]
print(consoantes)

