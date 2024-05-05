n = int(input("Digite n: "))
maior = 0
while n > 0:
    x = int(input("Digite x: "))
    if x > maior:
        maior = x
    else:
        n -= 1
print(maior)

