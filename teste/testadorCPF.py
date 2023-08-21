import re
import os
print('Testador de CPF')
entrada = input('Digite seu CPF: ')
cpf = re.sub(r'[^0-9]', '', entrada)
nove_digitos = cpf[:9]
entrada_senquecial = cpf == cpf[0] * len(cpf)
multiplicador_1 = 10

if entrada_senquecial:
    print('Caracteris repetidos !!!')

resultado_1 = 0
for digito in nove_digitos:
    resultado_1 += int(digito) * multiplicador_1
    multiplicador_1 -= 1
digito_1 = (resultado_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

multiplicador_2 = 11
dez_digitos = cpf[:10]

resultado_2 = 0
for digito in dez_digitos:
    resultado_2 += int(digito) * multiplicador_2
    multiplicador_2 -= 1
digito_2 = (resultado_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

novo_cpf = f'{nove_digitos}{digito_1}{digito_2}'

novo_cpf_formatado = f'{nove_digitos[0:3]}.{nove_digitos[3:6]}.{nove_digitos[6:9]}-{digito_1}{digito_2}'

if cpf == novo_cpf:
    print(f'CPF:{novo_cpf_formatado} VALIDO !!!')
else:
    print(f'CPF:{novo_cpf_formatado} INVALIDO !!!')