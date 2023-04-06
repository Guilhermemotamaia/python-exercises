lista = []
while True:
    n = int(input('Digite um valor:'))
    if n not in lista:
        lista.append(n)
    else:
        print('Desculpe, não vou adicionar! Número já se encontra na lista')
    while True:
        co = str(input('Quer continuar?'))
        if co == 'n' or co == 's':
            break
        if co != 'n' or co !='s':
            print('Opção inválida, Tente novamente!')
    if co == 'n':
        break
print(f'Essa e a lista: {lista}')
lista.sort()
print(f'Essa e a lista em ordem crescente: {lista}')
lista.sort(reverse= True)
print(f'Essa e a lista em ordem decrescente: {lista}')
