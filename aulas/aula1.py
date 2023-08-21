altura = input('Digite sua altura: ')
sexo = input('Digite seu sexo m/f: ')

if sexo == 'm':
    peso_ideal = (72.7 * float(altura)) - 58
    print(f'O peso ideal para o sexo Masculino é, {peso_ideal} kg')
elif sexo == 'f':
    peso_ideal = (62.1 * float(altura)) - 44.7
    print(f'O peso ideal para o sexo Feminino é, {peso_ideal} kg')
