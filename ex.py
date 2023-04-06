lista = [1, 2, 12, 28, 128, 1228, 2812, 3]
print(lista)
cont = 0
while True:
     if cont == 0:
        primeiro = str(input('Quer excluir algum número?')).strip().lower()
        if primeiro == 'n':
            break
        if primeiro == 's':
            num = int(input('Qual número vai excluir?'))
            cont += 1
            lista.remove(num)
            print('Nova lista:'.upper())
            print(lista)
            conti = str(input('Quer continuar?'))
            if conti == 'n':
                break
        else:
            print('Opção inválida, tente novamente!')
     if cont != 0:
        num = int(input('Qual número vai excluir?'))
        cont += 1
        lista.remove(num)
        print('Nova lista:'.upper())
        print(lista)
        conti = str(input('Quer continuar?'))
        if conti == 'n':
            break







