
while True:
    entrada1 = input('Digite o primeiro numero: ')
    operador = input('Digite o operador (+-*/): ')
    entrada2 = input('Digite o segundo numero: ')
    numeros_validos = None
    n1 = float(entrada1)
    n2 = float(entrada2)

    try:
        numeros_validos = True
    except:
        numeros_validos = None
    
    if numeros_validos is None:
        print('Um dos numeros são invalidos')
        continue

    operadores_permitidos = '+-*/'

    if operador not in operadores_permitidos:
        print('Operador invalido')
        continue

    if len(operador) > 1:
        print('Somente operadores aki!!')
        continue
    
    if operador == '+':
        soma = n1 + n2
        print(f'O valor da soma entre os numeros {n1} {operador} {n2} = {soma} ')

    elif operador == '-':
        subtracao = n1 - n2
        print(f'O valor da subtração entre os numeros {n1} {operador} {n2} = {subtracao} ')

    elif operador == '*':
        multiplicacao = n1 * n2
        print(f'O valor da multiplicação entre os numeros {n1} {operador} {n2} = {multiplicacao} ')

    elif operador == '/':
        divisao = n1 / n2
        print(f'O valor da divisão entre os numeros {n1} {operador} {n2} = {divisao} ')
    else:
        print('Isso nunca deveria aconter!!!')

    sair = input('Quer sair? [S]im: ').lower().startswith('s')
   
    if sair is True:
        break

