def formata_numero(numero):
  numero = numero.strip()

  if len(numero) < 8 or len(numero) > 9:
    return None
  
  elif len(numero) == 8:
    numero = "9" + numero

  elif len(numero) == 9:
    if numero[0] != "9":
      return None

  numero_formatado = f"{numero[:5]}-{numero[5:]}"

  return numero_formatado

while True:
  numero = input("Digite o número: ")
  numero_formatado = formata_numero(numero)

  if numero_formatado == None:
    print("Número inválido, o número deve começar com 9 e ter 9 dígitos")
  
  else:
    print(f"Número completo: {numero_formatado}")
