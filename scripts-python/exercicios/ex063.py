print('=' * 24)
print(' Sequencia de Fibonacci')
print('=' * 24)
f = int(input('Digite um numero: '))

t1 = 0
t2 = 1
tl = 0
i = 2

while i != f:
    if t1 == 0 and t2 == 1:
        print('{} -> {}'.format(t1, t2), end=' ')
    tl = t1 + t2
    t1 = t2
    t2 = tl
    i += 1
    print('-> {} '.format(tl), end=' ')
