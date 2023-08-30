import os

caminho_arquivo = 'C:\\Users\\guisl\\Desktop\\Nova pasta Atenção\\'
caminho_arquivo += 'aula41.txt'

#arquivo = open(caminho_arquivo, 'w')
#arquivo.close()

with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
    arquivo.write('Atenção\n')
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(('Linha 3\n', 'Linha 4\n'))

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())

