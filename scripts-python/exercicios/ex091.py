from random import randint
import time
from operator import itemgetter

jogador = dict()
sorteio = list()

for c in range(0, 5):
    jogador[c] = randint(1, 6)


for k, v in jogador.items():
    print(f'O Jogador{k+1} tirou {v} no dado')
    time.sleep(1)

sorteio = sorted(jogador.items(), key=itemgetter(1), reverse=True)

print('=-' * 20)
print('RANKING DOS JOGADORES')
for i, v in enumerate(sorteio):
    print(f'{i+1}° lugar: jogador{v[0]} com {v[1]}')
