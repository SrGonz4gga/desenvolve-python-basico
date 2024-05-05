num = int(input("Digite o número de respondentes: "))
soma = i = 0
while i < num:
    idade = int(input(f"Digite a idade da {i+1}º pessoa: "))
    soma += idade
    i += 1
print(f"A média das idades é {soma/num}")