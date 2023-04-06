def ficha(jog = '<unknow', gol =0):
    print(f'The player {player} scored {gol} in the championship')
player = str(input('Play is name :'))
gol = str(input('how many goals did he score:'))
if player == '':
    print(f'<unknown player> scored {gol} goals in the championship')
else:
    print(f'the player {player} scored {gol} goals in the championship!')
if player.isnumeric():
    player = int(player)
else:
    ficha(player, gol)



print(ficha())
