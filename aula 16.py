tu = ('maça', 2, 'Banana', 2.5,'granola', 4,'Abacate', 3.5,'pizza', 3,'Red Bull', 2.2)
print('-'*20)
print('LISTAGEM DE PREÇO')
print('-'*20)
for c in range(0,len(tu)):
    if c % 2 == 0:
        print(f'{tu[c]:.<30}', end=' ')
    else:
        print(f'R${tu[c]:.2f}')