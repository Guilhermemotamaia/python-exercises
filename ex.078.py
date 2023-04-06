lista = []
maior = menor = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c}:')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print(lista)
print(f'O menor número da lista é o {menor} na posição',end=' ')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...')
print(f'O maior número da lista é o {maior} na posição', end=' ')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...')
