tupla = ['Elon Musk', 'Jeff Bezos', 'Bernard Arnault', 'Bill Gates',
         'Warren Buffett', 'Larry Page', 'Sergey Brin', 'Larry Ellison', 'Steve Ballmer', 'Mukesh Ambani']
while True:
    print(''' Os 10 homens mais rico do mundo
    [ 1 ] OS 5 mais rico do mundo
    [ 2 ] Os 4 últimos mais rico do mundo
    [ 3 ] Lista em ordem alfabetica
    [ 4 ] Em que posição estar Bill gates''')
    esc = 0
    while True:
        esc = int(input('Qual opção você deseja?'))
        if esc <= 4:
            break
        print('Opção invalidade, tente novamente.', end= ' ')
    if esc == 1:
        print(tupla[:6])
    elif esc == 2:
        print(tupla[6:])
    elif esc == 3:
        print(sorted(tupla))
    elif esc == 4:
        print(tupla.index('Bill Gates')+1,'º posição')
    continuar = str(input('quer continuar?'))
    if continuar == 'n':
        break
