from functools import partial

def print_iter(iter):
    print(*list(iter), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.50},
    {'nome': 'Produto 1', 'preco': 11.25},
    {'nome': 'Produto 3', 'preco': 20.10},
    {'nome': 'Produto 2', 'preco': 5.05},
    {'nome': 'Produto 4', 'preco': 15.56},
]

def aumentar_porcen(valor, porcen):
    return round(valor * porcen, 2)

#novos_produtos = [
#    {**p, 'preco': aumentar_dez_porcen(p['preco'])} for p in produtos
#                 ]

def muda_preco_produtos(produto):
    return {**produto, 'preco': produto['preco'] * 1.2}

novos_produtos = map(muda_preco_produtos, produtos) # Para Mapear uma lista 

print_iter(novos_produtos)

print(list(map(lambda x: x * 3, [1, 2, 3, 4, 5, 6])))