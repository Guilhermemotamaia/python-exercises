def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except:
            print('ERRO: Digite um número inteiro válido!')
            continue
        else:
            return n

def lin(msg):
    print('-'*len(msg))
    print(msg)
    print('-'*len(msg))



list = ['Pedro', 'João', 'kassio', 'Guilherme', 'Fabio']


def haha(msg):
    num = int(input('Your Position:'))
    if num == 1:
        print(list)
    elif num == 2:
        s = str(input('Person name:'))
        a = list.append(s)




while True:
    lin('MAIN MENU')
    print('''    \033[0:31m1\033[m - See registered people
    \033[0:31m2\033[m - register new people
    \033[0:31m3\033[m -Exit the systhem''')
    haha('Your position')

