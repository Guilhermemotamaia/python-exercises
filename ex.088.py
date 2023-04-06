from random import randint
lista = []
jogos =[]
cont = tot = 0
print('-'*20)
print('JOGA NA MEGA SENA')
print('-'*20)
n = int(input('Quantas jogos você quer que eu sorteie?'))
for n in range(0,5):
    while True:
        num = randint (1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    jogos.append(lista[:])
    lista.clear()
    print(jogos)

