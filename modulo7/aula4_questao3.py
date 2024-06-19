import os

n_linhas = 0

f = open('estomago.txt', 'r')

for i in range(25):
    linha = f.readline()
    if linha:
        print(linha.strip())

for i in f:
    n_linhas += 1 

print(n_linhas)