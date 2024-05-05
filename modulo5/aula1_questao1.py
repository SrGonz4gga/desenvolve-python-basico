n1 = float(input("Digite o primeiro número decimal: "))
n2 = float(input("Digite o segundo número decimal: "))

diferenca_absoluta = abs(n1 - n2)
diferenca_absoluta_arredondada = round(diferenca_absoluta, 2)

print(f"A diferença absoluta entre {n1} e {n2} é {diferenca_absoluta_arredondada}")
