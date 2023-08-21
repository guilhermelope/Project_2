import re
print("Testador de CPF")
entrada = input("DIgite seu CPF: ")

cpf = re.sub(r'[^0-9]', '', entrada)

entrada_sequencial = cpf == cpf[0] * len(cpf)

if entrada_sequencial:
    print("NUMEROS SEQUENCIAIS DETECTADOS !!!")
    exit()


nove_digito = cpf[:9]
multiplicador1 = 10

resultado1 = 0
for digito in nove_digito:
    resultado1 += int(digito) * multiplicador1
    multiplicador1 -= 1
digito1 = (resultado1 * 10) % 11
digito1 = digito1 if digito1 <= 9 else 0

dez_digito = cpf[:10]
multiplicador2 = 11

resultado2 = 0
for digito in dez_digito:
    resultado2 += int(digito) * multiplicador2
    multiplicador2 -= 1
digito2 = (resultado2 * 10) % 11
digito2 = digito2 if digito2 <= 9 else 0

novo_cpf = f'{nove_digito}{digito1}{digito2}'
novo_cpf_formatado = f'{nove_digito[0:3]}.{nove_digito[3:6]}.{nove_digito[6:9]}-{digito1}{digito2}'

if cpf == novo_cpf:
    print("SEU CPF É VALIDO !!!")
else:
    print("SEU CPF É INVALIDO !!!")

