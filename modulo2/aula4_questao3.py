total = 1

for i in range (3):
    nome = str(input(f"Digite o nome do produto {i+1}: "))
    preco = float(input(f"Digite o preço do produto {i+1}: "))
    quantidade = int(input(f"Digite a quantidade ddo produto {i+1}: "))
    total += (preco*quantidade)

print(f"Total: R${total:.2f}")