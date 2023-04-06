from  random import randint
def sortei(lista):
    for c in range(0,5):
        lista.append(randint(1,10))

def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista} temos  {soma}')

num = list()
sortei(num)
somapar(num)
print(num)
