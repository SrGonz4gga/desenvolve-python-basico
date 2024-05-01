d = float(input("Digite a distância em km da entrega: "))
p = float(input("Digite o peso do pacote em kg: "))
if d <= 100:
    frete = 1*p
elif 101 <= d <= 300:
    frete = 1.5*p
elif d >= 300:
    frete = 2*p
if p > 10:
    frete += 10
print(f"O valor do frete é: R${frete:.2f}")