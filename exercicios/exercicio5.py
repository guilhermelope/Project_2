"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
entrada = input('Digite um numero inteiro:')
numero = int(entrada)
mod = numero % 2

if mod == 0:
    print('Seu numero é par')
else:
    print('Seu numero é inpar')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
entrada = input('Qual o horario de agora:')
hora = int(entrada)

if hora >= 0 and hora <= 11:
    print('Bom Dia')
elif hora >= 12 and hora <=17:
    print('Boa Tarde')
else:
    print('Boa Noite')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""
entrada = input('Digite seu Nome aki:')

nome = len(entrada)

if nome >= 0 and nome <= 4:
    print('Seu nome é curto')
elif nome >= 5 and nome <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é grande')        