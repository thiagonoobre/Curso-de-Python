from random import randint
print('=' * 40)
print(' {:^35}'.format('JOGA MEGA SENA'))
print('=' * 40)

sort = int(input('Quantos jogos você quer que eu sorteie? R: '))




lista = [[] for _ in range(sort)]

for c in range(0, sort):
    for i in range(0, 6):
        num = randint(0, 60)
        if num not in lista[c]:
            lista[c].insert(i, num)



for h in range(0, sort):
    lista[h].sort()
    print(f'JOGO {h+1}: {lista[h]}')

