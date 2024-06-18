def imprimir_nome_escada(nome):
  for i in range(1, len(nome) + 1):
    print(nome[:i])

nome = input("Digite seu nome: ")
imprimir_nome_escada(nome.upper())  # Converte para maiúsculas
