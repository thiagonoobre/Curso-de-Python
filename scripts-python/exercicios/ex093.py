gols = []
jogador = dict()
total = 0

jogador['Nome'] = str(input('Nome: '))

partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))

for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {c+1}: ')))
    jogador['gols'] = gols[:]
    total += gols[c]
    jogador['total'] = total

print('=-' * 40)
print(jogador)
print('=-' * 40)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('=-' * 40)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas')

for i, v in enumerate(gols):
    print(f'Na partida {i+1}, fez {v} gols')
print(f'Foi um total de {jogador["total"]}')





