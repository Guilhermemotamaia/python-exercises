lista = []
listap = []
listai = []
cont = 0
while cont < 7:
    c = int(input(f'Digite o {cont+1}º valor:'))
    cont += 1
    lista.append(c)
    if c % 2 == 0:
        listap.append(c)
    else:
        listai.append(c)
print(lista)
print(listap)
print(listai)
lista.sort()
listai.sort()
listap.sort()
print('LISTA EM ORDEM CRESCENTE:')
print(f'Lista integral: {lista}')
print(f'Lista par: {listap}')
print(f'Lista ímpar: {listai}')