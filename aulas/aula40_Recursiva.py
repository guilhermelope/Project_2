def recusiva(inicio=0, fim=10): #função que retorna ela msm 
    if inicio >= fim:
        return fim
    
    print(inicio, fim)
    
    inicio += 1
    return recusiva(inicio, fim)

def factorial(n):
    if n <= 1:
        return 1
    
    return n * factorial(n - 1)

print(factorial(5))
print(factorial(10))
