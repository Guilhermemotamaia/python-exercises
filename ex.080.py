lista = []
cont = co = 0
for c in range(0,5):
    n = int(input('Digite um número:'))
    lista.insert(n,cont)
    print(f'O valor {n} foi adicionado na posição {cont}')
    cont+= 1
print(lista)
lista.sort()
print(f'Essa e a lista em ordem crescente: {lista}')