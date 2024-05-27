urls = []

continuar = 's'
while continuar in 'Ss':
    url = str(input("Digite o endereço URL: "))
    urls.append(url)
    continuar = 'x'
    while continuar not in 'SsNn':
        continuar = str(input("Deseja continuar?"))



dominios = []

for u in urls:
    dominios.append(u[4:-4:1])

print(urls)
print(dominios)

