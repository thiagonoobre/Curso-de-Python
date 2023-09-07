print('=' * 26)
print('   PROGRAMA DE FATORIAL')
print('=' * 26)
tf = 1
f = 0
h = 1
n = int(input('Digite um numero inteiro: '))
while n != tf:
    if tf == 1:
        f = (n - tf)
        h = n * f
        tf = tf + 1
    f = (n - tf)
    h = h * f
    tf = tf + 1

print('A fatorial de {} é o valor {}'.format(n, h))
