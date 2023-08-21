a = 18 
b = 2

try: #Captura o erro para ser tratado#
    c = a / b
    
except(ZeroDivisionError) as error: #Trata um Erro#
    print('Dividiu por 0')
    print("MSG: ", error)
    print("Nome: ", error.__class__.__name__)

else:
    print("não de erro")

finally: #Sempre sera execultado#
    print("fechar")

print('continuar')