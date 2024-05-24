def intercalar_listas_simples(lista1, lista2):
  
  lista_intercalada = []
  for i in range(len(max(lista1, lista2, key=len))):
    if i < len(lista1):
      lista_intercalada.append(lista1[i])
    if i < len(lista2):
      lista_intercalada.append(lista2[i])
  return lista_intercalada

qtd_elementos_lista1 = int(input("Digite a quantidade de elementos da lista 1: "))
lista1 = []
for i in range(qtd_elementos_lista1):
  elemento = int(input(f"Digite o {i + 1}º elemento da lista 1: "))
  lista1.append(elemento)

qtd_elementos_lista2 = int(input("Digite a quantidade de elementos da lista 2: "))
lista2 = []
for i in range(qtd_elementos_lista2):
  elemento = int(input(f"Digite o {i + 1}º elemento da lista 2: "))
  lista2.append(elemento)


lista_intercalada = intercalar_listas_simples(lista1, lista2)
print("\nLista intercalada:", lista_intercalada)
