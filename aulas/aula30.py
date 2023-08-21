def concatenar(string_inicial):
    valor_final = string_inicial #Variavel Livre não pode ser alterada se nn for no escopo dele #

    def interna(string_a_concatenar):
        nonlocal valor_final #fala para o python q a variavel livre pode ser alterada#
        valor_final += string_a_concatenar
        return valor_final
    return interna


c = concatenar('a')

print(c('b'))