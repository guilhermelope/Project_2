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

novos_produtos = filter( ## Para filtrar em um lista
    lambda p: p ['preco'] > 10,
    produtos
)

print_iter(novos_produtos)