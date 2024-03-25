cpf_informado = list(input('Digite o número do CPF: '))
cpf_a_validar = cpf_informado[0:9]
multiplicador = 10
soma = 0
for i in range(9):
    fator = int(cpf_a_validar[i])
    soma += fator * multiplicador
    multiplicador -= 1
if(soma % 11 == 1 or soma % 11 == 0):
    digito_um = 0
else:
    digito_um = 11 - (soma % 11)

cpf_a_validar.append(str(digito_um))
multiplicador = 11
soma = 0
for i in range(10):
    fator = int(cpf_a_validar[i])
    soma += fator * multiplicador
    multiplicador -= 1  
if(soma % 11 == 1 or soma % 11 == 0):
    digito_dois = 0
else:
    digito_dois = 11 - (soma % 11)

cpf_a_validar.append(str(digito_dois))

if(cpf_informado == cpf_a_validar):
    print('O CPF informado foi digitado corretamente.')
else:
    print('O CPF foi digitado incorretamente. Tente novamente!')