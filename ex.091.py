from random import randint
from time import sleep
from operator import  itemgetter
jogador1 = randint(1,50)
jogador2 = randint(1,50)
jogador3 = randint(1,50)
jogador4 = randint(1,50)
jog = {'jogador 1': jogador1, 'Jogador 2': jogador2, 'jogador 3': jogador3, 'jogador 4': jogador4}
rank = []
for c, i in jog.items():
    print(f'{c} tirou {i} nos dados')
    #sleep(0.7)
rank = sorted(jog.items(), key= itemgetter(1), reverse= True)
for c, i in enumerate(rank):
    print(f'{c+1}º lugar: {i[0]} com {i[1]}')
