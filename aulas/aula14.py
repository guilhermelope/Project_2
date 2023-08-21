frase = 'O Python é uma liguagem de programação multiparadigma Python foi criado por Guido van Rossun.'
i = 0
qtd_apareceu_mais_vezes = 0
letra_que_apareceu_mais_vezes = ''
while i < len(frase):
    letra_atual = frase[i]
    if letra_atual == ' ':
        i += 1
        continue
    quantas_vezes_letra_apareceu_atual= frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < quantas_vezes_letra_apareceu_atual:
        qtd_apareceu_mais_vezes = quantas_vezes_letra_apareceu_atual
        letra_que_apareceu_mais_vezes = letra_atual

    i += 1
print(f'A letra q apareceu mais vezes foi "{letra_que_apareceu_mais_vezes}" que apareceu {qtd_apareceu_mais_vezes}x')