dados = dict()
galera = list()
cont = id = mu = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome:'))
    cont += 1
    dados['idade'] = int(input('Idade:'))
    id += dados['idade']
    while True:
        dados['sexo'] = str(input('Sexo: [M/F]')).strip().upper()
        if dados['sexo'] == 'F':
            mu += 1
        if dados['sexo'] not in 'MF':
            print('Opção inválida! Responda apena M ou F')
        else:
            break
    galera.append(dados.copy())
    c = str(input('Quer continuar? [S/N]')).lower()[0]
    if c == 'n':
        break
    if c not in 'sn':
        print('Opção inválida! Responda apena S ou N')
media = id / cont
print(f'A) Fora cadastradas {cont} pessoas.')
print(f'B) A média de idade é {media}')
print(f'C) Foram cadastradas {mu} mulheres')
print(galera)

