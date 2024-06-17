import random
lista_numeros = [random.randint(-10, 10) for _ in range(20)]
print("Lista original:", lista_numeros)

maior_negativos = None
inicio_negativos = None
contagem_negativos = 0

for i, numero in enumerate(lista_numeros):
    if numero < 0:
        if inicio_negativos is None:
            inicio_negativos = i
        contagem_negativos += 1
    else:
        if contagem_negativos > 0:
            if maior_negativos is None or contagem_negativos > maior_negativos:
                maior_negativos = contagem_negativos
                fim_negativos = i - 1

        contagem_negativos = 0
if maior_negativos is not None:
    del lista_numeros[inicio_negativos:fim_negativos + 1]
print("Lista final:", lista_numeros)
