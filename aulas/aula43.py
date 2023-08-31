def adiciona_cliente(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

cliente1 = adiciona_cliente('Guilherme')
adiciona_cliente('Luiz', cliente1)
print(cliente1)

cliente2 = adiciona_cliente('Neivaldo')
adiciona_cliente('Terezinha', cliente2)
print(cliente2)