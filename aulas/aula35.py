##Conbinations, Permutation e Product - Itertools

from itertools import combinations, permutations, product

def print_iter(iter):
    print(*list(iter), sep='\n')
    print()

pessoas = [
    'João', 'Joana', 'Luiz', 'Leticia'
]

camisetas = [['Preta', 'Branca'],
             ['P', 'M', 'G'],
             ['Masculina', 'Feminina'],
             ['Algodão', 'Linho']
            ]

#print_iter(combinations(pessoas, 2))
#print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas))

