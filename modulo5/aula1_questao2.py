from random import randint
from math import sqrt
soma = 0

n = int(input("Digite número de valores a serem gerados: "))

for i in range (n):
    aleatorio = randint(0,100)
    print(aleatorio)
    soma += aleatorio

raiz_soma = sqrt(soma)
print(f"A raiz da soma é {raiz_soma}")

