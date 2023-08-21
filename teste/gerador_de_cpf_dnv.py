import random

nove_digitos= ''

for n in range(9):
    nove_digitos += str(random.randint(0,9))

multiplicador1 = 10

resultado1 = 0

for digito in nove_digitos:
    resultado1 += int(digito) * multiplicador1
    multiplicador1 -= 1
digito1 = (resultado1 * 10) % 11
digito1 = digito1 if digito1 <= 9 else 0

dez_digito = nove_digitos + str(digito1)
multiplicador2 = 11

resultado2 = 0
for digito in dez_digito:
    resultado2 += int(digito) * multiplicador2
    multiplicador2 -= 1
digito2 = (resultado2 * 10) % 11
digito2 = digito2 if digito2 <= 9 else 0

cpf_gerado = f'{nove_digitos}{digito1}{digito2}'
cpf_gerado_formatado = f'{nove_digitos[0:3]}.{nove_digitos[3:6]}.{nove_digitos[6:9]}-{digito1}{digito2}'

print(f'O CPF gerado é: {cpf_gerado_formatado}')



