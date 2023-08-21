pessoa = {
    'nome': 'Guilherme',
    'sobrenome': 'Silva Lopes'
}

dados_pessoa = {
    'idade': 18,
    'altura': 1.80
}

pessoa_completa = {**pessoa, **dados_pessoa}

def mostra_argumentos(*args, **kwargs):
    print('Argumentos não Nomeados: ', args)

    for chave, valor in kwargs.items():
        print(chave, valor)

mostra_argumentos(**pessoa_completa)