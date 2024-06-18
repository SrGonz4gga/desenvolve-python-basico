import random

def embaralhar_palavras(frase):
  
  palavras = frase.split()
  for i, palavra in enumerate(palavras):
    if len(palavra) <= 2:
      continue

    letras_internas = list(palavra[1:-1])
    random.shuffle(letras_internas)

    palavras[i] = palavra[0] + "".join(letras_internas) + palavra[-1]

  return " ".join(palavras)

