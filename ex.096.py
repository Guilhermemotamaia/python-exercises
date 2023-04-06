def area(l, a):
    ar = l * a
    print(f'A area do terreno {l}x{a} e de {ar} metros')


print('controle de terrenos')
print('-'*22)
larg = float(input('Largura:'))
alt = float(input('Altura:'))
area(larg, alt)
