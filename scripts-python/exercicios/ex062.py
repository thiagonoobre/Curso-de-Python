print('CALCULO DE PROGRESSÃO ARITMÉTICA')
print('=' * 32)
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
pa = p
i = 1
t = 10
while i <= 10:
    if i == 1:
        print('PA {}: {}'.format(i, p), end=' -> ')
        i = i + 1
    else:
        pa += r
        print('PA {}: {}'.format(i, pa), end=' -> ')
        i = i + 1

while t != 0:
    t = int(input('Mais quantos termos você quer ver: '))
    j = i + t
    while i <= j:
        pa += r
        print('PA {}: {}'.format(i, pa), end='->')
        i = i + 1



