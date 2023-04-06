from random import randint
def lin(msg):
    print('-'*len(msg))
    print(msg)
    print('-' * len(msg))


cont = 0
from time import sleep
pc = randint(1,3)

#ME
es = ''
while es in 's':
    lin('\033[1:33:40mROCK SCISSORS PAPER\033[m')
    print('ROCK == 1')
    sleep(0.5)
    print('SCISSORS == 2')
    sleep(0.5)
    print('PAPER == 3')
    sleep(0.5)

    es = 's'
    l = ['none', 'rock', 'scissors', 'paper']
    i = int(input('What is your Move?'))
    me =(l[i])

    #   CONDIÇÕES !!!!
    print(f'\033[0:33mI chose {l[pc]}\033[m and \033[0:34mYou chose {l[i]}\033[m')
    if l[pc] == l[i]:
        print('tied')

    if l[pc] in 'rock' and l[i] in 'paper':
        print('You win player')
        cont += 1


    if l[pc] in 'rock' and l[i] in 'scissors':
        print('You lose')


    if l[pc] in 'paper' and l[i] in'rock':
        print('You lose')

    if l[pc] in 'paper' and l[i] in 'scissors':
            print('You win')
            cont += 1


    if l[pc] in 'scissors' and l[i] in'pedra':
        print('You win')
        cont += 1
    if l[pc] in 'scissors' and l[i] in 'paper':
            print('You lose')
    es = str(input('Play again?'))
    if es in 'n':
        break
print(f'Você ganhous {cont} vezes de mim')

