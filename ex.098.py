from time import sleep
def lin():
    print('-' * 20)
def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}')
    cont = i
    if i < f:
        while cont <=f:
            print(cont, end=' -> ')
            cont += p
            sleep(0.4)
    else:
        while cont >= f:
            print(cont, end=' -> ')
            cont -= p
            sleep(0.4)

print('Contagem regresiva:')
sleep(0.8)
print(contador(10, 0,2))
print('-'*20)

print('contagem progressiva')
sleep(0.8)
print(contador(0, 10, 2))
print(lin())

a = int(input('Escolha um número inicial:'))
b = int(input('Escolha um número final:'))
c = int(input('Escolha o termo:'))
print(contador(a, b, c))
