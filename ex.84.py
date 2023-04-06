lista1 = []
lista2 = []
cont = maior = menor = 0
while True:
    lista1.append(str(input('Nome:')))
    lista1.append(int(input('Peso:')))
    if len(lista1) == 0:
        maior = menor = lista1[1]
    else:
        if lista1[1] > maior:
            maior = lista1[1]
        if lista1[1] < menor:
            menor = lista1[1]
    lista2.append(lista1[:])
    lista1.clear()
    cont +=1
    c = str(input('Quer continuar?'))
    if c == 'n':
        break
print(lista2)
print(f'Você cadastou {cont} pessoas')
print(f'O maior peso foi de {maior}KG e o menor de {menor}KG')
