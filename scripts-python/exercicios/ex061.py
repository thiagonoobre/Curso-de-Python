print('CALCULO DE PROGRESSÃO ARITMÉTICA')
print('=' * 32)
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
pa = p
i = 0

while i != 10:
    if i == 0:
        print('PA {}: {}'.format(i+1, p), end=' ')
        i = i + 1
    else:
        pa += r
        print('PA {}: {}'.format(i+1, pa), end=' ')
        i = i + 1



