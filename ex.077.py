palavras = ('Banana','Abacaxi', 'Tomate','Guilherme', 'Beatriz', 'Mexixo','Brazil')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end='')