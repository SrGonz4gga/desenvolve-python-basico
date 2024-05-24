from random import randint
elementos = []
num_elementos = randint(5, 20)
for i in range(num_elementos):
    elementos.append(randint(1,10))

print(elementos)
print(sum(elementos))
print(sum(elementos)/num_elementos)
