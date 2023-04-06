num = ('um', 'dois', 'três', 'quatro', 'cinco','seis',
       'sete', 'oito', 'nove', 'dez')
#escolha = 0
while True:
    while True:
        escolha = int(input('Digite um número de 1 à 10:'))
        if 0 <=escolha <= 10 :
            break
        print('Tente novamente.', end=' ')
    print(num[escolha - 1])
    res = str(input('Quer continuar?')).strip().lower()
    if res == 'n':
        break

