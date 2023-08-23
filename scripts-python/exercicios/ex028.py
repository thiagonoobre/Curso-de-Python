import random
num = random.randint(0, 5)
print('Tente descobrir que eu estou pensando de 0  a 5')
us = int(input('Digite o numero: '))
if num == us:
    print('Você descobriu estou pensando no numero {}  :('.format(num))
else:
    print('ERROU!!! kkkkk. O numero é {}'.format(num))
