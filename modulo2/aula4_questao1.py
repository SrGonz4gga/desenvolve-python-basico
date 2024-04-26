#obtenção dos dados para cálculo da área
comprimento = float(input("Digite o comprimento do terreno em metro: "))
largura = float(input("Digite a largura do terreno em metro: "))
#preço para multiplicar por cada unidade de metro quadrado
area_m2 = comprimento*largura
preço_m2 = float(input("Digite o preço do metro quadrado em reais: "))

print (f"O terreno possui {area_m2} m2, portanto custará R${preço_m2*area_m2}")

