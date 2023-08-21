from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10.50},
    {'nome': 'Produto 1', 'preco': 11.25},
    {'nome': 'Produto 3', 'preco': 20.10},
    {'nome': 'Produto 2', 'preco': 5.05},
    {'nome': 'Produto 4', 'preco': 15.56},
]

def funcao_reduce(acumulador, produto):
    print("acumulador", acumulador)
    print("produto", produto),
    print()
    return acumulador + produto['preco']

total = reduce(funcao_reduce,produtos,0)

print(total)