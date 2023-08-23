s = 0
cont = 0
for c in range(1, 501):
    if c % 2 == 1:
        if c % 3 == 0:
            cont += 1
            s += c

print('A toma dos {} valores impares multiplos de três são {}'.format(cont, s))
