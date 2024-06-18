import random

def encrypt(nomes):
  chave_aleatoria = random.randint(1, 10)
  nomes_cript = []
  for nome in nomes:
    nome_cript = ""
    for letra in nome:
      codigo_ascii = ord(letra) #A função 'ord' é utilizada para obter o valor numérico de um caractere

      if 33 <= codigo_ascii <= 126:
        codigo_ascii_cript = codigo_ascii + chave_aleatoria

        if 33 <= codigo_ascii_cript <= 126:
          letra_cript = chr(codigo_ascii_cript) # O chr retorna a representação de caractere correspondente ao código Unicode fornecido como argumento.
        else:
          letra_cript = chr(codigo_ascii_cript - 126 + 33)
      else:
        letra_cript = letra

      nome_cript += letra_cript

    nomes_cript.append(nome_cript)

  return nomes_cript, chave_aleatoria

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_cript, chave_aleatoria = encrypt(nomes)

print(f"Nomes criptografados: {nomes_cript}")
print(f"Chave aleatória: {chave_aleatoria}")
