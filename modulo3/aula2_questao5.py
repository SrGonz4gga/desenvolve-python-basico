genero       = input("Qual o seu gênero? [M/F] ")
idade        = int(input("Quantos anos você tem? "))
contribuicao = int(input("Quantos anos de contribuição com o INSS você tem? "))

a = ((genero == 'F' or 'f') and idade > 60) or ((genero == 'M' or 'm') and idade >65)

b = (contribuicao >=30)

c = (idade >= 60 and contribuicao >=25)

pode_aposentar = a or b or c

print(pode_aposentar)