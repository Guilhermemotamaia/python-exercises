lista = []
while True:
    n = int(input('Digite um valor:'))
    lista.append(n)
    while True:
        cot = str(input('Quer continuar?'))
        if cot == 's' or cot == 'n':
            break
        else:
            print('Opção inválida, tente novamente!')
    if cot == 'n':
        break

if len(lista) == 1:
    print(F'Foi digitado apenas um número')
else:
    print(f'Foram digitados {len(lista)} números.')
lista.sort(reverse= True)
print(f'Lista em forma decrescente: {lista}')
if 5 not in lista:
    print('O valor 5 não foi digitado, portanto não estar na lista')
else:
    print('O valor 5 foi digitado, por isso estar na lista.')