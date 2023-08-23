n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
n3 = float(input('Digite o terceiro numero: '))

if n1 > n2 > n3:
    print('O MAIOR numero é o {}, e o MENOR numero é {}'.format(n1, n3))
if n1 > n3 > n2:
    print('O MAIOR numero é o {}, e o MENOR numero é {}'.format(n1, n2))
if n2 > n1 > n3:
    print('O MAIOR numero é o {}, e o MENOR numero é {}'.format(n2, n3))
if n2 > n3 > n1:
    print('O MAIOR numero é o {}, e o MENOR numero é {}'.format(n2, n1))
if n3> n2 > n1:
    print('O MAIOR numero é o {}, e o MENOR numero é {}'.format(n3, n1))
if n3 > n1 > n2:
    print('O MAIOR numero é o {}, e o MENOR numero é {}'.format(n3, n2))




