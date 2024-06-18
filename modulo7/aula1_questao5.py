def conta_vogais(frase):
  vogais = "aeiouAEIOU"
  numero_vogais = 0
  indices_vogais = []

  for i, letra in enumerate(frase):
    if letra in vogais:
      numero_vogais += 1
      indices_vogais.append(i)

  return numero_vogais, indices_vogais

frase = input("Digite uma frase: ")

numero_vogais, indices_vogais = conta_vogais(frase)

print(f"{numero_vogais} vogais")
print(f"Índices: {indices_vogais}")
