def lin(msg):
    print('-'*42)
    print(msg.center(42))
    print('-' * 42)

def menu(lista):
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    opc = leiaint('Sua opção:')


def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except:
            print('Erro: digite um numero válido:')
            continue
        else:
            return  n







lin('Menu Principal')
res = menu(['Cadastrar nova pessoa', 'Vizualizar a ficha de cadastro', 'sair do programa'])


