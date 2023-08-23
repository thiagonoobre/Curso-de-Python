'''for c in range(1, 10):
    print(c)
print('Fim!')'''

'''c = 1
while c < 10:
    print(c)
    c = c + 1
print('Fim!')'''
n = 1
np = 0
ni = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n % 2 == 0 and n != 0:
        np = np + 1
    elif n % 2 == 1 and n != 0:
        ni = ni + 1
print('São {} numero pares'.format(np))
print('São {} numero impares'.format(ni))
print('Acabou')
