idade = int(input("Digite sua idade: "))
jogou = input("Já jogou pelo menos 3 jogos de tabuleiro? [S/N]")
if jogou in "SsSimsim":
    jogou = True
else:
    jogou = False
venceu = int(input("Quantas vezes já venceu um jogo? "))

pode_entrar = (16 <= idade <= 18) and (jogou == True) and (venceu >= 1)
print("Apto para ingresso:",pode_entrar) 