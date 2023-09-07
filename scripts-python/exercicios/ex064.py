n = 0
r: int = 0
a = 0
while n != 999:
    n = int(input('Digite um numero: '))
    r = n + a
    a = r
    if n == 999:
        r = r - 999


print('a Soma dos valores é {}'.format(r))
