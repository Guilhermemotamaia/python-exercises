print('='*40)
print("BEM VINDO AO PEDRA PAPEL E TESOLRA!")
print('='*40)
from time import sleep
from random import randint

pc = randint(1,3)



print('Pedra = 1'.upper())
sleep(0.5)
print('Papel = 2'.upper())
sleep(0.5)
print('Tesoura = 3'.upper())


jogador = int(input('Qual e a sua jogada?'))
lista = ['pedra', 'papel', 'tesoura']

if jogador == pc:
    print('Infelizmente deu empate')


elif jogador == 1 and pc == 2:
    print(f'eu joguei {lista[pc -1]} e você jogou {lista[jogador -1]}')
    print('Então eu ganhei')
elif jogador == 1 and pc ==3:
    print(f'eu joguei {lista[pc - 1]} e você jogou {lista[jogador - 1]}')
    print('Você ganhou')

elif jogador == 2 and pc == 1:
    print(f'eu joguei {lista[pc - 1]} e você jogou {lista[jogador - 1]}')
    print('Você ganhou')
elif jogador == 2 and pc ==3:
    print(f'eu joguei {lista[pc - 1]} e você jogou {lista[jogador - 1]}')
    print('Então eu ganhei')


elif jogador == 3 and pc == 1:
    print(f'eu joguei {lista[pc - 1]} e você jogou {lista[jogador - 1]}')
    print('Então eu ganhei')
elif jogador == 3 and pc == 2:
    print(f'eu joguei {lista[pc - 1]} e você jogou {lista[jogador - 1]}')
    print('Você ganhou')