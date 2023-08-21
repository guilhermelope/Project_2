def zipper(lista1, lista2):
    intervalo_maximo = min(len(lista1), len(lista2))
    return [    #list comprerencion #
        (cidades[i], estados[i]) for i in range(intervalo_maximo)
    ]

def zipper_soma(l1, l2):
    intervalo_maximo = min(len(l1), len(l2))
    return [
        l1[i] + l2[i] for i in range(intervalo_maximo)
    ]

cidades = ["Salvador", "Ubatuba", "Belo Horizonte"]
estados = ["BA", "SP", "MG", "RJ"]

l1 = [1, 2, 3, 4, 5, 6, 7, 8]
l2 = [1, 2, 3, 4]

print(zipper_soma(l1, l2))



