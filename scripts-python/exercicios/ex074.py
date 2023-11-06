from random import randint

sorteio = (randint(0, 10,), randint(0, 10,), randint(0, 10,), randint(0, 10,), randint(0, 10,))
print('Os valores sorteados foram: ', end='')
for n in sorteio:
    print(f'{n} ', end='')

maior = sorteio[0]

if sorteio[1] > maior:
    maior = sorteio[1]

if sorteio[2] > maior:
    maior = sorteio[2]

if sorteio[3] > maior:
    maior = sorteio[3]

if sorteio[4] > maior:
    maior = sorteio[4]

menor = sorteio[0]

if sorteio[1] < menor:
    menor = sorteio[1]

if sorteio[2] < menor:
    menor = sorteio[2]

if sorteio[3] < menor:
    menor = sorteio[3]

if sorteio[4] < menor:
    menor = sorteio[4]

print('\nO maior valor é {}'.format(maior))
print('O menor valor é {}'.format(menor))

print(f'O maior valor sorteado foi {max(sorteio)}')
print(f'O menor valor sorteado foi {min(sorteio)}')

