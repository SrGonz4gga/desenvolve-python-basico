tipo = input("Qual a classe do personagem? ")
forca = int(input("Quantos pontos de força? "))
magia = int(input("Quantos pontos de magia? "))
if tipo == "guerreiro":
    valido = (forca >= 15) and (magia<=10)
elif tipo == "mago":
    valido = (forca <= 10) and (magia >= 15)
elif tipo == "arqueiro":
    valido = (5 < forca <= 15) and (5 < magia <= 15)
else:
    print("Tipo inválido")

print("Atributos consistentes com a classe escolhida:", valido)