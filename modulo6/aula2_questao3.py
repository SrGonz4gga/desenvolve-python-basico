from random import randint 

lista1 = []
lista2 = []
lista3 = []

for i in range (20):
    if i <= 9:
        lista1.append(randint(0, 50))
    else:
        lista2.append(randint(0,50))

for n in lista1:
    if n in lista2:
        lista3.append(n)

contador_lista1 = []
for valor in lista1:
    if valor not in contador_lista1:
        contador_lista1.append((valor, 1))
    else:
        for i, (item, count) in enumerate(contador_lista1):
            if item == valor:
                contador_lista1[i] = (item, count + 1)
                break

contador_lista2 = []
for valor in lista2:
    if valor not in contador_lista2:
        contador_lista2.append((valor, 1))
    else:
        for i, (item, count) in enumerate(contador_lista2):
            if item == valor:
                contador_lista2[i] = (item, count + 1)
                break

print(lista1)
print(lista2)
print(sorted(lista3))

print("\nContagem:")
for valor in lista3:
    contagem_lista1 = 0
    contagem_lista2 = 0

    for item, count in contador_lista1:
        if item == valor:
            contagem_lista1 = count
            break

    for item, count in contador_lista2:
        if item == valor:
            contagem_lista2 = count
            break

    print(f"{valor}: (lista1: {contagem_lista1}, lista2: {contagem_lista2})")
