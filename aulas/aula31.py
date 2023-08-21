def cria_funcao(func):
    def interna(*args, **kwargs):
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print(f'Seu resultado foi {resultado}')
        return resultado
    return interna

@cria_funcao
def inverter_string(string):
    return string[::-1]

def e_string(param):
    if not isinstance(param, str):
        raise TypeError("Param deve ser uma string")
    
entrada = input("Digite que será invertida: ")

invertida = inverter_string(entrada)



