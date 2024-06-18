def is_cpf_valid(cpf):
  cpf = cpf.replace(".", "").replace("-", "")

  if len(cpf) != 11:
    return False

  digitos = list(cpf)

  soma_primeiro_dv = 0
  for i, digito in enumerate(digitos[:9]):
    soma_primeiro_dv += int(digito) * (10 - i)
  resto_primeiro_dv = soma_primeiro_dv % 11
  if resto_primeiro_dv < 2:
    primeiro_dv = 0
  else:
    primeiro_dv = 11 - resto_primeiro_dv

  soma_segundo_dv = 0
  for i, digito in enumerate(digitos[:10]):
    soma_segundo_dv += int(digito) * (11 - i)
  resto_segundo_dv = soma_segundo_dv % 11
  if resto_segundo_dv < 2:
    segundo_dv = 0
  else:
    segundo_dv = 11 - resto_segundo_dv

  digitos_verificadores = f"{primeiro_dv}{segundo_dv}"
  if digitos_verificadores == cpf[-2:]:
    return True
  else:
    return False

while True:
  cpf = input("Digite o CPF: ")

  if is_cpf_valid(cpf):
    print("CPF válido")
  else:
    print("CPF inválido")
