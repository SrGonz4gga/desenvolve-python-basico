N = int(input('Quantos experimentos foram realizados? '))
cont = 1
coelhos = 0
sapos = 0
ratos = 0
total = 0

while cont <= N:
    tipo = input('Qual o tipo de cobaia utilizada?')

    if tipo == 'c' or 'C':
        cobaias = int(input('Quantas cobaias foram utilizadas?'))
        total += cobaias
        coelhos += cobaias
        cont+=1

    tipo = input('Qual o tipo de cobaia utilizada?')

    if tipo == 's' or 'S':
        cobaias = int(input('Quantas cobaias foram utilizadas?'))
        total += cobaias
        sapos += cobaias
        cont += 1

    tipo = input('Qual o tipo de cobaia utilizada?')

    if tipo == 'r' or 'R':
        cobaias = int(input('Quantas cobaias foram utilizadas?'))
        total += cobaias
        ratos += cobaias
        cont += 1

print (f'Total de cobaias : {total}')
print(f'Total de coelhos : {coelhos}')
print(f'Total de sapos : {sapos}')
print(f'Total de ratos : {ratos}')
print(f'Percentual de coelhos: {(coelhos/total)*100:.1f}%')
print(f'Percentual de sapos: {(sapos/total)*100:.1f}%')
print(f'Percentual de ratos: {(ratos/total)*100:.1f}%')