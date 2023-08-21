import os

palavra_secreta = 'geladeira'
letra_acertadas = ''
numero_tentativas = 0

while True:

    entrada = input("Digite uma letra: ")
    numero_tentativas += 1 

    if len(entrada) > 1:
        print("Digite uma Letra por vez !!!")
        continue

    if entrada in palavra_secreta:
        letra_acertadas += entrada

    palavra_formada = ''

    for letra_secreta in palavra_secreta:
        if letra_secreta in letra_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print(f"Palavra Formada: {palavra_formada}")

    if palavra_formada == palavra_secreta:
        os.system('CLS')
        print("VOCÊ GANHOU PARABENS !!!")
        print(f"A palavra secreta era {palavra_secreta}")
        print(f'Quantidade de tentativas usada foi {numero_tentativas}')
        palavra_secreta = 'geladeira'
        letra_acertadas = ''
        numero_tentativas = 0