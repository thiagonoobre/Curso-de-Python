print('CALCULO DE PROGRESSÃO ARITMÉTICA')
print('=' * 32)
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
pa = p

for c in range(0, 10):
    if c == 0:
        print('PA {}: {}'.format(c+1, p))
    else:
        pa += r
        print('PA {}: {}'.format(c+1, pa))