import math
ang = float(input('Digite um valor de um angulo: '))

s = math.sin(math.radians(ang))
c = math.cos(math.radians(ang))
t = math.tan(math.radians(ang))

print('O seno é {:.2f}, cosseno é {:.2f} e tangente {:.2f} do angulo {}°'.format(s, c, t, ang))