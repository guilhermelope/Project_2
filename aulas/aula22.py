lista = [ 
    {'nome': 'Guilherme', 'Sobrenome': 'Silva Lopes'},
    {'nome': 'Terezina', 'Sobrenome': 'Fatima Silva Lopes'},
    {'nome': 'Neivado', 'Sobrenome': 'Aparecido Lopes'},
    {'nome': 'Luiz Henrique', 'Sobrenome': 'Lopes'},
    {'nome': 'Leonardo', 'Sobrenome': 'Silva Lopes'},
]
 
def exibir(lista):
    for item in lista:
        print(item)
    print()

l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['Sobrenome'])


exibir(l1)
exibir(l2)