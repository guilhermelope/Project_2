def multiplicar(*args):
    total = 1
    for numeros in args:
        total *= numeros 
    return total

def par_inpar(numero):
    if numero % 2 == 0:
        return "ESSE NUMERO É PAR"
    return 'ESSE NUMERO É INPAR'

print(par_inpar(15))