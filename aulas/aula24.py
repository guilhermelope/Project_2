import pprint

lista = []

def imprimir(valor):
    pprint.pprint(valor)

for numero in range(10):
    lista.append(numero)

lista = [numero*2 for numero in range(10)]

#print(lista)

produtos = [

    {'produto': 'café', 'valor': 10},
    {'produto': 'pizza', 'valor': 50},
    {'produto': 'celular', 'valor': 1000},

]

novos_produtos = [
    {**produto , 'valor': produto['valor'] * 1.05}
    if produto['valor'] > 20 else {**produto}
    for produto in produtos
    if produto['valor'] > 20
]

lista3 = ['a',1,2,3,4,5,'corno',True,[0,1,2], (0,1), {0,2}, {'nome': 'Guilherme'}]

for item in lista3:
    if isinstance(item, (str,int)):
        print(item, isinstance(item, (str,int)))
    