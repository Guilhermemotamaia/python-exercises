c = ''
from time import sleep

while True:
    c = str(input('function or library:')).lower()
    if c in 'stop':
        break

    print(f'accessing the command manual {c}')
    print('.....',end=' ')
    sleep(0.5)
    print('.....',end=' ')
    sleep(0.5)
    print('.....',end=' ')
    sleep(0.5)
    print(help(c))

