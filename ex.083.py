expr = str(input('Digite o valor da sua expresão:'))
pilha = []
for valor in expr:
    if valor == '(':
        pilha.append('(')
    elif valor == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
if len(pilha) == 0:
    print('Expressão Válida:')
else:
    print()