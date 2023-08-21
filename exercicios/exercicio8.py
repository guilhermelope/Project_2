import os
i = 0
lista = []
letras_validas = None
letras_permitidas = 'ial'

while True:
    entrada = input(f'Selecione uma opção \n [i]nserir [a]pagar [l]istar: ').lower()

    if entrada not in letras_permitidas:
        print('Digite uma das letras pedidas [i] [a] [l]')
        continue 
    
    if entrada == 'a':
        os.system('CLS')
        item_apagar = input('Escolha o indice que deseja apagar: ')
        try:
            item_apagar_numero = int(item_apagar)
            del lista[item_apagar_numero]
        except ValueError:
            print('Digite somente numeros')
        except IndexError:
            print('indice não encontrado')

    elif entrada == 'l':
        os.system('CLS')
        if len(lista) == 0:
         print('Nada para listar')

        for indice, nome in enumerate(lista):
            print(indice, nome)

    elif entrada == 'i':
       os.system('CLS')
       nome_na_lista = input('Digite um Valor: ')
       lista.append(nome_na_lista)