from random import randint
lista = []

for i in range(20):
    lista.append(randint(-100,100))

print (sorted(lista))
print(lista)
print(max(lista))
print(min(lista))
