lista = []
i = 0
while True:
    n = int(input("Digite um valor (000 para parar)"))
    if (n == 000) and (i>4) : break
    if n!=000:
        lista.append(n)
    i += 1

print(lista)
print(lista[0:3:1])
print(lista[-1:-3:-1])
print(lista[::-1])
print(lista[0:-1:2])
print(lista[1:-1:2])