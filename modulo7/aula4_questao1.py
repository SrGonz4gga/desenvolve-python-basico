import os
frase = input("Digite uma frase: ")

arquivo = open('texto.txt', 'w')
arquivo.write(frase)

print(f"A frase foi salva em {os.path.abspath('texto.txt')}")

