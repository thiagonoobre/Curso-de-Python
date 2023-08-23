import random
num = random.randint(0, 10)
print('Tente descobrir que eu estou pensando de 0  a 10')

us = int(input('Digite o numero: '))
tot = 0
while num != us:
    print('Você errou!!! Tente novamente.')
    us = int(input('Digite o numero: '))
    tot = tot + 1
print('Você descobriu estou pensando no numero {}  :('.format(num))
print('Você precisou de {} posibilidade(s) para acerta.'.format(tot))
