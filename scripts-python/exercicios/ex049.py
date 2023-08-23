print('      TABUADA')
print('=' * 20)
n = int(input('Digite um numero: '))
for c in range(0, 11):
    r = n * c
    print('{} x {} = {}'.format(n, c, r))
