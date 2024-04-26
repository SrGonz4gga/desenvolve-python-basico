valor = int(input("digite o valor: "))

notas_cem = valor//100
valor_1 = valor%100

notas_cinquenta = valor_1//50
valor_2 = valor_1%50

notas_vinte = valor_2//20
valor_3 = valor_2%20

notas_10 = valor_3//10
valor_4 = valor_3%10

notas_5 = valor_4//5
valor_5 = valor_4%5

notas_2 = valor_5//2
valor_6 = valor_5%2

moedas_um = valor_6//1
valor_final = valor_6 - moedas_um



print( 
      '{} Notas de R$100,00 \n'
      '{} Notas de R$50,00  \n'
      '{} Notas de R$20,00  \n'
      '{} Notas de R$10,00  \n'
      '{} Notas de R$5,00   \n'
      '{} Notas de R$2,00   \n'
      '{} Moedas de R$1,00  \n'
      .format(notas_cem, notas_cinquenta, notas_vinte, notas_10, notas_5, notas_2, moedas_um))