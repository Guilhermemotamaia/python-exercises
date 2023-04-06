lista = []
lista1 = []
lista2 = []
while True:
    n = int(input('Digite um valor:'))
    lista.append(n)
    if n % 2 == 0:
        lista1.append(n)
    else:
        lista2.append(n)
    while True:
        cot = str(input('Quer continuar?'))
        if cot == 's' or cot == 'n':
            break
        else:
            print('Opção inválida, tente novamente!')
    if cot == 'n':
        break
print(f'Lista: {lista}')
print(f'Lista par: {lista1}')
print(f'Lista impar: {lista2}')