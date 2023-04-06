aluno = {}
aluno['nome'] = str(input('Nome do aluno:'))
aluno['media'] = float(input('Média:'))
if aluno['media'] >= 7:
    aluno['situação'] = 'aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'recuperação'
else:
    aluno['situação'] = 'reprovado'
for c, i in aluno.items():
    print(f'[{c} e igual {i}')