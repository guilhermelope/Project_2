import os

palavra_sacreta = 'cadeira'
letras_acertadas = ''
numero_tentativas = 0


while True:

    entrada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(entrada) > 1:
        print(f'Digite apenas um letra !!!')
        continue

    if entrada in palavra_sacreta:
        letras_acertadas += entrada

    palavra_formada = ''

    for letra_secreta in palavra_sacreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print(f'Palavra formada {palavra_formada}')

    if palavra_formada == palavra_sacreta:
        os.system('CLS')
        print(' VOCÊ GANHOU O JOGO !!!!')
        print(f'A palavra era {palavra_sacreta}')
        print(f'Numero de tentativas {numero_tentativas}')
        palavra_sacreta = 'cadeira'
        letras_acertadas = ''
        numero_tentativas = 0