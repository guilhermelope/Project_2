s1 = {1, 2, 3}
s2 = {2,3,4,5,6}
s3 = {3,6,4,7}
s4 = {1,4,8,5}
uniao = s1 | s2
uniao2 = s3 | s4
interseccao = s1 & s2
diferenca = s1 - s2
diferenca_simetrica = s1 ^ s2

print(s1)
print(uniao)
print(interseccao)
print(diferenca)
print(diferenca_simetrica)
print(uniao | uniao2 )
