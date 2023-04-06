dados = dict()
dados['nome'] = str(input('Nome: '))
from datetime import  datetime
nas = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nas
dados['CTPS'] = int(input('Carteira de trabalho:'))
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano da contratação:'))
    dados['Sálario'] = int(input('Sálario: R$'))
    dados['Aposentadoria'] = dados['Contratação'] + 35 - datetime.now().year
print(dados)