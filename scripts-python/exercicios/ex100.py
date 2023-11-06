from random import randint
numeros = list()

def sorteio(num):
    for c in range(0, 5):
        num.append(randint(1, 10))
    print('Soteado 5 valores da lista: ', end='')
    for c in num:
        print(c, end=' ')
    print('Pronto!')
def somaPar(num):
    soma = 0
    for c in num:
        if c % 2 == 0:
            soma += c
    print(f'A soma dos valores pares de {num}, temos {soma}')


sorteio(numeros)
somaPar(numeros)