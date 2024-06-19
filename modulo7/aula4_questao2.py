import os

arq1 = open('texto.txt', 'r')
arq2 = open('palavras.txt', 'r+')

linhas = arq1.readlines()
arq2.writelines(linhas)

arq2.close()

arq2 = open('palavras.txt', 'r')
print(arq2.read())
