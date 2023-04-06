from random import  randint
from time import sleep

print('='*20)
print('Jogo da matemática')
print('='*20)

cont = 0
while True:
    criadormatematico = randint(1,13), randint(1,100)
    respostadojogador = int(input(f'{criadormatematico[0]} x {criadormatematico[1]} ='))

    alternativacerta = criadormatematico[0]*criadormatematico[1]


    if respostadojogador == alternativacerta:
        print('parabéns, você acertou!')
        cont +=1
    else:
        print(f'Você errou! A resposta certa é {alternativacerta}')
    continuar = str(input('Quer continuar?'))
    if continuar == 'n':
        break
if cont > 1:
    print(f'Você acertous {cont} cálculos matemáticos.')
else:
    print(f'Você acertous {cont} cálculo matemático.')