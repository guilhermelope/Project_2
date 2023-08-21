#lista = [10, 20, 30, 40, 50]
#lista.append('Guilherme')
#nome = lista.pop()
#print(nome)
#del lista[-1]
#lista.append(60)
#lista.insert(0, 5)
#print(lista)

def multiplo_de(numero, multiplo):
    resultado = numero % multiplo == 0
    print(f'{numero} é múltiplo de {multiplo}?', end=' ')
    print(resultado)
 
 
multiplo_de(16, 3)
multiplo_de(15, 3)
multiplo_de(10, 2)