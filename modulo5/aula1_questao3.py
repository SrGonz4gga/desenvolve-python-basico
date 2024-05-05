from random import randint
from time import sleep

chute = 11

num = randint(1,10)

while chute != num:
    chute = int(input('tente acertar o número de 1 a 10: '))
    print('Processando...')
    sleep(1)
    if abs(chute-num) <= 2:
        print("Está quente")
    elif abs(chute-num)<= 4:
        print("Está morno")
    else:
        print("Está frio")
print("Acertou!!!" if chute == num else "Errou")
print(f"O número era {num}")