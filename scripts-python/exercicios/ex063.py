print('=' * 24)
print(' Sequencia de Fibonacci')
print('=' * 24)
f = int(input('Digite um numero: '))

t1 = 0
t2 = 1
tl= 0
i = 1

while i != f:
    tl = t1 + t2
    t1 = t2
    t2 = tl
    i += 1
    print(tl)

