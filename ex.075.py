num = (int(input('Digite um número:')),
       int(input('Digite outro número:')),
       int(input('Digite mais um número:')),
       int(input('Digite o ultimo número:')))
print(f'O número 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O primeiro valor 3 apareceu na {num.index(3)+1}º pergunta')
else:
    print('O valor 3 não foi digitado.')
print(f'Os valores pares digitado foram', end=' ')
for n in num:
    if n % 2 ==0:
        print(n,end=' ')
