

caminho_arquivo = 'C:\\Users\\guisl\\Desktop\\Nova pasta Atenção\\'
caminho_arquivo += 'aula41.txt'

#arquivo = open(caminho_arquivo, 'w')
#arquivo.close()

with open(caminho_arquivo, 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())