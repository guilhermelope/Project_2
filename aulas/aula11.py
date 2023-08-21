

numero_str = input('Vou dobrar o numero q vc digitar: ')

try:
    numero_float = float(numero_str)
    print(f'O dobro do numero digitado é {numero_str * 2}')
except:
    print('Isso não é um numero')
