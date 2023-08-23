print('======  Conversor de Dolares =====')
n = float(input('Quantos Reais você tem: '))
di = n // 3.27
d = n / 3.27
r = (d - di) * 100

print('Você tem {:0.0f} Dolares {} Centavos'.format(di, int(r)))

