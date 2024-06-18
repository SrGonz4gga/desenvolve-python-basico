def contar_espacos_branco(frase):
  contador_espaco = 0
  for caractere in frase:
    if caractere == " ":
      contador_espaco += 1
  return contador_espaco

frase = input("Digite a frase: ")
numero_espacos = contar_espacos_branco(frase)
print(f"Espaços em branco: {numero_espacos}")
