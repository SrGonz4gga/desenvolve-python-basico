while True:
    frase = input('Digite uma frase (digite "fim" para encerrar): ')
    if frase.lower() == "fim":
        break
    frase_reescrita = ''.join(char.lower() for char in frase if char.isalnum())
    if frase_reescrita == frase_reescrita[::-1]:
        print(f'"{frase}" é palíndromo')
    else:
        print(f'"{frase}" não é palíndromo')
