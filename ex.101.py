def voto(idade = 0):
    if idade >= 18 and idade < 60:
        print(f'you have {idade} years old!', end=' ')
        print('Your vote is mandatory!')
    elif idade <= 17 and idade >=16 or idade >= 60:
        print(f'you have {idade} years old!', end=' ')
        print('Your vote is optional')
    elif idade < 16:
        print(f'you have {idade} years old!', end=' ')
        print('You cannot vote')

voto(10)
voto(12)
voto(29)
voto(18)
voto(17)
voto(15)
voto(16)
voto(60)
voto(61)
voto(59)

cont = 0
c = ' '
while c != 'n':
    i = int(input('what year were you born?'))
    nascimento = 2022 -i
    voto(nascimento)
    c = str(input('Quer continhar?')).lower()
    cont += 1
if cont == 1:
    print(f'{cont} person')
else:
    print(f'{cont} peoples')
