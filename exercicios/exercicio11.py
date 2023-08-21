import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.50},
    {'nome': 'Produto 1', 'preco': 11.25},
    {'nome': 'Produto 3', 'preco': 20.10},
    {'nome': 'Produto 2', 'preco': 5.05},
    {'nome': 'Produto 4', 'preco': 15.56},
]

novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(produtos)
]


produtos_ordenado_por_nome = sorted( #Usado para ordenar um dicionario#
    copy.deepcopy(produtos),
    key=lambda produto: produto['nome'],#Função para ordenar do maior para o menor foi coloca Reverse= True #
     reverse= True
)

produtos_ordenado_por_preco = sorted( #Usado para ordenar um dicionario#
    copy.deepcopy(produtos),
    key=lambda preco: preco['preco'] #Função para ordenar do menor para o maior#
)
print(*produtos, sep='\n') #Para imprimir uma lista pulando 1 linha para cada lista#
print()
print(*novos_produtos, sep='\n')
print()
print(*produtos_ordenado_por_nome, sep='\n')
print()
print(*produtos_ordenado_por_preco, sep='\n')
