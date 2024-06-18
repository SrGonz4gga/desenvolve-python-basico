def validador_senha(senha):
    if len(senha) < 8:
        return False

    tem_maiuscula = True
    tem_minuscula = True
    tem_numero = True
    tem_especial = True
    
    for char in senha:
        if char.isupper():
            tem_maiuscula = True
        elif char.islower():
            tem_minuscula = True
        elif char.isdigit():
            tem_numero = True
        elif not char.isalnum():
            tem_especial = True
    
    return tem_maiuscula and tem_minuscula and tem_numero and tem_especial

